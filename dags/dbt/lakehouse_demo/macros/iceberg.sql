{% macro iceberg_rewrite_data_files(schema_name, table_name) %}
call iceberg.system.rewrite_data_files(table => '{{ target.catalog }}.{{ schema_name }}.{{ table_name }}')
{% endmacro %}
{% macro iceberg_expire_snapshots(schema_name, table_name, older_than_days=7) %}
call iceberg.system.expire_snapshots(table => '{{ target.catalog }}.{{ schema_name }}.{{ table_name }}',
 older_than => timestampadd(day, -{{ older_than_days }}, current_timestamp()))
{% endmacro %}
