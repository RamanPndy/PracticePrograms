import threading
from collections import defaultdict, deque
from typing import List, Dict

'''
Components
Topic: Represents a queue of messages.
Producer: Can publish messages to a topic.
Consumer: Can subscribe to a topic to consume messages.
Broker: Manages topics, producers, and consumers.
'''

class Topic:
    def __init__(self, name: str):
        self.name = name
        self.messages = deque()
        self.lock = threading.Lock()

    def publish(self, message: str):
        with self.lock:
            self.messages.append(message)
            print(f"Message published to {self.name}: {message}")

    def consume(self):
        with self.lock:
            if self.messages:
                return self.messages.popleft()
            return None

class Broker:
    def __init__(self):
        self.topics: Dict[str, Topic] = {}
        self.consumers: Dict[str, List['Consumer']] = defaultdict(list)

    def create_topic(self, name: str):
        if name not in self.topics:
            self.topics[name] = Topic(name)
            print(f"Topic created: {name}")
        else:
            print(f"Topic already exists: {name}")

    def get_topic(self, name: str) -> Topic:
        return self.topics.get(name, None)

    def add_consumer(self, topic_name: str, consumer: 'Consumer'):
        if topic_name in self.topics:
            self.consumers[topic_name].append(consumer)
            print(f"Consumer added to topic {topic_name}")

class Producer:
    def __init__(self, broker: Broker):
        self.broker = broker

    def publish(self, topic_name: str, message: str):
        topic = self.broker.get_topic(topic_name)
        if topic:
            topic.publish(message)
            print(f"Producer published message to {topic_name}: {message}")
        else:
            print(f"Topic {topic_name} does not exist")

class Consumer:
    def __init__(self, broker: Broker, name: str):
        self.broker = broker
        self.name = name
        self.subscriptions = set()
        self.lock = threading.Lock()

    def subscribe(self, topic_name: str):
        topic = self.broker.get_topic(topic_name)
        if topic:
            self.broker.add_consumer(topic_name, self)
            self.subscriptions.add(topic_name)
            print(f"Consumer {self.name} subscribed to {topic_name}")
        else:
            print(f"Topic {topic_name} does not exist")

    def consume(self, topic_name: str):
        topic = self.broker.get_topic(topic_name)
        if topic and topic_name in self.subscriptions:
            message = topic.consume()
            if message:
                print(f"Consumer {self.name} consumed message from {topic_name}: {message}")
                return message
            else:
                print(f"No messages to consume from {topic_name}")
        else:
            print(f"Consumer {self.name} is not subscribed to {topic_name}")

# Example Usage

broker = Broker()
broker.create_topic("topic1")

producer1 = Producer(broker)
producer2 = Producer(broker)

consumer1 = Consumer(broker, "consumer1")
consumer2 = Consumer(broker, "consumer2")

consumer1.subscribe("topic1")
consumer2.subscribe("topic1")

producer1.publish("topic1", "message1")
producer2.publish("topic1", "message2")

consumer1.consume("topic1")
consumer2.consume("topic1")
consumer1.consume("topic1")
