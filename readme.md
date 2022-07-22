Python microservices with gRPC

Following the tutorial : https://realpython.com/python-microservices-grpc/


### Docker commands

#### Build


```
docker build . -f recommendations/Dockerfile -t recommendations
docker build . -f marketplace/Dockerfile -t marketplace
```


#### Run Containers


```
docker network create microservices
docker run -p 127.0.0.1:50051:50051/tcp --network microservices  --name recommendations recommendations
docker run -p 127.0.0.1:5000:5000/tcp --network microservices -e RECOMMENDATIONS_HOST=recommendations marketplace
```


#### Run tests

```
docker-compose build
docker-compose up
docker-compose exec marketplace pytest marketplace_integration_test.py
```