# import pika, sys, os
# import time


# HOST="localhost"
# QUEUE1="#"
# QUEUE2="hello1"

# def main():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()

#     # channel.queue_declare(queue=QUEUE1)

#     def callback(ch, method, properties, body):
#         print(" [x] Received %r" % body)

#     channel.basic_consume(queue=QUEUE1, on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)


import pika
import sys
from datetime import datetime
import time

time.sleep(50)

HOST="exe3-rabitmq-1"
ROUTING_KEY1="compse140.o"
ROUTING_KEY2="compse140.i"
EXCHANGE='topic_msg'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

channel.queue_declare('#')


print(' [*] Waiting for logs. To exit press CTRL+C')
temp_counter=1
temp_file= open("/usr/data/temp_file.txt", "w")


def callback(ch, method, properties, body):
    dt = datetime.now()	
    temp_str=str(dt)+" "+str(temp_counter)+" "+str(body)+" "+method.routing_key+"\n"
    temp_file.write(temp_str)
    print("********"+temp_Str)
    
temp_file.close()

channel.basic_consume(
    queue='#', on_message_callback=callback, auto_ack=True)

channel.start_consuming()

