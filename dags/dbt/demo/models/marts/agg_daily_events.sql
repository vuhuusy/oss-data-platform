{{ config(materialized='table', file_format='iceberg', catalog='iceberg', schema='demo',
 partition_by=['event_date']) }}
select event_date, city, event_name, count(*) event_count, count(distinct user_id) active_users,
       sum(event_value) total_event_value, current_timestamp() dbt_loaded_at
from {{ ref('fct_events') }}
group by event_date, city, event_name
