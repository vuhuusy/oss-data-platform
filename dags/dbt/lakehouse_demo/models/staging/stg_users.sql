{{ config(materialized='view') }}
select cast(user_id as bigint) user_id, trim(user_name) user_name, lower(trim(email)) email,
       trim(city) city, cast(updated_at as timestamp) updated_at
from {{ source('raw', 'raw_users') }}
