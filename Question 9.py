#Question 9
#Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop. N: No of students (Read input from user)
#Ex: L1: [150, 155, 145, 148]
#Output: [68.03, 70.3, 65.77, 67.13]

weights_lbs =  [150, 155, 145, 148, 120, 130, 100]
weights_kgs = []
for x in weights_lbs:
   weights_kgs.append(round(x * 0.45359237,2))
print(f"weight in kgs: {weights_kgs}") #[68.04, 70.31, 65.77, 67.13, 54.43, 58.97, 45.36]
