from __future__ import annotations

from datetime import datetime
from pathlib import Path

from airflow.sdk import DAG
from cosmos import DbtTaskGroup, ExecutionConfig, ProfileConfig, ProjectConfig
from cosmos.constants import ExecutionMode


# With git-sync subPath: dags, this file is mounted at:
# /opt/airflow/dags/dbt_spark_cosmos.py
DAG_DIR = Path(__file__).resolve().parent

# Expected repository layout:
# dags/
# ├── dbt_spark_cosmos.py
# └── dbt/
#     └── lakehouse_demo/
#         ├── dbt_project.yml
#         ├── profiles.yml
#         └── models/
DBT_PROJECT_DIR = DAG_DIR / "dbt" / "lakehouse_demo"
DBT_PROFILES_YML = DBT_PROJECT_DIR / "profiles.yml"

project_config = ProjectConfig(
    dbt_project_path=str(DBT_PROJECT_DIR),
)

profile_config = ProfileConfig(
    profile_name="lakehouse_demo",
    target_name="prod",
    profiles_yml_filepath=str(DBT_PROFILES_YML),
)

execution_config = ExecutionConfig(
    execution_mode=ExecutionMode.WATCHER,
)

with DAG(
    dag_id="dbt_spark_cosmos",
    description="Run dbt Spark models through Kyuubi Thrift with LDAP authentication",
    start_date=datetime(2026, 7, 1),
    schedule=None,
    catchup=False,
    max_active_runs=1,
    tags=["dbt", "spark", "kyuubi", "ldap", "cosmos"],
) as dag:
    dbt_run = DbtTaskGroup(
        group_id="dbt_run",
        project_config=project_config,
        profile_config=profile_config,
        execution_config=execution_config,
    )