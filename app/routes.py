# The file to control the different routes within the application

from app import app, db, bcrypt, mail
from app.forms import LoginForm, RegisterForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm, \
    ChangeYearForm
from flask import render_template, flash, redirect, url_for, request
from app.userModel import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from app.databaseControllers.standingsController import getStandings, getWLofDivision, getCurrentTeams
from app.databaseControllers.awardsController import getPlayerAwards, getAllstar, getHallofFame, getManagerAward
from app.databaseControllers.postseasonController import getLgWins, getDivWins, getPostInfo, getWSWins, getRound
from app.databaseControllers.generalController import getRoster, getStats, getManagers, getTopSalaries, \
    getAppearances, getPitchingInfo
from app.databaseControllers.sidebarController import getHighestSO, getHighestERA, getHighestWins, \
    getHighestRBI, getHighestBA, getHighestHR


maxHR = getHighestHR()
maxBA = getHighestBA()
maxRBI = getHighestRBI()
maxWins = getHighestWins()
maxSO = getHighestSO()
maxERA = getHighestERA()


# The main page for the website
@app.route('/', methods=['GET', 'POST'])
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = ChangeYearForm()
    formSalary = ChangeYearForm()
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2019
    else:
        year = 2019
    if current_user.is_authenticated:
        roster = getRoster(current_user.fav_team, year)
        appearances = getAppearances(current_user.fav_team, year)
        pitchingInfo = getPitchingInfo(current_user.fav_team, year)
    else:
        roster = ""
        appearances = ""
        pitchingInfo = ""
    if formSalary.validate_on_submit():
        yearSalary = formSalary.changeYear.data
    elif request.method == 'GET':
        yearSalary = 2016
    else:
        yearSalary = 2016
    salaries = getTopSalaries(yearSalary)
    wschamp = getRound(2019, "WS")
    return render_template('dashboard.html', title='Home', roster=roster, form=form, appearances=appearances,
                           year=year, salaries=salaries, yearSalary=yearSalary, formSalary=formSalary,
                           wschamp=wschamp, maxHR=maxHR, maxBA=maxBA, maxRBI=maxRBI, maxWins=maxWins,
                           maxSO=maxSO, maxERA=maxERA, pitchingInfo=pitchingInfo, **request.args)


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
    return render_template('login.html', title='Sign In', form=form, maxHR=maxHR, maxBA=maxBA, maxRBI=maxRBI,
                           maxWins=maxWins, maxSO=maxSO, maxERA=maxERA)


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
    return render_template('register.html', title='Register', form=form, maxHR=maxHR, maxBA=maxBA, maxRBI=maxRBI,
                           maxWins=maxWins, maxSO=maxSO, maxERA=maxERA)


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
    teams = getCurrentTeams()
    return render_template('account.html', title='Account', form=form, teams=teams, maxHR=maxHR, maxBA=maxBA,
                           maxRBI=maxRBI, maxWins=maxWins, maxSO=maxSO, maxERA=maxERA)


# The route to control the about page
@app.route('/about')
def about():
    return render_template('about.html', title='About', maxHR=maxHR, maxBA=maxBA, maxRBI=maxRBI, maxWins=maxWins,
                           maxSO=maxSO, maxERA=maxERA)


@app.route('/allstar', methods=['GET', 'POST'])
def allstar():
    form = ChangeYearForm()
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2019
    else:
        year = 2019
    allstarInfo = getAllstar(current_user.fav_team, year)
    return render_template('allstar.html', title='All Star', form=form, year=year, allstarInfo=allstarInfo, maxHR=maxHR,
                           maxBA=maxBA, maxRBI=maxRBI, maxWins=maxWins, maxSO=maxSO, maxERA=maxERA)


@app.route('/halloffame', methods=['GET', 'POST'])
def halloffame():
    form = ChangeYearForm()
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2018
    else:
        year = 2018
    halloffame = getHallofFame(year)
    return render_template('halloffame.html', title='Hall of Fame', halloffame=halloffame, form=form, year=year,
                           maxHR=maxHR, maxBA=maxBA, maxRBI=maxRBI, maxWins=maxWins, maxSO=maxSO, maxERA=maxERA)


