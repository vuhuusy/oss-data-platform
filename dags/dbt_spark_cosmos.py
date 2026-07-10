from __future__ import annotations

from datetime import datetime
from pathlib import Path

from airflow.sdk import DAG
from cosmos import DbtTaskGroup, ExecutionConfig, ProfileConfig, ProjectConfig
from cosmos.constants import ExecutionMode
from cosmos.profiles import SparkThriftProfileMapping


# git-sync mounts repository/dags at /opt/airflow/dags.
DAG_DIR = Path(__file__).resolve().parent
DBT_PROJECT_DIR = DAG_DIR / "dbt" / "lakehouse_demo"

project_config = ProjectConfig(
    dbt_project_path=str(DBT_PROJECT_DIR),
)

profile_config = ProfileConfig(
    profile_name="lakehouse_demo",
    target_name="dev",
    profile_mapping=SparkThriftProfileMapping(
        conn_id="kyuubi_thrift",
        profile_args={
            "schema": "default",
        },
    ),
)

execution_config = ExecutionConfig(
    execution_mode=ExecutionMode.LOCAL,
)

with DAG(
    dag_id="dbt_spark_cosmos",
    description="Run dbt Spark models through Kyuubi using Astronomer Cosmos",
    start_date=datetime(2026, 7, 1),
    schedule=None,
    catchup=False,
    max_active_runs=1,
    tags=["dbt", "spark", "kyuubi", "cosmos"],
) as dag:
    dbt_run = DbtTaskGroup(
        group_id="dbt_run",
        project_config=project_config,
        profile_config=profile_config,
        execution_config=execution_config,
    )