## 2. Use SELECT and LIMIT to Filter Results ##

SELECT College_jobs, Median, Unemployment_rate
FROM recent_grads
LIMIT 20

## 3. Use WHERE to Filter Results ##

SELECT Major
FROM recent_grads
WHERE Major_Category='Arts'
LIMIT 5

## 4. Express Criteria With Operators ##

SELECT Major, Total, Median, Unemployment_rate
FROM recent_grads
WHERE (Median<=50000 OR Unemployment_rate > .065) AND (Major_Category!='Engineering')
/*We select non-engineering ppl with median income less thatn 50000 and unemploy rate >X*/

## 5. Order Your Results ##

SELECT Major 
FROM recent_grads
WHERE Major_Category!='Engineering'
ORDER BY Major DESC
LIMIT 20