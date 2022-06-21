from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)

user_dict = {'user1': {'name': 'Yossi', 'email': 'Yossi@gmail.com', 'password': '1212'},
             'user2': {'name': 'or', 'email': 'or@gmail.com', 'password': '1111'},
             'user3': {'name': 'ron', 'email': 'ron@gmail.com', 'password': '8787'},
             'user4': {'name': 'gal', 'email': 'gal@gmail.com', 'password': '4747'},
             'user5': {'name': 'tal', 'email': 'tal@gmail.com', 'password': '4545'}}

usersDetail = list(user_dict.values())

emails = []
for i in range(len(usersDetail)):
    emails.append(usersDetail[i]['email'])


def index_by_email(email):
    for i in range(len(usersDetail)):
        if usersDetail[i]['email'] == email:
            return i


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2_func():
    if request.method == 'GET':
        if 'email' in request.args:
            email = request.args['email']

            if email == '':
                return render_template('assignment3_2.HTML', usersDetail=usersDetail,
                                       message='If you want to search for one user write Email')

            if email in emails:
                index = index_by_email(email)
                username = usersDetail[index]['name']
                user_password = usersDetail[index]['password']
                return render_template('assignment3_2.html', name=username, email=email, password=user_password)
            else:
                return render_template('assignment3_2.HTML', message='not found this user')

    if request.method == 'POST':
        usermail = request.form['mail']
        print(usermail)
        password = request.form['password']
        print(password)
        if password == '' and usermail == '':
            return render_template('assignment3_2.html', message='Fill in the field of the password and email')
        if usermail == '':
            return render_template('assignment3_2.html', message='Fill in the field of the email')
        if password == '':
            return render_template('assignment3_2.html', message='Fill in the field of the password')
        if usermail in emails:
            Index = index_by_email(usermail)
            user_password = usersDetail[Index]['password']
            username = usersDetail[Index]['name']
            print(user_password)
            if user_password == password:
                session['user_name'] = username
                session['logedin'] = True
                return render_template('assignment3_2.html', message='Success')
            else:
                return render_template('assignment3_2.html', message='Wrong password try again!')
        else:
            return render_template('assignment3_2.html', message='Wrong email try again!')
    return render_template('assignment3_2.html')


@app.route('/log_out')
def log_out():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('assignment3_2_func'))


@app.route('/session')
def session_func():
    return jsonify(dict(session))


hobbies_dict = {
    'Trip': 'social',
    'play': 'social',
    'sea': 'social',
    'TV': 'alone',
    'eat': 'alone',
    '': 'alone'
}

social_li = []
alone_li = []

@app.route('/assignment3_1')
def assignment3_1_func():
    social_li.clear()
    alone_li.clear()
    if 'user_hob' in request.args:
        hobbie = request.args.get('user_hob', "")
        if hobbie == '':
            return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                   alone_li=alone_li, message='You did not wrote a hobby')
        for key in hobbies_dict:
            if hobbie.upper() == key.upper():
                session['user_hobbie'] = hobbie
                session['have_hobbie'] = True
                session['hobbieFromList'] = True
                return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li, alone_li=alone_li, message='you choose something from the list')

            else:

                session['user_hobbie'] = hobbie
                session['have_hobbie'] = True
                return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                       alone_li=alone_li, message='The hobby you write is not on the list, interesting!')

    else:
        return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li, alone_li=alone_li)


@app.route('/assignment3_1b')
def assignment3_1b_func():
    social_li.clear()
    alone_li.clear()
    if 'hob_type' in request.args:
        type = request.args.get('hob_type', "")
        if type.lower()=='social':
            social_li.append(session['user_hobbie'])
            return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                   alone_li=alone_li, message='insert social list')
        if type.lower()=='alone':
            alone_li.append(session['user_hobbie'])
            return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                   alone_li=alone_li, message='insert alone list')
        if type.lower()!='social' and type.lower()!='alone':
            return render_template('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li,
                                   alone_li=alone_li, message='You did not make the right choice, choose social or alone')

    return redirect('assignment3_1.html', hobbies_dict=hobbies_dict, social_li=social_li, alone_li=alone_li)

@app.route('/delete_hobbie')
def delete_func():
    session['have_hobbie'] = False
    session['user_hobbie']=""
    session['hobbieFromList'] = False
    social_li.clear()
    alone_li.clear()
    return redirect(url_for('assignment3_1_func'))


@app.route('/')
@app.route('/home')
def index_func():
    return render_template('home.HTML')


@app.route('/contact')
def contact_page():
    return render_template('contact.HTML')


if __name__ == '__main__':
    app.run(debug=True)
