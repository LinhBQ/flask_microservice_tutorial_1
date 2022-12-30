import pika

params = pika.URLParameters('amqps://qoutfarr:s2fNjLfPX53r2-qqhRSBcudmvWtXvN9h@armadillo.rmq.cloudamqp.com/qoutfarr')

conection = pika.BlockingConnection(params)

channel = conection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Reveived in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('start consuming')

channel.start_consuming()

channel.close()