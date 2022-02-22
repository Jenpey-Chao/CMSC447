from flask import Blueprint, redirect, render_template, request,url_for
from .models import User
from . import db
auth = Blueprint('auth', __name__)



@auth.route('/insert')
def insert():
    return render_template('insert.html')

@auth.route('/insert', methods=['POST'])
def insert_post():
    name = request.form.get('name')
    ids = request.form.get('ids')
    points = request.form.get('points')

    #print(name, ids, points)
    user = User.query.filter_by(ids=ids).first()
    if user:
        user.name = name
        user.points = points
        db.session.commit()
    else:
        new_user = User(name=name, ids=ids, points=points)
        db.session.add(new_user)
        db.session.commit()

    return redirect(url_for('main.index'))


@auth.route('/delete')
def delete():
    return render_template('delete.html')

@auth.route('/delete', methods=['POST'])
def delete_post():
    ids = request.form.get('ids')
    user = User.query.filter_by(ids=ids).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('main.index'))