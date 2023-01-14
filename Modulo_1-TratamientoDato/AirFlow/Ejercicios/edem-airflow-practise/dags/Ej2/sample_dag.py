from airflow import DAG

from datetime import datetime

from airflow.operators.empty import EmptyOperator

from airflow.decorators import task


with DAG(
    dag_id="sample_dag",
    start_date=datetime(2022, 5, 28),
    schedule_interval=None,
    tags=["sample_dag"],
    default_args={'retries': 1},
) as dag:

    # Here the corresponding tasks

    start_task = EmptyOperator(
        task_id='start'
    )

    end_task = EmptyOperator(
        task_id='end'
    )

    true_task = EmptyOperator(task_id="true_task")
    false_task = EmptyOperator(task_id = "false_task")


    @task.branch(task_id="is_Saturday")
    def is_saturday():
        if datetime.today().isoweekday() == 6:
            return "true_task"
        return "false_task"

    # Here the DAG dependencies

    start_task >> is_saturday() >> [true_task, false_task] >> end_task
