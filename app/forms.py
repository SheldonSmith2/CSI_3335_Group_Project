# The imports in order to create the different forms
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, NumberRange
from app.userModel import User
from app.databaseControllers.standingsController import getCurrentTeams
from app.databaseControllers.generalController import getPlayers

# Get all the current teams that the user can choose for favorite
teams = getCurrentTeams()
teamsForm = []
for team in teams:
    teamsForm.append(team[0])

# The class to handle the login information
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# The class to handle the registration information
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordRepeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    fav_team = SelectField('Favorite Team', choices=teamsForm, validators=[DataRequired()])
    submit = SubmitField('Create Account')

    # Validate that the username is not already taken by another user
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken.  Please choose another one.')

    # Validate that the email is not already taken by another user
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken.  Please choose another one.')


# The class to control updating the account information
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    fav_team = SelectField('Favorite Team', choices=teamsForm, validators=[DataRequired()])
    fav_player = StringField('Favorite Player')
    submit = SubmitField('Update')

    # Validate that the username is not already taken by another user
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken.  Please choose another one.')

    # Validate that the email is not already taken by another user
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken.  Please choose another one.')

    # Validate that the favorite player is a valid player in database
    def validate_fav_player(self, fav_player):
        players = getPlayers()
        isValid = 0
        splitName = fav_player.data.split()
        if fav_player.data != "":
            if len(splitName) == 2:
                for person in players:
                    if person.nameFirst == splitName[0] and person.nameLast == splitName[1]:
                        isValid = 1
            if isValid == 0:
                raise ValidationError('That player is not valid.  Make sure that the first and last name are capitalized.')


# The form in order to initiate a reset password request
class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    # Check that the email has an attached account with it
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email.  You must register first.')


# The form to finalize the reset password functionality
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    passwordRepeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


# The form that is used in order to change the year in many of the pages
class ChangeYearForm(FlaskForm):
    changeYear = IntegerField('Year', validators=[DataRequired(message="Must enter a year"),
                                                  NumberRange(min=1900, max=2020, message="Date must be within 1900-2020")])
    submit = SubmitField('Change Year')


# Form in order to see player info
class SeePlayerInfo(FlaskForm):
    submit = SubmitField('More')
