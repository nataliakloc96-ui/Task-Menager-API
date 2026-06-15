CREATE TABLE IF NOT EXISTS task_metrics (
    id SERIAL PRIMARY KEY,
    metric_date DATE NOT NULL,
    total_tasks INTEGER NOT NULL,
    completed_tasks INTEGER NOT NULL,
    todo_tasks INTEGER NOT NULL,
    completion_rate FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);