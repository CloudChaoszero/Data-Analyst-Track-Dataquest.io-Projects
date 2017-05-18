## 2. Introduction to the Data ##

import csv
file = open("nfl_suspensions_data.csv")
f = csv.reader(file)
nfl_suspensions_with_head = list(f)
nfl_suspensions = nfl_suspensions_with_head[1:]


def count_year(ls):
    years = {}
    for val in ls:
        row_year = val[5]
        if row_year in years:
            years[row_year] += 1
        else:
            years[row_year] = 1
    return(years)
years = count_year(nfl_suspensions)
print(years)

## 3. Unique Values ##

teams = [row[1] for row in nfl_suspensions]
unique_teams = set(teams)
print(unique_teams)

games = [row[2] for row in nfl_suspensions]
unique_games = set(games)
print(unique_games)

## 4. Suspension Class ##

class Suspension():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2] 
        self.year = row[5]
third_suspension = Suspension(nfl_suspensions[2])

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)
    
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
        