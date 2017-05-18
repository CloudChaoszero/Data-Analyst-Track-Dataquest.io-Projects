## 2. Working with dates in SQL ##

SELECT * FROM facts WHERE updated_at>"2015-10-30 16:00" AND updated_at<"2015-11-02 15:00"

## 3. Data types ##

PRAGMA table_info(facts)

## 4. Primary keys ##

SELECT * FROM facts ORDER BY id DESC LIMIT 1

## 5. Inserting data into a table ##

INSERT INTO facts
VALUES (262, "dq", "DataquestLand", 60000, 40000, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00");

## 6. Missing values ##

INSERT INTO facts
VALUES (263, "dq", "DataquestLand", NULL, NULL, 20000, 500000, 100, 50, 10, 20, "2016-02-25 12:00:00", "2016-02-25 12:00:00");

## 7. Updating rows ##

UPDATE facts
SET name="DataquestLand"
WHERE name="United States";

## 8. Deleting rows ##

DELETE FROM facts
WHERE name="Canada";