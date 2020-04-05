## Road accident france


#### Description :
This is a personal project that I set up using new tools to improve my technical skills and tools that I already knew.
The data is about road accidents in France.

#### Goal:
There are two purposes. The first is to process the data in the same way as ETL and the second is to process the data in the same way as an ELT.

1. ETL strategy: It is to realize a step-by-step data processing with python. Each python script is equivalent to a specific task.
Once the python scripts were created, it was necessary to automate these tasks using Airflow.Finally, create a dashboard. 
This allowed me to use Airflow for the first time.

*\[ELT strategy in progress]* <br/> <!-- saut de ligne -->
2. ELT strategy: Here the data is retrieved by storing it directly in a datawarehouse to process the data directly inside.
It was necessary to automate these tasks using Airflow.Finally, create a dashboard.

#### ETL Pipeline:
1. Get data from website
2. Convert csv file to tsv file makes (it easier to manipulate them when it comes to large files.)
3. Data processing
4. Load data to Bigquery
5. Create Dashboard

#### ELT Pipeline:
1. Get data from website
2. Load data to Bigquery
3. Data processing
4. Create Dashboard

#### Data used:
For more information on the data click [here](https://www.data.gouv.fr/en/datasets/base-de-donnees-accidents-corporels-de-la-circulation/#_)

#### Tools:
- Airflow
- Data build tool (dbt) *\[in progress]*
- Python
- Google cloud platform (Bigquery: SQL query, API)
- Data visualization: Data studio, PowerBI, Tableau *\[in progress]* 
<span style="color:red">*\[in progress]*</span>
 
