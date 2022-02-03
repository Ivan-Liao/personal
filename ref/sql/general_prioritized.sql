-- percentage makeup
-- data: test_address-book-database.sql

select City
	,count(*) as total
    ,round(count(*) * 100.0 / sum(count(*)) over (), 2) as percentage
from Persons
group by City