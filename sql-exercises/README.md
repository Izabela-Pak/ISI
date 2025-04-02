# EXCERCISE-01

> Write a SQL query to select the sex and body mass columns from the little_penguins in that order, sorted such that the largest body mass appears first.

``` 
SELECT sex,body_mass_g FROM little_penguins 
ORDER BY body_mass_g DESC
```

![excercise-01](./screenshots/excercise-01.png)

# EXCERCISE-02

> Write a SQL query to select the islands and species from rows 50 to 60 inclusive of the penguins table. Your result should have 11 rows.

``` 
SELECT  species, island FROM penguins
limit 11
OFFSET 49
```

![excercise-02](./screenshots/excercise-02.png)

