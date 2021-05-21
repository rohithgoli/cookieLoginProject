from flask import Flask,render_template,request, make_response, redirect, url_for
app = Flask(__name__)


@app.route('/')
def user_login():
    return render_template('login.html')


@app.route('/set', methods = ['POST','GET'])
def set_user_cookie():
    if request.method == 'POST':
        username = request.form['username']
        from_cookie = request.cookies.get('username')
        if username==from_cookie:
            return redirect(url_for('welcome_user'))
        else:
            res = make_response(render_template('welcome.html'))
            res.set_cookie('username',username)
            return res


@app.route('/welcome', methods = ['POST','GET'])
def welcome_user():
    username = request.cookies.get('username')
    return '<h1>Welcome '+username+'</h1>'


if __name__ == '__main__':
    app.run(debug = True)