@app.route('/playerawards', methods=['GET', 'POST'])
def playerawards():
    form = ChangeYearForm()
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2017
    else:
        year = 2017
    mvp = getPlayerAwards(year, "Most Valuable Player")
    cyyoung = getPlayerAwards(year, "Cy Young Award")
    rookie = getPlayerAwards(year, "Rookie of the Year")
    comeback = getPlayerAwards(year, "Comeback Player of the Year")
    hankaaron = getPlayerAwards(year, "Hank Aaron Award")
    reliever = getPlayerAwards(year, "Reliever of the Year Award")
    return render_template('playerawards.html', title='Player Awards', year=year, form=form, mvp=mvp, cyyoung=cyyoung,
                           rookie=rookie, comeback=comeback, hankaaron=hankaaron, reliever=reliever, maxHR=maxHR,
                           maxBA=maxBA, maxRBI=maxRBI, maxWins=maxWins, maxSO=maxSO, maxERA=maxERA)


@app.route('/managers')
def managers():
    tsnAwards = getManagerAward(current_user.fav_team, "TSN Manager of the Year")
    bbwaaAwards = getManagerAward(current_user.fav_team, "BBWAA Manager of the Year")
    managerList = getManagers(current_user.fav_team)
    return render_template('managers.html', title='Managers', managerList=managerList, tsnAwards=tsnAwards,
                           bbwaaAwards=bbwaaAwards, maxHR=maxHR, maxBA=maxBA, maxRBI=maxRBI, maxWins=maxWins,
                           maxSO=maxSO, maxERA=maxERA)


@app.route('/postseason')
def postseason():
    countWS = getWSWins(current_user.fav_team)
    countDiv = getDivWins(current_user.fav_team)
    countLg = getLgWins(current_user.fav_team)
    PostInfo = getPostInfo(current_user.fav_team)
    return render_template('postseason.html', title='Post Season Stats', countWS=countWS, countLg=countLg,
                           countDiv=countDiv, PostInfo=PostInfo, maxHR=maxHR, maxBA=maxBA, maxRBI=maxRBI,
                           maxWins=maxWins, maxSO=maxSO, maxERA=maxERA)


@app.route('/standings', methods=['GET', 'POST'])
def standings():
    form = ChangeYearForm()
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2019
    else:
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
    WSChamp = getRound(year, "WS")
    ALCS = getRound(year, "ALCS")
    NLCS = getRound(year, "NLCS")
    ALDS1 = getRound(year, "ALDS1")
    ALDS2 = getRound(year, "ALDS2")
    NLDS1 = getRound(year, "NLDS1")
    NLDS2 = getRound(year, "NLDS2")
    ALWC = getRound(year, "ALWC")
    NLWC = getRound(year, "NLWC")
    return render_template('standings.html', title='Standings', ALWest=ALWest, form=form, year=year, ALWestWL=ALWestWL,
                           ALEast=ALEast, ALEastWL=ALEastWL, ALCentralWL=ALCentralWL, ALCentral=ALCentral, NLWest=NLWest,
                           NLWestWL=NLWestWL, NLEast=NLEast, NLEastWL=NLEastWL, NLCentral=NLCentral, NLCentralWL=NLCentralWL,
                           WSChamp=WSChamp, ALCS=ALCS, NLCS=NLCS, ALDS1=ALDS1, ALDS2=ALDS2, NLDS1=NLDS1, NLDS2=NLDS2,
                           ALWC=ALWC, NLWC=NLWC, maxHR=maxHR, maxBA=maxBA, maxRBI=maxRBI, maxWins=maxWins,
                           maxSO=maxSO, maxERA=maxERA)


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
    return render_template('reset_request.html', title='Reset Password', form=form, maxHR=maxHR, maxBA=maxBA,
                           maxRBI=maxRBI, maxWins=maxWins, maxSO=maxSO, maxERA=maxERA)


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
    return render_template('reset_token.html', title='Reset Password', form=form, maxHR=maxHR, maxBA=maxBA,
                           maxRBI=maxRBI, maxWins=maxWins, maxSO=maxSO, maxERA=maxERA)
