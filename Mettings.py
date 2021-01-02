from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/auth')
def auth():
    return render_template("index.html")

@app.route('/users/self')
def selfpage():
    return render_template("self.html")

@app.route('/users')
def all_users():
    return 'лента пользователей'

@app.route('/user/<string:name>/<int:id>')
def user_id(name, id):
    return name + str(id)

if __name__ == '__main__':
    app.run(debug=True)