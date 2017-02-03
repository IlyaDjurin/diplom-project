from flask import Flask , render_template, request
from db_magazina import Kategor, Tovar, Tovar_photo


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

@my_flask_app.route('/smart/', methods = ['get'])
def category():
	t = Tovar()
	t1=Tovar_photo()
	c=t1.query.get(2).tovarphoto_image
	print(c)
	a=t.query.get(5).tovar_name
	b=t.query.get(5).tovar_info
		
	return render_template('smartfons.html', baza = a , baza1 = b , baza2 = c , baza3 =  t1.query.get(3).tovarphoto_image, \
		 baza4 = t1.query.get(3).tovari.tovar_info ,  baza5 = t1.query.get(3).tovari.tovar_name,\
		 baza6 = t1.query.get(4).tovarphoto_image , baza7 = t1.query.get(4).tovari.tovar_info ,baza8 = t1.query.get(4).tovari.tovar_name,\
		 baza9 = t1.query.get(5).tovarphoto_image , baza10 = t1.query.get(5).tovari.tovar_info ,baza11 = t1.query.get(5).tovari.tovar_name)

if 	__name__ == "__main__":
	my_flask_app.run(debug=True)
