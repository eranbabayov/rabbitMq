from broker import Person, Message


def person1_callback_function(ch, method, properties, body):
    msg = Message.from_bytes_to_msg(body)

    print(f"got new msg from: {msg.sender_id} the msg is: {msg.message}")


if __name__ == '__main__':
    person1 = Person(person_name='eran1')
    person1.broker.subscribe(callback_function=person1_callback_function)
