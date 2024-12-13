import pika

from broker import Person, Message
import time
if __name__ == '__main__':
    person2 = Person(person_name="eran")
    start = time.time()
    for i in range(1, 100000):
        msg = Message(sender_id=person2.name, recipient_id="eran1", message=f"hello from the other side message number {i}")

        person2.broker.out_channel.basic_publish(exchange="", routing_key="eran1", body=msg.msg_to_bytes(),
                                                 properties=pika.BasicProperties(delivery_mode=2))
        print(f"sent message number: {i} seconds")
    print(f"took: {time.time()- start}")