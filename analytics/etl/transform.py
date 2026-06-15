from datetime import date


def transform_tasks(df):

    total = len(df)

    completed = len(
        df[df["status"] == "done"]
    )

    todo = len(
        df[df["status"] == "todo"]
    )

    completion_rate = (
        completed / total * 100
        if total > 0
        else 0
    )

    return {
        "metric_date": date.today(),
        "total_tasks": total,
        "completed_tasks": completed,
        "todo_tasks": todo,
        "completion_rate": completion_rate
    }