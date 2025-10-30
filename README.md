# RabbitMQ

## O que é?
O RabbitMQ é um agente de mensagens: ele aceita e encaminha mensagens. Você pode pensar sobre isso como uma agência dos correios: quando você coloca o e-mail que deseja postar em um caixa postal, você pode ter certeza de que o carteiro acabará entregando o mail para o destinatário. Nesta analogia, o RabbitMQ é uma caixa de postagem, uma postagem escritório e um carteiro.

## Termos do RabbitMQ

- **Producing:** É quem é responsável por enviar mensagens. Ele cria uma mensagem e a encaminha para uma fila (queue) dentro do RabbitMQ, onde ela aguardará até ser processada.

- **queue_name:** Pense na fila como uma caixa de correio onde as mensagens são armazenadas até que alguém as leia. Assim como em um prédio podem existir várias caixas de correio uma para cada morador, no RabbitMQ podemos ter várias filas diferentes, cada uma com um nome (queue_name) e com mensagens específicas para determinados consumidores.

- **Consuming:** Programa que espera e recebe mensagens vindos dos protutores,ele fica “escutando” uma fila (queue_name) e, assim que uma nova mensagem chega, ele a lê e executa alguma ação com base no conteúdo da mensagem.