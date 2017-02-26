from flask import Flask,render_template,request,url_for
from scripts.zip import get_pincode
from scripts.yahoo_weather import get_weather

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
#@app.route("/")
def main():
	print "Main"
	
	if request.method == "POST":
		print "Main Post"

	if request.method == "GET":
		print "Main Get"

	# text = request.form['seach_food']
	# print text
	return render_template('index.html')

@app.route("/index",methods=['POST'])
def index():
	print "Index"
	if request.method == "POST":
		print "Index Post Method"
		print "Food--->",request.form['search_food']
		print "Details Entered--->",request.form['search_pincode']
		
		#Pincode,Address
		address_list = get_pincode(request.form['search_pincode'])
		print "Pincode",address_list[0],
		print "Address",address_list[1]
		
		weather = get_weather(address_list[0])
		print "CC:",weather[0]
		return render_template('index.html',temp=address_list[1],current_condition=weather[0].strip('"'),\
				current_temperature=weather[1].strip('"'),weather_forecast=weather[2])

	if request.method == "GET":
		print "Index Get Method"

	# text = request.form['seach_food']
	# print text
	return render_template('index.html')

if __name__ == "__main__":
    app.run()