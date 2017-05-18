## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
avg_col = conn.execute('SELECT AVG(population), AVG(population_growth), AVG(birth_rate), AVG(death_rate) FROM facts').fetchall()
pop_avg = avg_col[0][0]
pop_growth_avg = avg_col[0][1]
birth_rate_avg = avg_col[0][2]
death_rate_avg = avg_col[0][3]

## 2. Find Ranges ##

conn = sqlite3.connect("factbook.db")

averages = "select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate), avg(migration_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_growth_avg = avg_results[0][1]
birth_rate_avg = avg_results[0][2]
death_rate_avg = avg_results[0][3]
mig_rate_avg = avg_results[0][4]

mini = "select min(population), min(population_growth), min(birth_rate), min(death_rate), min(migration_rate) from facts;"
min_results = conn.execute(mini).fetchall()
pop_min = min_results[0][0]
pop_growth_min = min_results[0][1]
birth_rate_min = min_results[0][2]
death_rate_min = min_results[0][3]
mig_rate_min = min_results[0][4]

maxi = "select max(population), max(population_growth), max(birth_rate), max(death_rate), max(migration_rate) from facts;"
max_results = conn.execute(maxi).fetchall()
pop_max = max_results[0][0]
pop_growth_max = max_results[0][1]
birth_rate_max = max_results[0][2]
death_rate_max = max_results[0][3]
mig_rate_max = max_results[0][4]

## 3. Filter Values ##

onn = sqlite3.connect("factbook.db")
min_and_max = '''
select min(population), max(population), min(population_growth), max(population_growth),
min(birth_rate), max(birth_rate), min(death_rate), max(death_rate)
from facts where population > 0 and population < 2000000000;
'''
results = conn.execute(min_and_max).fetchall()
print(results)

# population column
pop_min = results[0][0]
pop_max = results[0][1]
# population_growth column
pop_growth_min = results[0][2]
pop_growth_max = results[0][3]
# birth_rate column
birth_rate_min = results[0][4]
birth_rate_max = results[0][5]
# death_rate column
death_rate_min = results[0][6]
death_rate_max = results[0][7]

## 4. Predict Future Population Growth ##

import sqlite3
conn = sqlite3.connect("factbook.db")
projected_population = conn.execute('SELECT ROUND(population*(1+population_growth/100),0) FROM facts WHERE population < 7000000000 AND population > 0 AND population IS NOT NULL AND population_growth IS NOT NULL').fetchall()

## 5. Explore Projected Population ##

import sqlite3
conn = sqlite3.connect("factbook.db")
pop_proj = conn.execute('SELECT ROUND(MAX(population*(1+population_growth/100)),0),ROUND(MIN(population*(1+population_growth/100)),0),ROUND(AVG(population*(1+population_growth/100)),0) FROM facts WHERE population <7000000000 AND population >0 AND population IS NOT NULL AND population_growth IS NOT NULL;').fetchall()
pop_proj_min = pop_proj[0][1]
pop_proj_max = pop_proj[0][0]
pop_proj_avg = pop_proj[0][2]

