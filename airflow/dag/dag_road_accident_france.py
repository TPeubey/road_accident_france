from datetime import timedelta
from datetime import datetime
import airflow
# @import the variable from database (webserver UI)
from airflow.models import Variable
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 4, 1),
    # 'end_date': datetime(2018, 12, 30),
    'depends_on_past': False,
    'email': ['beleth71@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    # If a tasks fail, retry it once after waiting
    # at least 10 seconds
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}

dag = DAG(
    'road_accident_france',
    default_args=default_args,
    description='Road accident DAG in France',
    # Continue to run DAG once per day
    schedule_interval=timedelta(minutes=1)
)

## 3 DB connections called
#var1 = Variable.get("raf_python_script_path")
var1 = """{{ var.value.raf_python_script_path }}"""


# t1: get all file from website to local folder
t1 = BashOperator(
    task_id='1_get_csv_file',
    bash_command="python " + var1 + "from_website_to_csv.py",
    dag=dag
)

# t2: This bash operator will run the python script to convert the csv to tsv
t2 = BashOperator(
    task_id='2_csv2tsv',
    bash_command="python " + var1 + "convert2tsv.py",
    dag=dag
)

# t3: This bash operator will run python script to process the data
t3 = BashOperator(
    task_id='3_data_processing',
    bash_command="python " + var1 + "Main.py",
    dag=dag
)

# t4: This bash operator will run python script to load data into Bigquery
t4 = BashOperator(
    task_id='4_tsv_to_bigquery',
    bash_command="python " + var1 + "load2bigquery.py",
    dag=dag
)

t1 >> t2 >> t3 >> t4
