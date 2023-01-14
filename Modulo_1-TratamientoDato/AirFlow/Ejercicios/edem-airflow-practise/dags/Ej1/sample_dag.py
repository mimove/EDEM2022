from airflow import DAG

from datetime import datetime

from airflow.operators.empty import EmptyOperator

from airflow.operators.bash import BashOperator

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

    print_hello_world = BashOperator(
        task_id='print_hello_world',
        bash_command='echo "\n\n\nHello MDA!\n\n\n"'
    )

    end_task = EmptyOperator(
        task_id='end'
    )



    # Here the DAG dependencies

    start_task >> print_hello_world
    print_hello_world >> end_task
