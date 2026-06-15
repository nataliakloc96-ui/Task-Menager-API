from sqlalchemy import create_engine, text
import os


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/tasks_db"
)


def load_metrics(metrics):

    engine = create_engine(DATABASE_URL)

    query = text("""
        INSERT INTO task_metrics
        (
        metric_date,
        total_tasks,
        completed_tasks,
        todo_tasks,
        completion_rate
        )
        VALUES
        (
        :metric_date,
        :total_tasks,
        :completed_tasks,
        :todo_tasks,
        :completion_rate
        )
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            metrics
        )