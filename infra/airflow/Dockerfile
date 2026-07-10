# ---- builder: has the compiler, nobody ships it ----
FROM apache/airflow:3.2.2-python3.12 AS builder
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ libsasl2-dev libssl-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*
USER airflow
WORKDIR /opt/airflow
COPY requirements.txt .
RUN pip install --no-cache-dir --user \
    "apache-airflow==3.2.2" \
    "astronomer-cosmos[dbt-core]" \
    "dbt-spark[PyHive]" \
    "psycopg2-binary" \

    -r requirements.txt
# ---- runtime: no compiler, no dev headers ----
FROM apache/airflow:slim-3.2.2-python3.12
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsasl2-modules \
    && rm -rf /var/lib/apt/lists/*
USER airflow
COPY --from=builder /home/airflow/.local /home/airflow/.local