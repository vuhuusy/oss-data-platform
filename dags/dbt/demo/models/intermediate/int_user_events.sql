select e.event_id, e.user_id, u.user_name, u.email, u.city, e.event_name,
       e.event_ts, e.event_date, e.event_value
from {{ ref('stg_events') }} e
left join {{ ref('stg_users') }} u on e.user_id = u.user_id
