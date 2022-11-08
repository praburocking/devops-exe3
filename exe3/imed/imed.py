import pika, sys, os
import time



HOST="exe3-rabitmq-1"
ROUTING_KEY1="compse140.o"
ROUTING_KEY2="compse140.i"
EXCHANGE='topic_msg'
time.sleep(50)
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')
    channel.queue_declare(queue=ROUTING_KEY1)
    channel.queue_declare(queue=ROUTING_KEY2)
    channel.queue_bind(exchange=EXCHANGE, queue=ROUTING_KEY2, routing_key=ROUTING_KEY2)

    def callback(ch, method, properties, body):
        channel.basic_publish(exchange=EXCHANGE,
                        routing_key=ROUTING_KEY2,
                        body=body)
        time.sleep(1)
        print("******** [x] Received %r" % body)

    channel.basic_consume(queue=ROUTING_KEY1, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)




