from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import os

app = Flask(__name__)

kafka_service_name = os.getenv('KAFKA_SERVICE_NAME', 'kafka-service')
kafka_port = os.getenv('KAFKA_SERVICE_PORT', '9092')
kafka_servers = f"{kafka_service_name}:{kafka_port}"

producer = KafkaProducer(bootstrap_servers=kafka_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.json 
        key = data['key'] if 'key' in data else None
        value = data['value']

        if key:
            producer.send('topic-data', key=key.encode('utf-8'), value=value)
        else:
            producer.send('topic-data', value=value)
        
        producer.flush()

        return jsonify({"message": "Mensaje enviado a Kafka con éxito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)