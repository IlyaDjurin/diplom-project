from flask import Flask , render_template, request
from db_magazina import Kategor, Tovar


my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
	return render_template('index.html')

@my_flask_app.route('/inf/')
def info():
	return render_template('info_gl_str.html')

@my_flask_app.route('/log1/')
def log1():
	return render_template('login_menu.html')	

@my_flask_app.route('/login/',methods = ['POST'])
def login():
		return render_template('login.html',email=request.form.get("email"), password=request.form.get("passwd"))	

@my_flask_app.route('/category/<int:cat_id>')
def category(cat_id):
	t = Tovar
	my_tovar = t.query.filter(Tovar.kategory_id == cat_id).all()
	for m in my_tovar:
		print(m.tovar_name)
	return "ok"

if 	__name__ == "__main__":
	my_flask_app.run(debug=True)
