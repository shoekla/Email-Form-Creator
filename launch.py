from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import time
import os
import em
app = Flask(__name__)

@app.route('/emailFormCreator/')
def goToLogin():
	return render_template("email/EmailHome.html")

@app.route('/emailFormCreator/email/',methods=['POST'])
def emailFormMake(email = None):
	print "Email Method--------"
	email = None
	email = request.form['email']
	email = em.getForm(email)
	return render_template("email/form.html",email = email)
@app.route('/test/')
def em():
	return render_template("email/test.html")
if __name__ == '__main__':
    app.run()