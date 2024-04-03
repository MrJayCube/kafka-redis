from kafka import KafkaConsumer
import redis
import json
import os
import logging

logging.basicConfig(level=logging.INFO)

kafka_service_name = os.getenv('KAFKA_SERVICE_NAME', 'kafka-service')
kafka_port = os.getenv('KAFKA_SERVICE_PORT', '9092')
kafka_servers = f"{kafka_service_name}:{kafka_port}"

consumer = KafkaConsumer('topic-data',
                         bootstrap_servers=kafka_servers,
                         auto_offset_reset='earliest',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

redis_service_name = os.getenv('REDIS_SERVICE_NAME', 'redis-service')
redis_port = os.getenv('REDIS_SERVICE_PORT', '6379')
redis_host = f"{redis_service_name}"

r = redis.Redis(host=redis_host, port=redis_port, db=0)

for message in consumer:
    key = message.key
    value = message.value
    r.set(key, value)
    logging.info(f"Stored in Redis: {key} - {value}")
