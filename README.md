# RabbitMQ Producer-Consumer Example

This repository demonstrates how to use **RabbitMQ** with Python to implement a simple producer-consumer system. The **Producer** sends messages to a queue, and the **Consumer** listens to that queue, processes the messages, and prints them to the console. This example uses the **pika** library to interact with RabbitMQ.

## Overview

- **Producer**: Sends a message to the `consumer` queue.
- **Consumer**: Listens to the `consumer` queue, processes the messages, and prints the message content.

The example includes two separate scripts:
- **Producer**: Sends a message to the `consumer` queue.
- **Consumer**: Listens to the `consumer` queue and processes incoming messages.

### Key Concepts

- **pika**: A Python library used to interact with RabbitMQ, allowing message publication and consumption.
- **Message Broker**: Manages the connection, channel setup, and message serialization/deserialization.

## Prerequisites

Before running the examples, make sure you have the following:

- **Python 3.x** (preferably Python 3.11 or later)
- **RabbitMQ server** running (local or remote)
- **Required Python libraries** (installable via `pip`)

### Required Libraries

- **pika**: A Python RabbitMQ client to send and receive messages.

To install the necessary dependencies, you can run:

```bash
pip install pika
