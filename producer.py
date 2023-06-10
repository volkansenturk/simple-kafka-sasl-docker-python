from confluent_kafka import Producer
import socket


KAFKA_PRODUCER_CONFIGURATION = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': socket.gethostname(),
    'security.protocol' : 'SASL_PLAINTEXT',
    'sasl.username': 'admin',
    'sasl.password': 'admin-secret',
    'sasl.mechanism':'PLAIN'
}

producer = Producer(KAFKA_PRODUCER_CONFIGURATION)

# Write hello world to test topic
producer.produce("test", '{"name":"DGR"}')
producer.flush()