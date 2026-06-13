import logging
import sys
import json
from datetime import datetime, UTC


class JsonFormatter(logging.Formatter):

    def format(self, record):

        log = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
        }

        if hasattr(record, "request_id"):
            log["request_id"] = record.request_id

        if hasattr(record, "method"):
            log["method"] = record.method

        if hasattr(record, "path"):
            log["path"] = record.path

        if hasattr(record, "status_code"):
            log["status_code"] = record.status_code
        
        if hasattr(record, "duration_ms"):
            log["duration_ms"] = record.duration_ms
        
        return json.dumps(log)

logger = logging.getLogger("task-api")

logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)

handler.setFormatter(JsonFormatter())

logger.addHandler(handler)