from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
users_databese = SQLAlchemy(app)


class Users(users_databese.Model):
	id = users_databese.Column(users_databese.Integer, primary_key=True)
	username = users_databese.Column(users_databese.String(100), nullable=False)
	sex = users_databese.Column(users_databese.String(100), nullable=False)
	datetime_of_registration = users_databese.Column(users_databese.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<User %r>' % self.id


@app.route('/')
@app.route('/auth')
def auth():
	return render_template("index.html")

@app.route('/main')
def main():
	users = Users.query.order_by(Users.datetime_of_registration.desc()).all()
	return render_template("main.html", users=users)

@app.route('/main/<int:id>')
def show_user(id):
	user = Users.query.get(id)
	return render_template("userpage.html", user=user)

@app.route('/users/self')
def selfpage():
	return render_template("self.html")

@app.route('/registration', methods=['POST', 'GET'])
def registrate():
	if request.method == 'POST':
		username = request.form['username']
		sex = request.form['sex']

		user = Users(username=username, sex=sex)

		try:
			users_databese.session.add(user)
			users_databese.session.commit()
			return redirect('/main')
		except:
			return "Ooops"
		
	else:
		return render_template("registration.html")


if __name__ == '__main__':
	app.run(debug=True)