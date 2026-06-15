from analytics.etl.extract import extract_tasks
from analytics.etl.transform import transform_tasks
from analytics.etl.load import load_metrics


def run_pipeline():

    print("Starting ETL pipeline")

    tasks = extract_tasks()

    print(
        f"Extracted {len(tasks)} tasks"
    )

    metrics = transform_tasks(tasks)

    print(
        "Metrics:",
        metrics
    )

    load_metrics(metrics)

    print("ETL finished successfully")

if __name__ == "__main__":
    run_pipeline()
    