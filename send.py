import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# Realiza a conexão com com o servidor RabbitMQ e abre um canal de conexão com ele


channel.queue_declare(queue="hello")
# Declara a lista dos destinatários que receberam uma mensagem
# Essa lista é criada dentro do servidor RabbitMQ

channel.basic_publish(exchange='', routing_key='hello',body='Hello World!')
# Envia a mensagem para o servidor do rabbitMQ deacordor a lista especificada.
print(" [x] Sent 'Hello World!'")

connection.close()
# Encerra conexão com o servidor do RabbitMQ