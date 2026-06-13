import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware

from backend.core.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        request_id = str(uuid.uuid4())

        start = time.time()


        response = await call_next(request)

        duration = round(
            (time.time() - start) * 1000,
            2
        )

        logger.info(
            "request completed",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": duration
            }
        )


        response.headers["X-Request-ID"] = request_id

        return response