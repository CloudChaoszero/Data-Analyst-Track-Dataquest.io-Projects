## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
filename_beg = "schools/"
data = {}
print("schools/{0}".format("ads"))

for file in data_files:
    df_input = filename_beg+file
    dataframe = pd.read_csv(df_input)
    df_name = file.split(".")[0]
    
    data[df_name] = dataframe

    

## 5. Exploring the SAT Data ##

print(data["sat_results"].head())

## 6. Exploring the Remaining Data ##

for key in data:
    print(data[key][:5])

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv("schools/survey_all.txt", delimiter ="\t", encoding = "windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter = "\t", encoding ="windows-1252")
survey = pd.concat([all_survey,d75_survey], axis = 0)
print(survey.head())

## 9. Cleaning Up the Surveys ##

survey["DBN"] = survey["dbn"]
relevant_columns = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey = survey.loc[:,relevant_columns]
data["survey"] = survey
data["survey"].head()

## 11. Inserting DBN Fields ##

def to_padded_csd(col):
    csd = str(col)
    if len(csd) ==2:
        return(csd)
    else:
        return(csd.zfill(2))
    
data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"] 
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(to_padded_csd)

data["class_size"]["DBN"] =  data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"] 
data["class_size"]["DBN"].head()

## 12. Combining the SAT Scores ##

#Convert three different column in the sat_results data to integer data type
sat_scores = ["SAT Math Avg. Score","SAT Critical Reading Avg. Score","SAT Writing Avg. Score"]
sat = "sat_results"
for sat_type in sat_scores:
    data[sat][sat_type] = pd.to_numeric(data[sat][sat_type],errors = "coerce")
data[sat]["sat_score"] = (data[sat][sat_scores[0]]+data[sat][sat_scores[1]]+data[sat][sat_scores[2]]) 
data[sat]["sat_score"].head()

## 13. Parsing Geographic Coordinates for Schools ##

import re

def extract_coordinates(location_string):
    find_lat_long = re.findall("\(.+, .+\)", location_string)
    lat_long_coordinates_no_left_par = find_lat_long[0].replace("(","")
    lat_long_coordinates_no_right_par = lat_long_coordinates_no_left_par .replace(")","")
    lat_long_coordinates = lat_long_coordinates_no_right_par.split(",")
    return(lat_long_coordinates[0])

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(extract_coordinates)
print(data["hs_directory"])

## 14. Extracting the Longitude ##

import re
def extract_long(string):
    lat_long = re.findall("\(.+, .+\)", string)
    print(lat_long)
    long_no_par = lat_long[0].replace(")","")
    long = long_no_par.split(",")[1]
    return(long)

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(extract_long)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors = "coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors = "coerce")



#hs_directory