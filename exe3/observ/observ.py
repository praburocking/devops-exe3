
import pika
import sys
from datetime import datetime
import time


HOST="exe3-rabitmq-1"
ROUTING_KEY1="compse140.o"
ROUTING_KEY2="compse140.i"
EXCHANGE='topic_msg'
FILE_PATH="/usr/data/temp_file.txt"
temp_counter=1

def is_port_in_use(port: int) -> bool:
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((HOST, port)) == 0

# sleep util the rabit mq is active to accept the client.
while True:
	if not is_port_in_use(5672):
		print("observe pre-check going on-----------")
		time.sleep(2)
	else:
		print("observ started ........")
		break
time.sleep(5)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')

channel.queue_declare('#')





#clear the file before starting the consumer.
with open(FILE_PATH, 'w') as fp:
    pass



def callback(ch, method, properties, body):
    temp_file= open(FILE_PATH, "a",encoding='utf-8')	
    dt = datetime.now()
    #temp_counter=temp_counter+1	
    temp_str=str(dt)+" "+str(temp_counter)+" "+str(body)+" "+method.routing_key+"\n"
    temp_file.write(temp_str)
    print("********"+temp_str)    
    temp_file.close()

channel.basic_consume(
    queue='#', on_message_callback=callback, auto_ack=True)

channel.start_consuming()

