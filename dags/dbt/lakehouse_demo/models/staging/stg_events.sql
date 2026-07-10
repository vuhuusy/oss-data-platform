select
    cast(id as bigint) as event_id,
    cast(event_name as string) as event_name,
    cast(event_ts as timestamp) as event_ts,
    cast(user_id as bigint) as user_id
from {{ source('raw', 'events') }}