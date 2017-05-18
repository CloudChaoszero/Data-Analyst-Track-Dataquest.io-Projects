## 1. Introduction ##

import sqlite3 as sql

conn = sql.connect('factbook.db') #Connect with the database
cursor = conn.cursor() #Store reference database to cursor(read only) structure
cursor.execute('SELECT COUNT (*) FROM facts;') #SQL command
facts_count = cursor.fetchall() #Save database reference to a local variable to modify
print(facts_count)

## 2. Counting the Number of Rows in SQL ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
cursor.execute('SELECT COUNT(birth_rate) FROM facts;')
birth_rate_count = cursor.fetchall()
print(birth_rate_count)

## 3. Finding a Column's Minimum and Maximum Values in SQL ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
cursor.execute('SELECT MIN(population_growth) FROM facts;')
min_population_growth = cursor.fetchall()
print(min_population_growth[0][0])

cursor.execute('SELECT MAX(death_rate) FROM facts;')
max_death_rate = cursor.fetchall()
print(max_death_rate[0][0] )

## 4. Calculating Sums and Averages in SQL ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
cursor.execute('SELECT SUM(area_land) FROM facts;')
total_land_area = cursor.fetchall()
print(total_land_area[0][0])

cursor.execute('SELECT AVG(area_water) FROM facts;')
avg_water_area = cursor.fetchall()
#avg_water_area = avg_water_area_t[0][0]
print(avg_water_area[0][0])

## 5. Combining Multiple Aggregation Functions ##

conn = sqlite3.connect("factbook.db")
cursor = conn.cursor()
facts_stats_tuple = cursor.execute('SELECT AVG(population), SUM(population), MAX(birth_rate) FROM facts;').fetchall()
facts_stats = facts_stats_tuple[0:3]
print(facts_stats)

## 6. Aggregating Values for a Subset of the Data ##

conn = sqlite3.connect("factbook.db")
population_growth_tuple = conn.execute('SELECT AVG(population_growth) FROM facts WHERE population >10000000').fetchall()
population_growth=population_growth_tuple[0][0]
print(population_growth)

## 7. Selecting Unique Rows ##

conn = sqlite3.connect("factbook.db")
unique_birth_rates = conn.execute('SELECT DISTINCT(birth_rate) FROM facts;').fetchall()
print(unique_birth_rates)

## 8. Aggregating Unique Values ##

conn = sqlite3.connect("factbook.db")
average_birth_rate = conn.execute('SELECT AVG(DISTINCT birth_rate) FROM facts WHERE population>20000000;').fetchall()
print(average_birth_rate[0][0])

sum_population = conn.execute('SELECT SUM(DISTINCT population) FROM facts WHERE area_land>1000000;').fetchall()
print(sum_population[0][0])


## 9. Performing Arithmetic in SQL ##

conn = sqlite3.connect("factbook.db")
population_growth_millions = conn.execute('SELECT population_growth/1000000.0 FROM facts;').fetchall()
print(population_growth_millions)

## 10. Performing Arithmetic Between Columns ##

conn = sqlite3.connect("factbook.db")
next_year_population = conn.execute("SELECT (1 + (population_growth/100)) * population FROM facts;").fetchall()
print(next_year_population)