# The imports in order to create the different forms
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.userModel import User


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
    fav_team = SelectField('Favorite Team', choices=['Houston Astros', 'Oakland Athletics', 'Boston Red Sox', 'New York Yankees', 'Texas Rangers', 'San Diego Padres'], validators=[DataRequired()])
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

    # Validate that the password follows the constraints given
    def validate_password(self, password):
        num_chars = 0
        num_upper = 0
        num_other = 0
        num_letters = 0
        for element in password.data:
            num_chars += 1
            if element.isnumeric():
                num_letters += 1
            elif element.isupper():
                num_upper += 1
            elif not element.islower():
                num_other += 1
        if 8 > num_chars or num_chars > 20 or num_letters <= 0 or num_upper <= 0 or num_other <= 0:
            raise ValidationError('The password does not match the minimum requirements.')


# The class to control updating the account information
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    fav_team = SelectField('Favorite Team', choices=['Houston Astros', 'Oakland Athletics', 'Boston Red Sox', 'New York Yankees', 'Texas Rangers', 'San Diego Padres'], validators=[DataRequired()])
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


class ChangeYearForm(FlaskForm):
    changeYear = StringField('Year', validators=[DataRequired()])
    submit = SubmitField('Change Year')


class SeePlayerInfo(FlaskForm):
    submit = SubmitField('More')
