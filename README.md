# kafka Usage Example

## Docker / Docker Compose

### Start Kafka
```
docker-compose up
```

### Interactive 
Shell into kafka container
```
docker exec -it kafka_kafka_1
```
List topics
```
kafka-topics --bootstrap-server localhost:29092 --list
```

Create a topic
```
kafka-topics --bootstrap-server localhost:29092 --create --replication-factor 1 --partitions 1 --topic sample
```

Interact to see details - describe info on our test topic
```
kafka-topics --bootstrap-server localhost:29092 --describe --topic mytopic
```

# Test Data
Generate 1KB file with null character, then base64 for use in sending to kafka
```
fallocate -l 1KB 1kbfile
base64 ./1kbfile > 1kbfile.txt
```

