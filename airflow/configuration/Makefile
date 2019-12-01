create-image:
	docker pull puckel/docker-airflow webserver

run-container:
	docker run -d -p 8080:8080 -v $(CURDIR)/../dags/tasks:/usr/local/airflow/tasks/ -v $(CURDIR)/../dags/dag_templates/:/usr/local/airflow/dags/ -v $(CURDIR)/../dags/config:/usr/local/airflow/config/ puckel/docker-airflow webserver
