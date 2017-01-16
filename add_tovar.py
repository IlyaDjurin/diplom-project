from db_magazina import Tovar , db_session, Kategor

tovar_list = [{'tovar_name': 'Атлант(холодильник)', 'tovar_info':'Качественный холодильник',\
 'tovar_image':'Картинка холодильника','tovar_made':'Беларусь','tovar_price':'20000','kategory_id' : 2},
 {'tovar_name': 'IPhone', 'tovar_info':'7 и его характеристики ',\
 'tovar_image':'Картинка IPhone','tovar_made':'USA','tovar_price':'70000','kategory_id' : 1},
 {'tovar_name': 'IPhone', 'tovar_info':'6 и его характеристики ',\
 'tovar_image':'Картинка IPhone 6','tovar_made':'USA','tovar_price':'35000','kategory_id' : 1},
 {'tovar_name': 'Воздушный фильтр', 'tovar_info':'Воздушный фильтр Kia Optima ',\
 'tovar_image':'Картинка фильтра','tovar_made':'Korea','tovar_price':'1000','kategory_id' : 3},
 {'tovar_name': 'Mobihell', 'tovar_info':'автомобильная краска акриловая 1 литр ',\
 'tovar_image':'Картинка краски','tovar_made':'Germany','tovar_price':'750','kategory_id' : 3}]

for k in tovar_list:
	tov = Tovar(k['tovar_name'],k['tovar_info'],k['tovar_image'],k['tovar_made'],k['tovar_price'],k['kategory_id'])
	db_session.add(tov)

db_session.commit()