from pydoc import render_doc
from flask import Blueprint, render_template, url_for
from .models import User
from . import db
main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    user = User.query.all()
    return render_template('index.html',user=user )


