## 2. Adding columns ##

ALTER TABLE facts
ADD leader text;

## 6. Creating a table with relations ##

CREATE TABLE factbook.states(
    id integer PRIMARY KEY,
    name text,
    area integer,
    country integer,
    FOREIGN KEY(country) REFERENCES facts(id)
);

## 7. Querying across foreign keys ##

SELECT * FROM landmarks
INNER JOIN facts
ON facts.id = landmarks.country;

## 9. Types of joins ##

SELECT * FROM landmarks
LEFT OUTER JOIN facts --If one row on landmarks table doesn't match facts table, facts table entries are null
ON facts.id = landmarks.country