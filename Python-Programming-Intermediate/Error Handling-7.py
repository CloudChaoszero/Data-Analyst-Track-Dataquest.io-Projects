## 2. Sets ##

gender = []
for gen in legislators:
    gender.append(gen[3])
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party =[]
for word in legislators:
    party.append(word[6])
party = set(party)
print(party)

for partychec in legislators:
    if partychec[6] == "":
        print(partychec)

## 4. Missing Values ##


for row in legislators:
    if row[3] == "":
        row[3] = "M"
    

## 5. Parsing Birth Years ##

birth_years = []
for row in legislators:
    parts = []
    parts =row[2].split("-")
    birth_years.append(parts[0])

birth_years

## 6. Try/except Blocks ##

try:
    float("Hello")
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##

try:
    int('')
except Exception as ex:
    print(type(ex))
    print(str(ex))

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)

## 9. Convert Birth Years to Integers ##

#birth_year = []
for row in legislators:
    get_b_year = row[2].split("-")[0] 
    try:
        get_b_year = int(get_b_year)
    except Exception:
        get_b_year = 0
    
    row.append(get_b_year)

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]