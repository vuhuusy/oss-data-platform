{{ config(materialized='table', file_format='iceberg', catalog='iceberg', schema='demo',
 tblproperties={'format-version':'2','write.format.default':'parquet'}) }}
select user_id, user_name, email, city, updated_at, current_timestamp() dbt_loaded_at
from {{ ref('stg_users') }}
