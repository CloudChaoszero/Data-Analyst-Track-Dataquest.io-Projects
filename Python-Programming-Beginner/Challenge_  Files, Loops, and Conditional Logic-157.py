## 3. Read the File Into a String ##

op = open("dq_unisex_names.csv",'r')
names = op.read()


## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")

first_five=[]
for nam in names_list[0:5]:
    first_five.append(nam)
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
nested_list = []
for cr in names_list:
    
    nested_list.append(cr.split(",")) #For every item in names_list, we split by the comma delim. Thereafter, it is saved to the nested_list list

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list=[]
for line in nested_list:
    line[1]=float(line[1])
    numerical_list.append(line)

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater=[]
for cl in numerical_list:
    if cl[1]>=1000:
        thousand_or_greater.append(cl[0])
print(thousand_or_greater[0:5])