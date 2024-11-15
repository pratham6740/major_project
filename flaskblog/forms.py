from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class SearchForm(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Submit') 


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
        username = StringField('Username',
                               validators=[DataRequired(), Length(min=2, max=20)])
        email = StringField('Email',
                            validators=[DataRequired(), Email()])
        picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
        submit = SubmitField('Update')

        def validate_username(self, username):
            if username.data != current_user.username:
                user = User.query.filter_by(username=username.data).first()
                if user:
                    raise ValidationError('That username is taken. Please choose a different one.')

        def validate_email(self, email):
            if email.data != current_user.email:
                user = User.query.filter_by(email=email.data).first()
                if user:
                    raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    type = SelectField('Type', choices=[('FTE+6M', 'FTE + 6M'),('FTE', 'FTE'), ('Internship', 'Internship(2M/6M)')], validators=[DataRequired()])
    branch = SelectField('Branch', choices=[('cse', 'Computer Science Engineering'),('ece', 'Electronics & Communication Engineering'),('ee', 'Electrical Engineering'), ('mech', 'Mechanical Engineering'),('mme', 'Metallurgical and Materials Engineering'), ('chem', 'Chemical Engineering'),('civil', 'Civil Engineering')], validators=[DataRequired()])
    title = SelectField('Company', choices=[('Other', 'Other'), ('Amazon', 'Amazon'), ('Reliance', 'Reliance'),('Microsoft', 'Microsoft'), ('Vedantaa', 'Vedantaa'), ('MSCI', 'Morgan Stanley Capital International(MSCI)'),('Google', 'Google'),('Oracel', 'Oracel'),('Meesho', 'Meesho'), ('Zomato', 'Zomato'), ('Texas instrument', 'Texas Instrument')], validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    role = StringField('Role', validators=[DataRequired()])
    picture = FileField('Add Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Post')
