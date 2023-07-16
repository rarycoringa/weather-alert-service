# Weather Alert Service

## About this project

This project was built with the main porpuse to reach the goals from the Distributed Programming class, by improving knowledges using microservices and RabbitMQ as message broker.

On this service you will be able to create weather alerts from four differents types. These alerts will be sent to the type appropriated queue.

This service was built by:

- Rary Coringa
  - e-mail: rary.goncalves.123@ufrn.edu.br
  - github: https://github.com/rarycoringa
  - enrollment number: 20210081823
- Matheus Cortez
  - e-mail: 
  - github: https://github.com/matheus-cortez
  - enrollment number:

## Project resources

That's a service to send weather alerts for subscribers. People can use Publisher API to make new alerts and Subscriber Engine to receive new alerts.

### Publisher API

Using the endpoint `/alerts` you can do a `POST` with the content of the alert.

You can see below an example of body/content to pass to this endpoint:

```json
{
    "type": "YELLOW",
    "category": "SNOW_STORM",
    "title": "Snow storm on Revelstoke, BC",
    "description": "A snow storm was detected by our radars in Revelstoke, BC next monday. So, would be better for all Revelstoke's population keep safe in home at night.",
    "source_agency": "Canada Weather Metrics"
}
```

You can pass one of these types in `type` property:

- `"BLUE"`
- `"YELLOW"`
- `"ORANGE"`
- `"RED"`

You can pass one of these categories in `category` property:

- `"FOREST_FIRE"`
- `"SNOW_STORM"`
- `"THUNDERSTORM"`
- `"HURRICANE"`
- `"TORNADO"`

**A fully documentation are available in the endpoint `/redoc` of the service API, available on `http://localhost:8080`.**

### Subscriber Engine

And watching the Subscriber Engine logs you will be able to see when a new alert is received by the subscriber.

Here bellow we can se a log example received when the example of alert mentioned above is created:

```bash
was-subscriber  | INFO:root:Received message on queue _
was-subscriber  | method: <Basic.Deliver(['consumer_tag=ctag1.4b105ba7d39749bb9afe20811ca48a6c', 'delivery_tag=1', 'exchange=', 'redelivered=False', 'routing_key=red'])>
was-subscriber  | properties: <BasicProperties>
was-subscriber  | body: {"type": "RED", "category": "SNOW_STORM", "title": "Snow storm on Revelstoke, BC", "description": "A snow storm was detected by our radars in Revelstoke, BC next monday. So, would be better for all Revelstoke's population keep safe in home at night.", "source_agency": "Canada Weather Metrics"}
```

## How to run

To run this service you just need to make sure Docker and docker-compose are installed and working well on your machine and then run this command:

```bash
$ docker-compose up --build
```

It will create three containers:

1. was-publisher
   - A python FastAPI application responsible to receive alerts and send to message broker.
2. was-subscriber
   - A python application responsible to listen to alert queues and receive alert messages from message broker
3. was-rabbitmq
   - A RabbitMQ instance to work as message broker that is responsible to receive messages, enqueue in correct alert queues and make available to subscribers.

> A good point to be raised here is that when you up the containers, publisher and subscriber aren't connected by a network. The publisher has an own network with the rabbitmq and the subscriber has also an own network with the rabbitmq, so both can connect with rabbitmq using amqp protocol, but aren't able to make connections between publisher and subscribers. So this network architecture can make sure we are just using RabbitMQ to make communication between publisher and subscriber.

> Also, would be good keep in mind that the container orchestration was built to up was-publisher and was-subscriber just after was-rabbitmq is started and healthy running.