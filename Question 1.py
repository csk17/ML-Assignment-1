#Question 1
#The following is a list of 10 students ages:
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#•	Sort the list and find the min and max age
#•	Add the min age and the max age again to the list
#•	Find the median age (one middle item or two middle items divided by two)
#•	Find the average age (sum of all items divided by their number)
#•	Find the range of the ages (max minus min)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] 
#sorting
ages.sort()                                     
print("sorted List:", ages)                     
#appending
ages.append(min(ages)), ages.append(max(ages))  
print("Updated List : ",ages)
#median age
def medianFunction(data):                        
    med = len(data) // 2
    if not len(data) % 2:
        return (data[med - 1] + data[med]) / 2.0
    return data[med]
print("median age is : ", medianFunction(ages))
#average age
avg = 0 
for int in ages:                                
    avg = avg+int
print("Average age is : ",avg/len(ages)) 
#range        
print("Range of ages is : ", (max(ages)-min(ages)))  