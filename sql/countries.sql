-- What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order.

SELECT countries.name,languages.language,languages.percentage
FROM countries
JOIN languages ON countries.id=languages.country_id
ORDER BY percentage DESC;

SELECT countries.name,count(cities.id)
FROM countries
join cities on countries.id=cities.country_id
group by countries.id
order by count(cities.id) desc;

select * from countries;


select cities.name,cities.population,countries.name
from cities
join countries on countries.id=cities.country_id
where cities.population>500000 and countries.name='mexico'
order by population desc;

select languages.language,languages.percentage,countries.name as country_name
from languages
join countries on countries.id=languages.country_id
where percentage > 89
order by percentage desc;

select countries.name,countries.surface_area
from countries
where surface_area<501 and population >100000;

select countries.name
from countries 
where capital >200 and life_expectancy>75 and government_form='constitutional monarchy';

select countries.name,cities.name,cities.district,cities.population
from countries
join cities on countries.id=cities.country_id
where countries.name='argentina' and cities.district='buenos aires' and cities.population > 500000;

select countries.region,count(countries.id)
from countries
group by region
order by count(countries.id) desc;


