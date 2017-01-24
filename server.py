from flask import Flask , render_template, request

my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
	return render_template('index.html')

@my_flask_app.route('/inf/')
def info():
	return render_template('info_gl_str.html')	

@my_flask_app.route('/login/',methods = ['POST'])
def login():
		return render_template('login.html',email=request.form.get("email"), password=request.form.get("passwd"))	

if 	__name__ == "__main__":
	my_flask_app.run(debug=True)
