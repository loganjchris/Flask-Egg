from eggHunt import eggHunt
from flask import escape, flash, Flask, render_template, redirect, request, session, url_for


@eggHunt.route("/", methods=['GET', 'POST'])
def hello():
    '''This is the main page of the Egg hunt. It has a cookie that gets changed on a POST request. Sending a second post request
    with the updated cookie gets the flag. This page also has a javascript flag'''

    error = None

    #TODO who would figure this out? Make something easier
    if request.method == 'GET':
        if 'room_number' not in session:
            session['room_number'] = 1817
            session.modified = True 

    if request.method == 'POST':
        if session['room_number'] == 1818:
            flash(r"You've found the hardest flag! eggFlag{who-made-this}")
        else:
            error = "Who's on first"
            session['room_number'] = 1818
    return render_template('hello.html', error=error),  200, {'Extra Header': r'eggHunt{page-headers-leak-info}'}

@eggHunt.route("/logout")
def logout():
    '''The logout page clears the session settings allowing a reset of the scoreboard.
    It redirects to the hello page afterwards'''

    session.pop('room_number', None)
    session.pop('challenges', None)
    session.pop('flags', None)
    return redirect(url_for("hello"), code=301)

@eggHunt.route("/scoreboard", methods=['GET', 'POST'])
def scoreboard():
    '''The scoreboard page checks submitted flags against a dictionary of flags. If a correct flag is submitted, the counter goes up
    and the session stores the flag as being solved. Duplicates cannot be submitted to increase score'''

    flags = {0:r"eggFlag{extra-points-before-breakfast}", 1:r"eggFlag{who-made-this}", 2:r"eggFlag{view-source}", 3:r"eggHunt{page-headers-leak-info}"}
    
    if 'challenges' not in session:
        session['challenges'] = 0
        session.modified = True
    if 'flags' not in session:
        session['flags'] = {0 : False, 1 : False, 2 : False, 3 : False}
    
    if request.method == 'POST':
        flag = escape(request.form.get('Flag'))

        for i in flags:
            if flag == flags[i]:
                if session['flags'][str(i)]:
                    flash(r"Already Submitted this flag")
                    break
                else:
                    flash(r"Congrats! You've entered a correct flag")
                    session['challenges'] += 1
                    session['flags'][str(i)] = True
                    session.modified = True
                    break

        if not flag or flag == "":
            flash(r"Please enter a flag")

        if flag not in flags:
            flash(r"Incorrect flag")
        
    challenges = session['challenges']

    return render_template('scoreboard.html', challenges=challenges)