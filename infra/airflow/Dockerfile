# ---------- Builder ----------
FROM apache/airflow:slim-3.2.2-python3.12 AS builder

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libsasl2-dev \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

USER airflow
WORKDIR /opt/airflow

COPY requirements.txt .

RUN pip install --no-cache-dir --user \
    "astronomer-cosmos[dbt-core]" \
    "dbt-spark[PyHive]" \
    "psycopg2-binary" \
    "asyncpg" \
    -r requirements.txt

# ---------- Runtime ----------
FROM apache/airflow:slim-3.2.2-python3.12

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    libsasl2-modules \
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY --from=builder /home/airflow/.local /home/airflow/.local

ENV PATH="/home/airflow/.local/bin:${PATH}"