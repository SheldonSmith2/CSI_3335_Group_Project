# The file to control the different routes within the application
from itsdangerous import json

from app import app, db, bcrypt, mail
from app.forms import LoginForm, RegisterForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm, \
    ChangeYearForm
from flask import render_template, flash, redirect, url_for, request
from app.userModel import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from app.baseballModels.modelConnection import getRoster, getStandings, getManagers, getTopSalaries, \
    getTSNAwards, getBBWAAawards, getLatestWSChamp, getWLofDivision, getWSWins, getStats

# The main page for the website
@app.route('/')
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = ChangeYearForm()
    formSalary = ChangeYearForm()
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2019
    if current_user.is_authenticated:
        roster = getRoster(current_user.fav_team, year)
    else:
        roster = ""
    if formSalary.validate_on_submit():
        yearSalary = formSalary.changeYear.data
    elif request.method == 'GET':
        yearSalary = 2016
    salaries = getTopSalaries(yearSalary)
    wschamp = getLatestWSChamp()
    return render_template('dashboard.html', title='Home', roster=roster, form=form,
                           year=year, salaries=salaries, yearSalary=yearSalary, formSalary=formSalary,
                           wschamp=wschamp, **request.args)


@app.route('/getinfo/<id>/<year>', methods=['GET', 'POST'])
def stats(id, year):
    flash("Player " + id + " " + year, 'success')
    player_stats = getStats(id, year, current_user.fav_team)
    toggle = ".show"
    return redirect(url_for('dashboard', toggle=toggle, player_stats=player_stats))


# The route to control the login functionality
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Disallow a logged in user from accessing login page
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    # Check if the login is valid
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # If valid, redirect to dashboard or alternate page
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        flash('Login Unsuccessful.  Please check email and password', 'danger')
    return render_template('login.html', title='Sign In', form=form)


# The route to control the registration functionality
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Disallow a logged in user from accessing registration page
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegisterForm()
    # Check if the registration form is valid
    if form.validate_on_submit():
        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Create a new User and add to the database
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, fav_team=form.fav_team.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!  You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# The route to log out the user
@app.route('/logout')
def logout():
    # Log out the user
    logout_user()
    return redirect(url_for('dashboard'))


# The route to control the logged in user's account information
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        # Update the user's information if the information is valid
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.fav_team = form.fav_team.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        # Populate the fields with the current information
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.fav_team.data = current_user.fav_team
    return render_template('account.html', title='Account', form=form)


# The route to control the about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/managers')
def managers():
    tsnAwards = getTSNAwards(current_user.fav_team)
    bbwaaAwards = getBBWAAawards(current_user.fav_team)
    managerList = getManagers(current_user.fav_team)
    return render_template('managers.html', title='Managers', managerList=managerList,
                           tsnAwards=tsnAwards, bbwaaAwards=bbwaaAwards)


@app.route('/postseason')
def postseason():
    countWS = getWSWins(current_user.fav_team)
    return render_template('postseason.html', title='Post Season Stats', countWS=countWS)


@app.route('/standings', methods=['GET', 'POST'])
def standings():
    form = ChangeYearForm()
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2019
    ALWest = getStandings(year, "AL", "W")
    ALWestWL = getWLofDivision(year, "AL", "W")
    ALEast = getStandings(year, "AL", "E")
    ALEastWL = getWLofDivision(year, "AL", "E")
    ALCentral = getStandings(year, "AL", "C")
    ALCentralWL = getWLofDivision(year, "AL", "C")
    NLWest = getStandings(year, "NL", "W")
    NLWestWL = getWLofDivision(year, "NL", "W")
    NLEast = getStandings(year, "NL", "E")
    NLEastWL = getWLofDivision(year, "NL", "E")
    NLCentral = getStandings(year, "NL", "C")
    NLCentralWL = getWLofDivision(year, "NL", "C")
    return render_template('standings.html', title='Standings', ALWest=ALWest, form=form, year=year, ALWestWL=ALWestWL,
                           ALEast=ALEast, ALEastWL=ALEastWL, ALCentralWL=ALCentralWL, ALCentral=ALCentral, NLWest=NLWest,
                           NLWestWL=NLWestWL, NLEast=NLEast, NLEastWL=NLEastWL, NLCentral=NLCentral, NLCentralWL=NLCentralWL)


# The function to send the reset password email
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


# The function when the user wants to reset their password
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RequestResetForm()
    if form.validate_on_submit():
        # Send email to user
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


# The function to handle resetting a user's password with given token
@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    user = User.verify_reset_token(token)
    if user is None:
        # If the token is invalid then redirect user
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated!  You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
