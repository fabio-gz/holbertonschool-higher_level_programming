-- subquery to list all the cities of California
-- in the hbtn_0d_usa database
SELECT cities.id, cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name = 'California' ORDER BY id ASC;
