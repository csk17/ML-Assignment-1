#Question 3
#•	Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers=("Srikanth","Varun")
print(brothers)                                
sisters=("Spandana","Sravya") 
print(sisters)                                                            

#•	Join brothers and sisters tuples and assign it to siblings

siblings=brothers+sisters
print(siblings)

#•	How many siblings do you have?
 
print("Number of siblings are ",len(siblings))
 
#•	Modify the siblings tuple and add the name of your father and mother and assign it to family_members

siblings=siblings+("Malla Reddy","Kalavathi")
print(siblings)