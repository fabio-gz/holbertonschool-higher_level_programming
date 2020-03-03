-- list all cities in the database
-- one select statement
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id;
