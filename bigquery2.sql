CREATE VIEW `jlr-dl-cat-training.2022_temp_lippe_dm_bikesharing.top_2_region_by_capacity`
AS
SELECT region_id, SUM(capacity) as total_capacity
FROM `jlr-dl-cat-training.2022_temp_lippe_raw_bikesharing.stations`
WHERE region_id != ''
GROUP BY region_id
ORDER BY total_capacity desc
LIMIT 2;



-- to see the view have to run below command in bigquery
-- SELECT * FROM `jlr-dl-cat-training.2022_temp_lippe_dm_bikesharing.top_2_region_by_capacity` LIMIT 1000
