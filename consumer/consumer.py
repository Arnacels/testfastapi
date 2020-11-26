import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task')

    def callback(ch, method, properties, body):
        print(f"New task {body}")

    channel.basic_consume(queue='task', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    main()
