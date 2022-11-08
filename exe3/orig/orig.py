import pika
import time


HOST="exe3-rabitmq-1"
ROUTING_KEY1="compse140.o"
EXCHANGE='topic_msg'
ROUTING_KEY2="compse140.i"

time.sleep(50)
connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))

channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')
channel.queue_declare(queue=ROUTING_KEY1)
channel.queue_bind(exchange=EXCHANGE, queue=ROUTING_KEY1, routing_key=ROUTING_KEY1)
channel.queue_declare(queue='#')
channel.queue_bind(exchange=EXCHANGE, queue='#', routing_key='#')
N=3
for i in range(N):
    channel.basic_publish(exchange=EXCHANGE,
                        routing_key=ROUTING_KEY1,
                        body='MSG_'+str(i+1))
    print(" [x] Sent 'Hello World!'")
    time.sleep(3)

connection.close()


# import pika
# import sys

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()

# channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
# message = ' '.join(sys.argv[2:]) or 'Hello World!'
# channel.basic_publish(
#     exchange='topic_logs', routing_key=routing_key, body=message)
# print(" [x] Sent %r:%r" % (routing_key, message))
# connection.close()
