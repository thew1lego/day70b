from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from functools import wraps
from flask import abort
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
    submit = SubmitField("Register!")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login!")

class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")


# def admin_only(function):
#     def wrapper(*args,**kwargs):
#         print(f"You called {fn.__name__}{args}")
#         if current_user.is_anonymous or current_user.id != 1:
#
#             return current_app.login_manager.unauthorized() , f"<p>user is forbidden!</p>"
#         return func(*args, **kwargs)
#     return wrapper


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function

# def admin_only(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         #If id is not 1 then return abort with 403 error
#          try:
#             if current_user.id != 1:
#                 return abort(403)
#          except NameError:
#             return redirect(url_for('login'))
#         #Otherwise continue with the route function
#          else:
#             return f(*args, **kwargs)
#     return decorated_function