select f.* from {{ ref('fct_events') }} f
left join {{ ref('dim_users') }} d on f.user_id=d.user_id
where d.user_id is null
