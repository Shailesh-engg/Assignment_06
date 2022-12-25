import json
	
# Data to be written
State_Capital ={
"Bihar": "Patna","Goa": "Panaji","Chattisghar": "Naya Raipur","Madhya Pradesh": "Bhopal","West Bengal" : "Kolkata","Maharastra" : "Mumbai","Gujrat" : "Gandhinagar"
}
#  Writing it in the JSONs file
with open("D:\\DS\\Assignment-06\\Statecapital.json","w") as file:
    json_object = json.dump(State_Capital,file)