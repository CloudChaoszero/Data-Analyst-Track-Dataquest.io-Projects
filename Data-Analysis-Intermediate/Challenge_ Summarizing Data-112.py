## 3. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
recent_grads.head()
all_ages.head()

## 4. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()

#Use the total column to calculate the number of people who fall
#under each Major_category
aa_mcategory = all_ages['Major_category'].unique()
rg_mcategory = recent_grads['Major_category'].unique()

for item in rg_mcategory:
    major_df = recent_grads[recent_grads["Major_category"] == item]
    rg_cat_counts[item] =  major_df["Total"].sum()
    
for item in aa_mcategory:
    major_dfr = all_ages[all_ages["Major_category"] == item]
    aa_cat_counts[item] = major_dfr["Total"].sum()
print(rg_cat_counts)
print("----------------")
print(aa_cat_counts)

## 5. Low-Wage Job Rates ##

low_wage_percent = 0.0
low_wage_count = recent_grads["Low_wage_jobs"].sum()
total_count = recent_grads["Total"].sum()

low_wage_percent = low_wage_count / total_count
print(low_wage_percent)

## 6. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for major in majors:
    
    rg_df = recent_grads[recent_grads["Major"] == major]
    aa_df = all_ages[all_ages["Major"] == major]
    
    if rg_df.iloc[0]["Unemployment_rate"] < aa_df.iloc[0]["Unemployment_rate"]:
        rg_lower_count +=1
    
print(rg_lower_count)