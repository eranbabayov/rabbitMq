import pika

from broker import Person, Message
if __name__ == '__main__':
    person2 = Person(person_name="eran")
    msg = Message(sender_id=person2.name, recipient_id="eran1", message=f"hello from the other side message number")
    person2.broker.out_channel.basic_publish(exchange="", routing_key="eran1", body=msg.msg_to_bytes(),
                                             properties=pika.BasicProperties(delivery_mode=2))
    print("message sent")