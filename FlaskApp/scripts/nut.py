#UPC Database
from nutritionix import Nutritionix
import json

nix = Nutritionix(app_id="66cb7ae9", api_key="0cede6486dc6177929d950a7f593d406")

def get_nutritions(food_item):
	search_entity = nix.search(str(food_item))
	results = search_entity.json()

	#print json.dumps(results)
	search_results = []
	for result in results['hits']:
		#print json.dumps(result)
		search_results.append(str(result['_id']))
		#a = raw_input("is this the list?")
	#print search_results

	for item_id in search_results:
		#nix.item(id=item_id).json
		#print json.dumps(nix.item(id=str(item_id)).json())
		html_format = ""
		json_item = nix.item(id=str(item_id)).json() 
		# for i in json_item:
		# 	html_format += "<li> " str(i["nf_serving_weight_grams"]) + " g" + \
		# 						str(i["usda_fields"]["VITA_IU"]['desc']) + " " + str(i["usda_fields"]["VITA_IU"]['value']) +\
		# 						str(i["usda_fields"]["VITB12"]['desc']) + " " + str(i["usda_fields"]["VITB12"]['value']) +\
		# 						str(i["usda_fields"]["FE"]['desc']) + " " + str(i["usda_fields"]["FE"]['value']) +\
		# 						str(i["usda_fields"]["PROCTN"]['desc']) + " " + str(i["usda_fields"]["PROCTN"]['value']) +\
		# 						str(i["usda_fields"]["FAT"]['desc']) + " " + str(i["usda_fields"]["FAT"]['value']) +\
		print json_item
		break
		#a = raw_input("Pause...")

if __name__ == '__main__':
	print __name__
	print get_nutritions("Pringles")