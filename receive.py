import pika
import os
import sys 

def callback(ch, method, properties, body):
    print(f" [x] Received :{body}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    # Como não temos garantias que a lista foi realmente declarada é recomendado que ela seja declarada também na parte do consumidor

    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
    # Consumidor das listas que retorna uma callback caso o servidor indique que existe alguma mensagem para ser lida
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    # Inicia o consumidor
    # O consumidor fica rodando esperando uma mensagem
    # e chamando a callback sempre que uma nova mensagem é enviada
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)