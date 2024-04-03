Kafka and Redis Integration with Flask

This project demonstrates a simple implementation of a producer-consumer pattern using Kafka and Redis, integrated with a Flask application. The setup includes separate deployments for Redis, Kafka (alongside Zookeeper for Kafka management), a producer Flask app, and a consumer service. This system is designed to send messages from the producer to the consumer through Kafka, with the consumer then storing these messages in Redis.

Components

Redis: An in-memory data structure store, used as a database, cache, and message broker.
Kafka: A distributed streaming platform that lets you publish and subscribe to streams of records.
Zookeeper: A centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.
Flask Producer App: A simple Flask application to produce messages and send them to Kafka.
Consumer Service: A service that consumes messages from Kafka and stores them in Redis.

How It Works

Sending Messages:
The Flask app serves an endpoint /send to receive POST requests. Upon receiving a request, the Flask app publishes the message to a Kafka topic.

Consuming Messages:
The Consumer Service listens for new messages on the Kafka topic. Once a message is received, it is stored in Redis.

Setup Instructions
To deploy this system, you need to apply the Kubernetes configuration files provided. This guide assumes you have Kubernetes and kubectl configured and ready to use.

Deploy Kafka:
kubectl apply -f .\kafka-deployment.yaml

Deploy Redis:
kubectl apply -f .\redis-deployment.yaml

Deploy Producer and Consumer Applications:
kubectl apply -f .\producer-deployment.yaml
kubectl apply -f .\consumer-deployment.yaml

Verify the Deployments:
Use kubectl get pods and kubectl get services to verify that all components are up and running.

Usage
To send a message through the Flask app, use the /send endpoint with a POST request containing the message data. The consumer service will automatically consume any new messages and store them in Redis.

curl -X POST http://<flask-app-service-ip>:5000/send -H "Content-Type: application/json" -d '{"key": "messageKey", "value": "yourMessage"}'

Replace <flask-app-service-ip> with the actual IP address or hostname of the Flask app service. (Localhost if forwarding)
