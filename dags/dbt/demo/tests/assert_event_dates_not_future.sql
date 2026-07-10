select * from {{ ref('fct_events') }} where event_date > current_date()
