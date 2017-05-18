## 2. Opening Files ##

a = open("crime_rates.csv", "r") #Returns the file object
#the local variable a is an object that acts as an interface to the file and contains methods for reading it.
f = a
print(a)

## 3. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()
print(data)

## 4. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows=data.split("\n")
print(rows[0:5])

## 6. Practice - Loops ##

ten_rows = rows[0:10]
for numbers in ten_rows:
    print(numbers) #For loop to print every element in the list ten_rows

## 7. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(",")
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

## 8. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data=[]
for num in rows:
    final_data.append(num.split(","))
print(final_data[:5])

## 9. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
length=len(five_elements)
cities_list=[]
for num in range(0,length):
    cities_list.append(five_elements[num][0])

## 10. Looping Through a List of Lists ##

crime_rates = []
cities_list=[]
for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
length=len(final_data)
for num in range(0,length):
    cities_list.append(final_data[num][0])
    

## 11. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n') #Splits data by new line delimiter

print(rows[0:5])

int_crime_rates = []#new list

for n in rows: #get every list in rows list
    split_rows = n.split(",") #split list of list
    
    crime_rate=int(split_rows[1]) #get int value of crime rate
    int_crime_rates.append(crime_rate)