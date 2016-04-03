from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask.ext.login import login_user, logout_user, login_required

from appname.extensions import cache
from appname.forms import LoginForm

import string, random  # to create random filenames
from try_MPSSP import *

main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        N = 10  # length of filename
        entry = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
        with open('Sequences/' + entry, 'w') as fid:
            fid.write(form.sequence.data)

        try:
            predict(entry)
            with open('Results/%s.res' % entry, 'r') as fid:
                features = fid.read()
            flash(features)  # na to doume argotera
        except Exception:
            flash('Could not predict your features. Sorry about that!')

    return render_template("login.html", form=form)
