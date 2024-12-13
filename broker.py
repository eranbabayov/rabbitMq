import pika
from pydantic import BaseModel

'''
why port 5672?
what is heartbeat ?
what is auto_ack?
what is exclusive?
'''


class Message(BaseModel):
    sender_id: str
    recipient_id: str
    message: str

    def msg_to_bytes(self):
        return self.model_dump_json().encode("utf-8")

    @staticmethod
    def from_bytes_to_msg(msg_bytes: bytes) -> 'Message':
        return Message.model_validate_json(msg_bytes)


class MessageBroker:
    def __init__(self, sender_id):
        self.sender_id: str = sender_id
        self.connection = self.get_connection()
        self.in_channel = self.connection.channel()
        self.out_channel = self.connection.channel()

    @staticmethod
    def get_connection():
        connection_parameters = pika.ConnectionParameters(host="localhost", port=5672, heartbeat=60)
        return pika.BlockingConnection(parameters=connection_parameters)

    def subscribe(self, callback_function):
        self.in_channel.queue_declare(queue=self.sender_id)
        self.in_channel.basic_consume(queue=self.sender_id, on_message_callback=callback_function, auto_ack=True)
        print("listening to queue")
        self.in_channel.start_consuming()


class Person:
    def __init__(self, person_name):
        self.name = person_name
        self.broker = MessageBroker(sender_id=self.name)
