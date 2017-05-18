## 2. Calling Functions ##

# Define the add function
add <- function(a, b){
    return(a + b)
}

# subtract <- function(a,b){
# return(a-b)
#
#}


# Call the add function with the arguments 1 and 2
print(add(1, 2))
d <- add(5,10)

## 3. Defining a Function ##

subtract <- function(a,b){
    return(a-b)

}
d <- subtract(50,10)

## 4. Reading in the Data ##

readfile <- function(file){
    return(read.csv(file))
}
ufos <- readfile("ufo_sightings.csv")

## 5. Previewing the Dataframe with head and tail ##

# Print the first five rows in the dataframe
print(head(ufos, 5))
print(tail(ufos,5))

## 6. Calculating UFO Sightings Per Year ##

str(ufos)
print(ufos)

## 7. Converting a Vector's Type ##

dateReported <- as.character(ufos$date.reported)
dateSighted <- as.character(ufos$date.sighted)

## 8. Extracting Part of a Character with the Substring Function ##

# This extracts "2004" from our string
date <- "20040415"
print(substr(date, 1, 4))

# This extracts the year from each string in the vector
dates <- c("20040415", "20080515")
print(substr(dates, 1, 4))

years <- substr(dateSighted,1,4)

## 9. Generating a Table of Sightings Per Year ##

# Create a small vector containing a few years
selectedYears <- c("2004", "2002", "1992", "2005", "2006", "2005", "2004")

# Create and print a table
print(table(selectedYears))
print(table(years))

## 10. Working with Dates ##

dateSighted <- as.character(ufos$date.sighted)
dateSighted <- as.Date(dateSighted, "%Y%m%d")

dateReported <- as.character(ufos$date.reported)
dateReported <- as.Date(dateReported, "%Y%m%d")

## 11. Subtracting Vectors ##

delay <- dateReported - dateSighted

## 12. Making a Table of Reporting Delays ##

print(table(delay))

## 13. Cleaning and Combining the Data ##

dates <- data.frame(dateReported, dateSighted)
print(dates)

## 14. Introduction to Boolean Vectors ##

a <- c(1,2,3)
b <- c(5,2,5)

print(a > b)

positiveDelays <- delay > 0

## 15. Filtering With Boolean Vectors ##

filter <- c(FALSE, FALSE, TRUE, TRUE)
bestIceCreamFlavors <- data.frame(c("Peanut Butter Oreo", "Cookie Dough", "Mint Chocolate Chip", "Peanut Butter Cup"))
twoFlavors <- bestIceCreamFlavors[filter,]
print(twoFlavors)

positiveDates <- dates[positiveDelays,]

## 16. Removing Null Values ##

cleanDates <- na.omit(positiveDates)

## 17. Remaking our Table ##

delay <- cleanDates[,"dateReported"] - cleanDates[,"dateSighted"] 
print(table(delay))