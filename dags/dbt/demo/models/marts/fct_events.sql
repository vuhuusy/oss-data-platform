{{ config(materialized='incremental', incremental_strategy='merge', unique_key='event_id',
 file_format='iceberg', catalog='iceberg', schema='demo', partition_by=['event_date'],
 tblproperties={'format-version':'2','write.format.default':'parquet'}) }}
select event_id, user_id, user_name, city, event_name, event_ts, event_date, event_value,
       current_timestamp() dbt_loaded_at
from {{ ref('int_user_events') }}
{% if is_incremental() %}
where event_ts >= (select coalesce(max(event_ts), timestamp('1900-01-01 00:00:00')) from {{ this }})
{% endif %}
