import pika

from broker import Person, Message
if __name__ == '__main__':
    person2 = Person(person_name="producer")
    msg = Message(sender_id=person2.name, recipient_id="consumer", message=f"hello this is the producer")
    person2.broker.out_channel.basic_publish(exchange="", routing_key="consumer", body=msg.msg_to_bytes(),
                                             properties=pika.BasicProperties(delivery_mode=2))
    print("message sent")