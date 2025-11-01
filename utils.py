import json
import logging

import redis
from typing import Dict, Any

logger = logging.getLogger(__name__)

def get_redis_connection(redis_config: Dict[str, Any]) -> redis.Redis:
    """Creates a Redis connection with the given config."""
    try:
        return redis.Redis(
            host=redis_config['host'],
            port=redis_config['port'],
            db=redis_config['db']
        )
    except KeyError as e:
        logger.error(f"Missing Redis config key: {e}")
        raise