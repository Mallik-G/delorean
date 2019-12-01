FROM puckel/docker-airflow

COPY dags/tasks /usr/local/airflow/tasks/

COPY dags/dag_templates/ /usr/local/airflow/dags/

COPY dags/config/ /usr/local/airflow/config/

EXPOSE 8080

CMD ["webserver"]
