## 2. Array Comparisons ##

countries_canada = world_alcohol[:,2] == 'Canada'
years_1984 = world_alcohol[:,0] == "1984"

## 3. Selecting Elements ##

country_is_algeria = (world_alcohol[:,2] == "Algeria")
country_algeria = world_alcohol[country_is_algeria, :]

## 5. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria")
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

## 6. Replacing Values ##

is_1986_in_world_alcohol = (world_alcohol[:,0] == "1986")
is_wine_in_world_alcohol = (world_alcohol[:,3] == "Wine")
world_alcohol[is_1986_in_world_alcohol,0] = "2014"
world_alcohol[is_wine_in_world_alcohol, 3] = "Grog"

## 7. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty,4] = "0"

## 8. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

## 9. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 10. Total Annual Alcohol Consumption ##

is_canada_1986 = (world_alcohol[:,2] == "Canada") & (world_alcohol[:,0] == '1986')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,4]
empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = "0"
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 11. Calculating Consumption for Each Country ##

totals = {}
is_year = world_alcohol[:,0] == "1989"
year = world_alcohol[is_year,:]

for row in countries:
    is_country = (year[:,2] == row)
    country_consumption = year[is_country, :]
    
    extract_alcohol = country_consumption[:,4]
    is_empty = extract_alcohol == ''
    extract_alcohol[is_empty] = '0'
    extract_alcohol = extract_alcohol.astype(float)
    totals[row] = extract_alcohol.sum()
print(totals)

## 12. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for name, val in totals.items():
    if val > highest_value:
        highest_key = name
        highest_value = val