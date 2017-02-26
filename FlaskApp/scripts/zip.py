import urllib, json
import http.client

api_key =  "AIzaSyCU8pm4K5Es8KqVqk4ojzY-G4IwsJPghX0" 

def get_pincode(city):
	try:
		url = "https://maps.googleapis.com/maps/api/geocode/json?address=+"+str(city)+"&key="+str(api_key)
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		return  (str(data['results'][0]['address_components'][0]['long_name']),str(data['results'][0]['formatted_address']))
	except:
		return "No Pincode Found"

if __name__ == '__main__':
	print __name__