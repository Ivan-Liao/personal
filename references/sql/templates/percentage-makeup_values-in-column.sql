select <column_name> 
	,count(*) as total
    ,round(count(*) * 100.0 / sum(count(*)) over (), 2) as percentage
from <table_name>
group by <column_name>