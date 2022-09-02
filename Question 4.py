#Question 4
#it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'} A = {19, 22, 24, 20, 25, 26} B = {19, 22, 20, 25, 26, 24, 28, 27} age = [22, 19, 24, 25, 26, 24, 25, 24]
#•	Find the length of the set it_companies
#•	Add 'Twitter' to it_companies
#•	Insert multiple IT companies at once to the set it_companies
#•	Remove one of the companies from the set it_companies
#•	What is the difference between remove and discard
#•	Join A and B
#•	Find A intersection B
#•	Is A subset of B
#•	Are A and B disjoint sets
#•	Join A with B and B with A
#•	What is the symmetric difference between A and B
#•	Delete the sets completely
#•	Convert the ages to a set and compare the length of the list and the set.


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
Count_IT= len(it_companies)
print("Total IT companies ",Count_IT)    
it_companies.add("Twitter") 
print("Added new Company ",it_companies)
it_companies.update(["Capgemini","Chase","BOK_Fin"])
print("Added multiple companies ",it_companies)
it_companies.remove("BOK_Fin")
print("After removing one values ",it_companies)
AB_Joined=A.union(B)
print("A Union B ",AB_Joined)
AB_INtersection=A.intersection(B)
print("A Intersection B ",AB_INtersection)
print("is A is subset of B :",A.issubset(B))
print("is A and B are disjoint sets :",A.isdisjoint(B))
print("the symmetric difference between A and B :",A.symmetric_difference(B))
print("deleting set A and B ", A.clear(), B.clear())
AgeSet=set(age)               
print("converted age list to set ",AgeSet)
print("Comparing the length of the list and the set by making difference between length of age list and length of age set is ",len(age)-len(AgeSet))