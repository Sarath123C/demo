from flask import Flask
new=Flask(__name__)

@new.route('/profile/<username>')
def profile(username):
    return '<h1>Hello %s<h1>'% username
new.run(debug=True)
