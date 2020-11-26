import pika

from config import RABBITMQ_HOST, RABBITMQ_PORT


def main():
    print("start work")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
    channel = connection.channel()

    channel.queue_declare(queue='task')

    def callback(ch, method, properties, body):
        print(f"New task {body}")

    channel.basic_consume(queue='task', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    main()
    print("end work")
