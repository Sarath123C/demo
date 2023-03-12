from flask import Flask, render_template

new=Flask(__name__)

@new.route('/')
def index():
    return render_template('index.html')
@new.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isActive=True)
@new.route('/books')
def book():
    books=[{'name':'Immortals of Meluha','author':'Amish','cover':'https://d1af37c1pl2nfl.cloudfront.net/images/books/tbs/front/immortals-of-meluha-malayalam-version-.jpg'},
           {'name':'Aadujeevitham','author':'Beniyamen','cover':'https://d.gr-assets.com/books/1283726170l/9242236.jpg'},
           {'name':'Randamoozham','author':'MT Vasudevan Nair','cover':'https://d1af37c1pl2nfl.cloudfront.net/images/books/cbt/front/randamoozhammmm.jpg'}]
    return render_template('book.html',books=books)
new.run(debug=True)
