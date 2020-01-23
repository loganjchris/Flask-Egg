from flask import escape, flash, Flask, render_template, request, session
from wtforms import Form

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d4e41f2b6176a'


@app.route("/", methods=['GET', 'POST'])
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

@app.route("/logout", methods= 'GET')
def logout():

    session.pop('room_number', None)

if __name__ == "__main__":
    app.run()
#    app.run(host="0.0.0.0", port=1234)