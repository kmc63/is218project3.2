from app.auth.forms import *
from flask_login import FlaskLoginClient
from app.db.models import User

def test_login_successful(application, client):
    test_login = login_form()
    test_login.email.data = "keith@njit.edu"
    test_login.password.data = "password"
    assert test_login.validate()

def test_login_unsuccessful(application, client):
    test_login = login_form()
    test_login.email.data = "keith@njit.edu"
    test_login.password.data = "pass"
    assert not test_login.validate()