run-container:
	cd $(pwd)../dags/dag_templates/ && docker run -d -p 8080:8080 -v $(pwd)/../tasks:/usr/local/airflow/tasks/ -v $(pwd):/usr/local/airflow/dags/ -v $(pwd)/../config:/usr/local/airflow/config/ puckel/docker-airflow webserver
