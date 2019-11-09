from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import os
import yaml
import uuid

def create_default_args():
    return {
            'owner': 'Airflow',
            'depends_on_past': False,
            'start_date': datetime(2015, 6, 1),
            'email': ['airflow@example.com'],
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5)
            }

def create_dag(dag_name, args, dag_schedule):
    return DAG(dag_name, default_args=args, schedule_interval=dag_schedule)

def create_task(task_name, dag):
    return BashOperator(
            task_id=task_name,
            bash_command='date',
            dag=dag)

def run_template():
    yaml_path = "/usr/local/airflow/config/"
    for yaml_file in os.listdir(yaml_path):
        with open(f"{yaml_path}{yaml_file}") as conf_file:
            conf_list = yaml.load(conf_file)
            args = create_default_args()
            dag = create_dag(conf_list["dag_name"], args, conf_list["dag_schedule"])
            with dag:
                task_list = []
                for task in conf_list["dag_tasks"]:
                    task_list.append(create_task(task["task_name"], dag))
                task_list[0] >> task_list[1]
                globals()[uuid.uuid1()] = dag

run_template()
