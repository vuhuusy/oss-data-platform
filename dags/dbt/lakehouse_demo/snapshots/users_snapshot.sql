{% snapshot users_snapshot %}
{{ config(target_catalog='iceberg', target_schema='snapshots', unique_key='user_id', file_format='iceberg',
 strategy='check', check_cols=['user_name','email','city','updated_at'], invalidate_hard_deletes=True) }}
select user_id, user_name, email, city, updated_at from {{ ref('stg_users') }}
{% endsnapshot %}
