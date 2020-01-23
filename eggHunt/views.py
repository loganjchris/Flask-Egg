from eggHunt import eggHunt
from flask import escape, flash, Flask, render_template, request, session

@eggHunt.route("/", methods=['GET', 'POST'])
def hello():
    
    error = None
    if request.method == 'GET':
        if 'room_number' not in session:
            session['room_number'] = 1817
            session.modified = True 

    if request.method == 'POST':
        if session['room_number'] == 1818:
            flash(r"The first part of the code is {storage hacks}")
        else:
            error = "Who's on first"
            session['room_number'] = 1818
    return render_template('hello.html', error=error)

@eggHunt.route("/logout")
def logout():
    session.pop('room_number', None)
