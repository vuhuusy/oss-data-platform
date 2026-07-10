from datetime import datetime

from airflow import DAG
from cosmos import DbtTaskGroup, ExecutionConfig, ProfileConfig, ProjectConfig
from cosmos.constants import ExecutionMode

DBT_PROJECT_PATH = "/opt/airflow/dbt/lakehouse_demo"
DBT_PROFILES_PATH = "/opt/airflow/dbt/lakehouse_demo"

with DAG(
    dag_id="dbt_spark_cosmos_demo",
    description="Run dbt-spark models through Kyuubi using Cosmos",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    render_template_as_native_obj=True,
    tags=["dbt", "spark", "kyuubi", "cosmos"],
) as dag:
    dbt_spark_models = DbtTaskGroup(
        group_id="dbt_spark_models",
        project_config=ProjectConfig(
            dbt_project_path=DBT_PROJECT_PATH,
        ),
        profile_config=ProfileConfig(
            profiles_yml_filepath=f"{DBT_PROFILES_PATH}/profiles.yml",
            profile_name="lakehouse_demo",
            target_name="dev",
        ),
        execution_config=ExecutionConfig(
            execution_mode=ExecutionMode.LOCAL,
            dbt_executable_path="/home/airflow/.local/bin/dbt",
        ),
        operator_args={
            "install_deps": False,
        },
    )