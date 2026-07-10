{{ config(materialized='view') }}
select cast(event_id as bigint) event_id, cast(user_id as bigint) user_id,
       trim(event_name) event_name, cast(event_ts as timestamp) event_ts,
       cast(event_value as decimal(18,2)) event_value,
       to_date(cast(event_ts as timestamp)) event_date
from {{ source('raw', 'raw_events') }}
