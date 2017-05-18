## 2. Returning Multiple Conditions With AND ##

SELECT Major,ShareWomen,Employed FROM recent_grads WHERE ShareWomen>0.5 AND Employed>10000
LIMIT 10

## 3. Returning One of Several Conditions With OR ##

SELECT Major, Median, Unemployed FROM recent_grads WHERE Median>10000 OR Unemployed<=1000
LIMIT 20

## 4. Grouping Operators With Parentheses ##

SELECT Major, Major_category,ShareWomen,Unemployment_rate FROM recent_grads WHERE (Major_category='Engineering') AND (ShareWomen>0.5 OR Unemployment_rate<.051)

## 5. Practice Grouping Operators ##

SELECT Major,Major_Category,Employed,Unemployment_rate FROM recent_grads WHERE (Major_Category = 'Business' OR Major_Category='Arts' OR Major_Category='Health') AND (Employed>=20000 OR Unemployment_rate<0.051)

## 6. Order Results With ORDER BY ##

SELECT Major FROM recent_grads
ORDER BY Major DESC
LIMIT 10

## 7. Order Results Based on Multiple Columns ##

SELECT Major_category, Median, Major FROM recent_grads ORDER BY Major ASC, Median DESC
LIMIT 20