## 2. Parsing the File ##

weather_data = []
file = open("la_weather.csv",'r')
read = file.read()
rows = read.split("\n")
for r in rows:
    split_row = r.split(",")
    weather_data.append(split_row)
print(weather_data[:5])

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for w_word in weather_data:
    weather.append(w_word[1])

## 4. Counting the Items in a List ##

count = 0
for w_item in weather:
    count += 1

## 5. Removing the Header ##

new_weather = weather[1:] #Took out the header for weather column

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = 'cat' in animals
space_monster_found = 'space_monster' in animals

## 7. Weather Types ##

#List of cross references
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]

weather_type_found = []

for w_type in weather_types:
    #If a word in weather_type is in new_weather, then we add True to w_type_found
    if w_type in new_weather:
        weather_type_found.append(True)
     #Else case   
    else:
        weather_type_found.append(False)