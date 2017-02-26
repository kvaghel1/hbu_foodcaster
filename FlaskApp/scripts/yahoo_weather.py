import urllib2, urllib, json

baseurl = "https://query.yahooapis.com/v1/public/yql?"

#yql_query = "select wind from weather.forecast where woeid=2460286"
#location = "'Gandinagar,Gujarat'"
def get_weather(location):
	yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="+ location + ")"
	yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
	result = urllib2.urlopen(yql_url).read()
	data = json.loads(result)
	#print json.dumps(data)
	#print json.dumps(data['query']['results']['channel']['item']['condition']['temp'])
	#return json.dumps(data['query']['results']['channel']['item']['description'])
	forecast_details = data['query']['results']['channel']['item']['forecast']
	current_cond = json.dumps(data['query']['results']['channel']['item']['condition']['text'])
	current_temp = json.dumps(data['query']['results']['channel']['item']['condition']['temp'])
	#forecast_details =
	html_forecast = ""  
	for i in xrange(5):
		#print i['text'],i['day'],i['date'],i['low'],i['high']
		html_forecast += "<li>" + str(forecast_details[i]['text']) + " " + str(forecast_details[i]['day']) + " " + str(forecast_details[i]['date']) + " " +\
							 str(forecast_details[i]['low']) +"/"+str(forecast_details[i]['high']) + "</li>" 
	return current_cond,current_temp,html_forecast

if __name__ == '__main__':
	print __name__
	#print get_weather(str(382021))
