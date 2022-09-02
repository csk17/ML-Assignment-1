#Question 2
#•	Create an empty dictionary called dog
dog=dict()   
#•	Add name, color, breed, legs, age to the dog dictionary

dog={"Name":"Mike","Color":"Creamy","Breed":"abc","Legs":"4","Age":"1"}
print(dog)
#•	Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student_dictionary={"first_name":"Sai Krishna Reddy","last_name":"Chevutukur","gender":"male","age":22,"maritial_status":"single","skills":"Java","country":"India","city":"Hyderabad","address":"Hyd-500059"}
print(student_dictionary)
#•	Get the length of the student dictionary

print("Length of the student Dictionary",len(student_dictionary))

#•	Get the value of skills and check the data type, it should be a list

print(student_dictionary["skills"])
print(type("skills"))

#•	Modify the skills values by adding one or two skills

student_dictionary["skills"].append["Javascript","Python"]

#•	Get the dictionary keys as a list

keys = student_dictionary.keys()
print(keys)

#•	Get the dictionary values as a list

values = student_dictionary.values()
print(values)
