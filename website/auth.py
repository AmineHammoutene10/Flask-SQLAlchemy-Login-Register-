from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html', title="Login page")



@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash ('Account created!', category='success')
            # add user to database
           # new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
           # db.session.add(new_user)
           # db.session.commit()
           # login_user(new_user, remember=True)
           # flash('Account created!', category='success')
           # return redirect(url_for('views.home'))
        
    return render_template('sign_up.html', title="Signup page")