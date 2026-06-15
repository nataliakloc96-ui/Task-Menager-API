# System Architecture


```text
                 USER
                  |
                  |
                  v

             FastAPI REST API
                  |
                  |
        ---------------------
        |                   |
        v                   v

 Authentication        Task Service
        |
        v

 Repository Layer

        |
        v

    PostgreSQL
    tasks_db

        |
        |
        v

 Apache Airflow Scheduler

        |
        |
        v

     ETL Pipeline

 Extract
    |
 Transform
    |
 Load

        |
        v

 Analytics Tables