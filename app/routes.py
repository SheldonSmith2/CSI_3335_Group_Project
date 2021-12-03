# The file to control the different routes within the application

from app import app, db, bcrypt, mail
from app.forms import LoginForm, RegisterForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm, \
    ChangeYearForm
from flask import render_template, flash, redirect, url_for, request
from app.userModel import User
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

# Import all of the function to get information from database
from app.databaseControllers.standingsController import getStandings, getWLofDivision, getCurrentTeams
from app.databaseControllers.awardsController import getPlayerAwards, getAllstar, getHallofFame, getManagerAward
from app.databaseControllers.postseasonController import getLgWins, getDivWins, getPostInfo, getWSWins, getRound
from app.databaseControllers.generalController import getRoster, getManagers, getTopSalaries, \
    getAppearances, getPitchingInfo
from app.databaseControllers.favPlayerController import careerBattingPost, careerPitchingPost, careerPitchingStats, \
    careerBattingStats, battingStats, battingPost, postAppearancesBatting, postAppearancesPitching, pitchingPost, \
    pitchingStats, getSumAppearances


# The main page for the website
@app.route('/', methods=['GET', 'POST'])
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = ChangeYearForm()
    formSalary = ChangeYearForm()
    # Set the correct year
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2019
    else:
        year = 2019
    # Load the dashboard with the correct roster
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
                           wschamp=wschamp, pitchingInfo=pitchingInfo)


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
        user = User(username=form.username.data, email=form.email.data, password=hashed_password,
                    fav_team=form.fav_team.data, fav_player=None)
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
        # Check if the user has a favorite player
        if form.fav_player.data == "":
            current_user.fav_player = None
        else:
            current_user.fav_player = form.fav_player.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        # Populate the fields with the current information
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.fav_team.data = current_user.fav_team
        if current_user.fav_player is not None:
            form.fav_player.data = current_user.fav_player
    teams = getCurrentTeams()
    return render_template('account.html', title='Account', form=form, teams=teams)


# The route to control the about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')


# The route that contains all the allstar information based on year
@app.route('/allstar', methods=['GET', 'POST'])
def allstar():
    form = ChangeYearForm()
    # Set the correct year
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2019
    else:
        year = 2019
    #allstarInfo = getAllstar(current_user.fav_team, year)
    allstarInfo = ""
    return render_template('allstar.html', title='All Star', form=form, year=year, allstarInfo=allstarInfo)


# The route that contains all of hall of fame information based on year
@app.route('/halloffame', methods=['GET', 'POST'])
def halloffame():
    form = ChangeYearForm()
    # Set the correct year
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2018
    else:
        year = 2018
    #halloffame = getHallofFame(year)
    halloffame = ""
    return render_template('halloffame.html', title='Hall of Fame', halloffame=halloffame, form=form, year=year)


# The route that controls the player awards base on year
@app.route('/playerawards', methods=['GET', 'POST'])
def playerawards():
    form = ChangeYearForm()
    # Set the correct year
    if form.validate_on_submit():
        year = form.changeYear.data
    elif request.method == 'GET':
        year = 2017
    else:
        year = 2017
    # Get the correct data from the database
    #mvp = getPlayerAwards(year, "Most Valuable Player")
    #cyyoung = getPlayerAwards(year, "Cy Young Award")
    #rookie = getPlayerAwards(year, "Rookie of the Year")
    #comeback = getPlayerAwards(year, "Comeback Player of the Year")
    #hankaaron = getPlayerAwards(year, "Hank Aaron Award")
    #reliever = getPlayerAwards(year, "Reliever of the Year Award")
    mvp = ""
    cyyoung = ""
    rookie = ""
    comeback = ""
    hankaaron = ""
    reliever = ""
    return render_template('playerawards.html', title='Player Awards', year=year, form=form, mvp=mvp, cyyoung=cyyoung,
                           rookie=rookie, comeback=comeback, hankaaron=hankaaron, reliever=reliever)


# The route that controls the manager information for a team
@app.route('/managers')
def managers():
    # Get the data from the database
    #tsnAwards = getManagerAward(current_user.fav_team, "TSN Manager of the Year")
    #bbwaaAwards = getManagerAward(current_user.fav_team, "BBWAA Manager of the Year")
    #managerList = getManagers(current_user.fav_team)
    tsnAwards = ""
    bbwaaAwards = ""
    managerList = ""
    return render_template('managers.html', title='Managers', managerList=managerList, tsnAwards=tsnAwards,
                           bbwaaAwards=bbwaaAwards)


# The route to control the career stats of the user's favorite player
@app.route('/careerstats')
def careerstats():
    #careerPitching = careerPitchingStats(current_user.fav_player)
    #pitching = pitchingStats(current_user.fav_player)
    #careerBatting = careerBattingStats(current_user.fav_player)
    #batting = battingStats(current_user.fav_player)
    #appearances = getSumAppearances(current_user.fav_player)
    careerPitching = ""
    pitching = ""
    careerBatting = ""
    batting = ""
    appearances = ""
    return render_template('careerstats.html', title='Career Stats', careerPitching=careerPitching, careerBatting=careerBatting,
                           appearances=appearances, pitching=pitching, batting=batting)


# The route that controls the career postseason stats of the user's favorite player
@app.route('/careerpostseason')
def careerpostseason():
    # Get all the information from the database
    #careerPitching = careerPitchingPost(current_user.fav_player)
    #pitching = pitchingPost(current_user.fav_player)
    #careerBatting = careerBattingPost(current_user.fav_player)
    #batting = battingPost(current_user.fav_player)
    #appearances = getSumAppearances(current_user.fav_player)
    #postBatting = postAppearancesBatting(current_user.fav_player)
    #postPitching = postAppearancesPitching(current_user.fav_player)
    careerPitching = ""
    pitching = ""
    careerBatting = ""
    batting = ""
    appearances = ""
    postBatting = ""
    postPitching = ""
    return render_template('careerpostseason.html', title='Postseason Stats', postPitching=postPitching,
                           careerPitching=careerPitching, careerBatting=careerBatting,
                           appearances=appearances, pitching=pitching, batting=batting, postBatting=postBatting)


# The route that controls the postseason information for the user's favorite team
@app.route('/postseason')
def postseason():
    #countWS = getWSWins(current_user.fav_team)
    #countDiv = getDivWins(current_user.fav_team)
    #countLg = getLgWins(current_user.fav_team)
    #PostInfo = getPostInfo(current_user.fav_team)
    countWS = ""
    countDiv = ""
    countLg = ""
    PostInfo = ""
    return render_template('postseason.html', title='Post Season Stats', countWS=countWS, countLg=countLg,
                           countDiv=countDiv, PostInfo=PostInfo)


# The route that controls the division standings per year
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
    # Get the postseason round information
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
                           ALEast=ALEast, ALEastWL=ALEastWL, ALCentralWL=ALCentralWL, ALCentral=ALCentral,
                           NLWest=NLWest, NLWestWL=NLWestWL, NLEast=NLEast, NLEastWL=NLEastWL, NLCentral=NLCentral,
                           NLCentralWL=NLCentralWL, WSChamp=WSChamp, ALCS=ALCS, NLCS=NLCS, ALDS1=ALDS1, ALDS2=ALDS2,
                           NLDS1=NLDS1, NLDS2=NLDS2, ALWC=ALWC, NLWC=NLWC)


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
