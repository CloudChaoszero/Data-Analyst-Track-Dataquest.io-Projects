## 3. Condensing the Class Size Data Set ##

class_size = data["class_size"]
class_size = class_size[class_size["GRADE "] == '09-12']
class_size = class_size[class_size["PROGRAM TYPE"]=="GEN ED"]
print(class_size)

## 5. Computing Average Class Sizes ##

import numpy as np
import pandas as pd

class_size = class_size.groupby("DBN").agg(np.mean)
class_size.reset_index(inplace = True)

data["class_size"] = class_size
data["class_size"].head()

## 7. Condensing the Demographics Data Set ##

'''
demographics = data["demographics"]
demographics = demographics[demographics["schoolyear"] == 20112012]
print(demographics.head())
'''

data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]
print(data["demographics"].head())

## 9. Condensing the Graduation Data Set ##

data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]
print(data["graduation"].head())

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
da = data["ap_2010"]
for column in cols:
    da[column] = pd.to_numeric(da[column], errors="coerce")
print(data["ap_2010"])

## 12. Performing the Left Joins ##

combined = data["sat_results"]
combined = combined.merge(data["ap_2010"],how="left")
combined = combined.merge(data["graduation"],how="left")
print(combined.head())
print(combined.shape)

## 13. Performing the Inner Joins ##

demographics= data["demographics"]
class_size = data["class_size"]
survey = data["survey"]
hs_directory = data["hs_directory"]
combined = combined.merge(class_size, how = "inner")
combined = combined.merge(demographics, how = "inner")
combined = combined.merge(survey, how="inner")
combined = combined.merge(hs_directory, how = "inner")

print(combined.head())
print(combined.shape)

## 15. Filling in Missing Values ##

combined = combined#data["combined"]
mean_combined = combined.mean()
combined = combined.fillna(mean_combined)

combined = combined.fillna(0)
print(combined.head())

## 16. Adding a School District Column for Mapping ##

def get_district(DBN_string):
    return(DBN_string[0:2])
combined["school_dist"] = combined["DBN"].apply(get_district)
print(combined["school_dist"])