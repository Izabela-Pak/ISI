# EXCERCISE-01

> Write a SQL query to select the sex and body mass columns from the little_penguins in that order, sorted such that the largest body mass appears first.

``` 
SELECT sex,body_mass_g FROM little_penguins 
ORDER BY body_mass_g DESC
```

![exercise-01](./screenshots/exercise-01.png)

# EXCERCISE-02

> Write a SQL query to select the islands and species from rows 50 to 60 inclusive of the penguins table. Your result should have 11 rows.

``` 
SELECT  species, island FROM penguins
limit 11
OFFSET 49
```

![exercise-02](./screenshots/exercise-02.png)

# EXCERCISE-03

> Modify your query to select distinct combinations of island and species from the same rows and compare the result to what you got in part 1.

``` 
SELECT DISTINCT species, island FROM (
SELECT species, island FROM penguins
limit 11
OFFSET 49
)

```

![exercise-03](./screenshots/exercise-03.png)

# EXCERCISE-04

> Write a query to select the body masses from penguins that are less than 3000.0 grams.

``` 
SELECT body_mass_g FROM penguins 
WHERE body_mass_g < 3000


```

![exercise-04](./screenshots/exercise-04.png)

# EXCERCISE-05

> Write another query to select the species and sex of penguins that weight less than 3000.0 grams. This shows that the columns displayed and those used in filtering are independent of each other.

``` 
SELECT species, sex FROM penguins 
WHERE body_mass_g < 3000

```

![exercise-05](./screenshots/exercise-05.png)


# EXCERCISE-06
> Use the not operator to select penguins that are not Gentoos.

```
SELECT * FROM penguins 
WHERE species != "Gentoo"
```

![exercise-06](./screenshots/exercise-06.png)

# EXCERCISE-07
> SQL's or is an inclusive or: it succeeds if either or both conditions are true. SQL does not provide a specific operator for exclusive or, which is true if either but not both conditions are true, but the same effect can be achieved using and, or, and not. Write a query to select penguins that are female or on Torgersen Island but not both.

```
SELECT * FROM penguins 
WHERE (island="Torgersen" AND sex !="FEMALE") OR (island!="Torgersen" AND sex="FEMALE")
```

![exercise-07](./screenshots/exercise-07.png)

# EXCERCISE-08
> Write a single query that calculates and returns:
> A column called what_where that has the species and island of each penguin separated by a single space.
> A column called bill_ratio that has the ratio of bill length to bill depth.

```
SELECT  
 species || ' ' || island
,bill_length_mm / bill_depth_mm as bill_ratio
FROM penguins
```

![exercise-08](./screenshots/exercise-08.png)


# EXCERCISE-09
> Use SQLite's .nullvalue command to change the printed representation of null to the string null and then re-run the previous query. When will displaying null as null be easier to understand? When might it be misleading?

```
.nullvalue null
SELECT species || ' ' || island ,bill_length_mm / bill_depth_mm as bill_ratio FROM penguins;
```

![exercise-09](./screenshots/exercise-09.png)

# EXCERCISE-10
> Write a query to find penguins whose body mass is known but whose sex is not.

```
SELECT * FROM penguins
WHERE body_mass_g is NOT NULL AND sex is NULL
```

![exercise-10](./screenshots/exercise-10.png)

# EXCERCISE-11
> Write another query to find penguins whose sex is known but whose body mass is not.

```
SELECT * FROM penguins
WHERE body_mass_g is NULL AND sex is Not NULL
```

![exercise-11](./screenshots/exercise-11.png)

# EXCERCISE-12
> What is the average body mass of penguins that weight more than 3000.0 grams?

```
SELECT AVG(body_mass_g) as average_body_mass
FROM (SELECT body_mass_g FROM penguins WHERE body_mass_g > 3000)
```

![exercise-12](./screenshots/exercise-12.png)

# EXCERCISE-13
> How many different body masses are in the penguins dataset?

```
SELECT COUNT(body_mass_g)
FROM(SELECT DISTINCT body_mass_g FROM penguins WHERE body_mass_g )
```

![exercise-13](./screenshots/exercise-13.png)

# EXCERCISE-14
> Write a query that shows each distinct body mass in the penguin dataset and the number of penguins that weigh that much.

```
SELECT DISTINCT COUNT(body_mass_g), body_mass_g
FROM penguins
GROUP BY body_mass_g
```

![exercise-14](./screenshots/exercise-14.png)

# EXCERCISE-15
> Write a query that uses filter to calculate the average body masses of heavy penguins (those over 4500 grams) and light penguins (those under 3500 grams) simultaneously. Is it possible to do this using where instead of filter?

```
select
    round(
        avg(body_mass_g) filter (where body_mass_g > 4500.0),
        1
    ) as heavy_penguins,
	round(
        avg(body_mass_g) filter (where body_mass_g < 3500.0),
        1
    ) as light_penguins
from penguins
```

![exercise-15](./screenshots/exercise-15.png)

# EXCERCISE-16
> Using an in-memory database, define a table called notes with two text columns author and note and then add three or four rows. Use a query to check that the notes have been stored and that you can (for example) select by author name.

```
sqlite3 :memory:
sqlite> create table notes( author text not null, note text not null);
sqlite> insert into notes values ('Staszek', 'notatka 1'), ('Dominik', 'notatka 2'), ('Grażyna', 'notatka 3'), ('Maja', 'notatka 4');
sqlite> SELECT * FROM notes;
sqlite> SELECT note FROM notes WHERE author='Maja';
```

![exercise-16](./screenshots/exercise-16.png)

# EXCERCISE-17
> What happens if you try to delete rows that don't exist (e.g., all entries in work that refer to juna)?

```
DELETE FROM notes WHERE author='Grześ';
```

![exercise-17](./screenshots/exercise-17.png)

# EXCERCISE-18
> Re-create the notes table in an in-memory database and then use SQLite's .output and .dump commands to save the database to a file called notes.sql. Inspect the contents of this file: how has your data been stored?

```
sqlite> .output notes.sql
sqlite> .dump
sqlite> .output stdout
```

![exercise-18](./screenshots/exercise-18.png)

# EXCERCISE-19
> Start a fresh SQLite session and load notes.sql using the .read command. Inspect the database using .schema and select *: is everything as you expected?

```
sqlite> .read notes.sql
sqlite> SELECT * FROM notes
```

![exercise-19](./screenshots/exercise-19.png)

# EXCERCISE-20
> Re-create the notes table in an in-memory database once again and use SQLite's .backup command to save it to a file called notes.db. Inspect this file using od -c notes.db or a text editor that can handle binary data: how has your data been stored?

```
sqlite> .backup notes.db
```

![exercise-20](./screenshots/exercise-20.png)

# EXCERCISE-21
> Start a fresh SQLite session and load notes.db using the .restore command. Inspect the database using .schema and select *: is everything as you expected?

```
.restore notes.db
```

![exercise-21](./screenshots/exercise-21.png)

# EXCERCISE-22
> Re-run the query shown above using where job = name instead of the full table.name notation. Is the shortened form easier or harder to read and more or less likely to cause errors?

```
select *
from work, job
where work.job = job.name
```

![exercise-22](./screenshots/exercise-22.png)

# EXCERCISE-23
> Find the least time each person spent on any job. Your output should show that mik and po each spent 0.5 hours on some job. Can you find a way to show the name of the job as well using the SQL you have seen so far?

```
select work.person, MIN(job.billable), job.name
from work join job on work.job = job.name
group by work.person
```

![exercise-23](./screenshots/exercise-23.png)
