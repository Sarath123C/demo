from flask import Flask, render_template

new=Flask(__name__)

@new.route('/')
def index():
    return render_template('index.html')
@new.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isActive=True)
@new.route('/names')
def name():
    names=['Sarath','Mahesh','Jithu']
    return render_template('name.html',names=names)
new.run(debug=True)
