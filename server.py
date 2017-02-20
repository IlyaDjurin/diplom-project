from flask import Flask , render_template, request
from db_magazina import Kategor, Tovar, Tovar_photo, Tovar_inphoto


my_flask_app = Flask(__name__)

@my_flask_app.route('/')
def index():
	return render_template('index.html')

@my_flask_app.route('/smart/harakter/')
def harakt():
	t1= Tovar_inphoto()
	harackter = Tovar_inphoto.query.filter(Tovar_inphoto.id==1).all()

	return render_template('harakteriskick.html' ,  harackter=harackter)	

@my_flask_app.route('/inf/')
def info():
	return render_template('info_gl_str.html')

@my_flask_app.route('/log1/')
def log1():
	return render_template('login_menu.html')	

@my_flask_app.route('/login/',methods = ['POST'])
def login():
		return render_template('login.html',email=request.form.get("email"), password=request.form.get("passwd"))	
@my_flask_app.route('/smart/')
@my_flask_app.route('/smart/<username>', methods = ['GET', 'POST'])
def category(username=None):
	phone_name = request.args.get('phone_name', False)

	t = Tovar()

	smartfons = t.query.filter(Tovar.kategory_id==1)
	harackter = Tovar_inphoto.query.filter(Tovar_inphoto.id==1).all()
	if phone_name:
		qry = '%{}%'.format(phone_name)
		smartfons = smartfons.filter(Tovar.tovar_name.like(qry))

	if username:
		qry = '%{}%'.format(username)
		smartfons = smartfons.filter(Tovar.tovar_name.like(qry))
	

	check9 = request.args.get('check9', False)	
	check8 = request.args.get('check8', False)
	check7 = request.args.get('check7', False)
	check6 = request.args.get('check6', False)	
	check5 = request.args.get('check5', False)
	check4 = request.args.get('check4', False)	
	check3 = request.args.get('check3', False)	
	check2 = request.args.get('check2', False)
	check1 = request.args.get('check1', False)
	check0 = request.args.get('check0', False)
	checki = request.args.get('checki', False)
	if checki:
		z = [check0,check1,check2,check3,check4,check5,check6,check7,check8,check9]

	
		smartfons=smartfons.filter(Tovar.tovar_name.in_([z[0],z[1],z[2],z[6]]))
		try:
			smartfons= Tovar.query.filter(Tovar.id.in_([Tovar_inphoto.query.filter(Tovar_inphoto.tovarinphoto_diagon.in_([z[3],z[4],z[5]])).all()[0].tovar_id]))
			
		except IndexError:
			pass

		try:
			a = Tovar_inphoto.query.filter(Tovar_inphoto.tovarinphoto_ram.in_([z[7],z[8],z[9]])).all()
			for i in a:
				smartfons= Tovar.query.filter(Tovar.id.in_([i.tovar_id]))
				#smartfons= Tovar.query.filter(Tovar.id.in_([a[0].tovar_id , a[1].tovar_id]))
		except IndexError:
			pass		
		print(smartfons)
			
		smartfons=smartfons.all()
	


	return render_template('smartfons.html', smartfons=smartfons)

if 	__name__ == "__main__":
	my_flask_app.run(debug=True)
