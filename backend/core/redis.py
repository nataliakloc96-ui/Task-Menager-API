import redis
import os


if os.getenv("TESTING") == "True":

    class FakePipeline:
        def incr(self, *args, **kwargs):
            return self
        
        def expire(self, *args, **kwargs):
            return self
        
        def execute(self):
            return True

    class FakeRedis:
        def get(self, *args, **kwargs):
            return None
        
        def setex(self, *args, **kwargs):
            return True
        
        def delete(self, *args, **kwargs):
            return 1
        
        def incr(self, *args, **kwargs):
            return 1
        
        def expire(self, *args, **kwargs):
            return True

        def pipeline(self):
            return FakePipeline()    
    
    
    redis_client = FakeRedis()

else:
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=6379,
        decode_responses=True
    )

