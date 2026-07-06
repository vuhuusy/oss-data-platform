FROM apache/kyuubi:1.11.1 AS kyuubi

FROM apache/spark:3.5.8-iceberg

USER root

COPY --from=kyuubi /opt/kyuubi /opt/kyuubi

ENV KYUUBI_HOME=/opt/kyuubi
ENV SPARK_HOME=/opt/spark
ENV PATH=/opt/kyuubi/bin:/opt/spark/bin:${PATH}

# Kyuubi JVM cần load S3A trước khi Spark engine được launch.
# Copy S3A dependencies vào classpath /opt/kyuubi/jars/*.
RUN cp /opt/spark/jars/hadoop-aws-*.jar /opt/kyuubi/jars/ \
 && cp /opt/spark/jars/aws-java-sdk-bundle-*.jar /opt/kyuubi/jars/ \
 && cp /opt/spark/jars/spark-hadoop-cloud_2.12-*.jar /opt/kyuubi/jars/ \
 && mkdir -p \
      /opt/kyuubi/pid \
      /opt/kyuubi/logs \
      /opt/kyuubi/work \
      /opt/kyuubi/operation_logs \
 && chown -R 185:0 /opt/kyuubi \
 && chmod -R g=u /opt/kyuubi

ENTRYPOINT []
WORKDIR /opt/kyuubi
USER 185