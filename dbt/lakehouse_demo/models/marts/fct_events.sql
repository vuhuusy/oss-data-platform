select
    event_id,
    event_name,
    event_ts,
    user_id,
    date(event_ts) as event_date
from {{ ref('stg_events') }}