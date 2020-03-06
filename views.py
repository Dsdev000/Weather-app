from app import *


@app.route('/',methods=['GET','POST'])
def weather():
	new_city=request.form.get('search_place')
	url='http://api.openweathermap.org/data/2.5/forecast?q={}&units=imperial&appid=0feff28e59f24064fe087c5cd9c3238d'
	if not new_city:
			new_city='Ahmedabad'

	city=new_city

	r = requests.get(url.format(city)).json()

	weathers=[]

	i=0
	while i<len(r['list']):

		#dictionary to store city and temprature
		wh={
			'city':city,
			'description': r['list'][i]['weather'][0]['description'],
			'temperature': r['list'][i]['main']['temp'],
			'icon':r['list'][i]['weather'][0]['icon'],
			'pressure':r['list'][i]['main']['pressure'],
			'humidity':r['list'][i]['main']['humidity'],
			'wind':r['list'][i]['wind']['speed'],
			'd_t': r['list'][i]['dt_txt']
		}

			
		weathers.append(wh)
		i+=1
		
	i=0

	date_values=''
	dates=''
	times=''
	ddate_values=''
	ddate=''
	dtime=''
	k=0
	init=True
	new_weather=[]
	while i<len(weathers):
		
		if  init==True:

				
			new_weather.append(weathers[i])
			date_values=new_weather[k]['d_t']
			dates,times=date_values.split(' ')
			k+=1
			init=False

		else:
			ddate_values=weathers[i]['d_t']
			ddate,dtime=ddate_values.split(' ')

			if ddate!=dates:

				if dtime==times:

						
					new_weather.append(weathers[i])
					date_values=new_weather[k]['d_t']
					dates,times=date_values.split(' ')
					k+=1
						

						
		i+=1        
		
	return render_template('weather.html',weather=new_weather)