SELECT
name as region_name, total_trips
FROM `jlr-dl-cat-training.2022_temp_lippe_dwh_bikesharing.fact_region_gender_daily`fact
JOIN `jlr-dl-cat-training.2022_temp_lippe_dwh_bikesharing.dim_regions` dim
-- ON fact.region_id = dim.region_id
ON cast(fact.region_id as STRING) = cast(dim.region_id as STRING)
WHERE DATE(trip_date) = DATE('2018-01-01')
AND member_gender = 'Female'
ORDER BY total_trips desc
LIMIT 3;



