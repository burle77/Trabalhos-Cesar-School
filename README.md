Documentação do Sistema de Rastreamento de Despesas Pessoais
FP B // Professores: Carol Melo // Mateus Valgueiro
Grupo: 
André Burle
Artur Melo
Caio Fonseca
Paulo Portella
Rastreamento de Despesas Pessoais
Este código implementa um programa simples de rastreamento de despesas pessoais. Ele permite ao usuário adicionar, listar, deletar e filtrar transações financeiras, além de gerar extratos por categoria e converter valores para uma moeda específica com base em taxas de câmbio fornecidas pelo usuário.
Funcionalidades
1. Adicionar transação
Permite ao usuário adicionar uma nova transação fornecendo o nome, categoria e valor da transação. Os dados são armazenados em um arquivo CSV chamado "transacoes.csv".
2. Listar transações
Exibe uma lista de todas as transações registradas até o momento, mostrando o nome, categoria e valor de cada uma.
3. Deletar transação
Permite ao usuário deletar uma transação específica fornecendo o nome da transação. A transação é removida do arquivo de transações.
4. Filtrar transações por categoria
Permite ao usuário filtrar as transações por categoria, exibindo apenas as transações que pertencem à categoria especificada.
5. Mostrar extrato por categoria
Calcula e exibe o valor total gasto em cada categoria com base nas transações registradas até o momento.
6. Mostrar extrato bancário por categoria em outra moeda
Calcula e exibe o valor total gasto em cada categoria, convertendo o valor para uma moeda específica com base nas taxas de câmbio fornecidas pelo usuário.
7. Adicionar taxa de câmbio
Permite ao usuário adicionar uma taxa de câmbio para uma moeda específica. Essas taxas de câmbio são usadas na conversão de valores na opção anterior.
0. Sair do programa
Encerra a execução do programa.
Estrutura do código
O código é organizado em uma série de funções que implementam cada uma das funcionalidades mencionadas acima. Além disso, há uma função menu() que exibe um menu de opções para o usuário e chama a função correspondente com base na escolha feita.
O arquivo de transações é lido e gravado utilizando a biblioteca open() do Python, e os dados são armazenados como uma lista de listas, onde cada lista interna representa uma transação com nome, categoria e valor.
O código também faz uso da biblioteca os para limpar a tela do console entre as operações. A função limpar_tela() verifica o sistema operacional em uso e utiliza os comandos apropriados para limpar a tela.
Execução do programa
O programa é iniciado chamando a função menu() no bloco final do código. Isso faz com que o menu principal seja exibido e permite ao usuário interagir com as diferentes funcionalidades do programa.
O programa continuará em execução até que o usuário escolha a opção "0" para sair do programa. Caso contrário, o menu será exibido novamente após a execução de cada operação, garantindo que o usuário possa selecionar uma nova opção ou encerrar o programa quando desejar.


Manual do Usuário
 - Sistema de Rastreamento de Despesas Pessoais
FP B // Professores: Carol Melo // Mateus Valgueiro
Grupo: 
André Burle
Artur Melo
Caio Fonseca
Paulo Portella

Bem-vindo ao Sistema de Rastreamento de Despesas Pessoais! Este sistema permite que você gerencie suas transações financeiras, categorize-as e obtenha um extrato das despesas por categoria. Você também pode adicionar taxas de câmbio para converter o extrato para outras moedas.
Aqui está um guia de como utilizar o sistema:
1.	Adicionar Transação:
●	Digite o nome da transação.
●	Digite a categoria da transação.
●	Digite o valor da transação.
●	A transação será adicionada ao sistema.
2.	Listar Transações:
●	Exibe todas as transações registradas no sistema.
●	O nome, a categoria e o valor de cada transação serão mostrados.
3.	Deletar Transação:
●	Digite o nome da transação que deseja deletar.
●	A transação será removida do sistema.
4.	Filtrar Transações por Categoria:
●	Digite a categoria desejada para filtrar as transações.
●	Todas as transações pertencentes à categoria informada serão exibidas.
5.	Mostrar Extrato por Categoria:
●	Exibe um extrato com o total gasto em cada categoria.
●	As categorias e seus respectivos valores totais serão mostrados.
6.	Mostrar Extrato Bancário por Categoria em Outra Moeda:
●	Exibe o extrato bancário por categoria, com os valores convertidos para uma moeda específica.
●	Digite a moeda desejada para conversão e o valor convertido será exibido.
7.	Adicionar Taxa de Câmbio:
●	Digite o código da moeda para a qual deseja adicionar uma taxa de câmbio.
●	Digite a taxa de câmbio para essa moeda.
●	A taxa de câmbio será registrada no sistema.
8.	Sair do Programa:
●	Encerra a execução do programa.
Observações:
●	As transações são salvas em um arquivo chamado "transacoes.csv".
●	Caso o arquivo não exista, ele será criado automaticamente.
●	O sistema utiliza a função os.system("cls" if os.name == "nt" else "clear") para limpar a tela do terminal/console. Dependendo do seu sistema operacional, pode ser que a função não limpe a tela corretamente. Nesse caso, você pode limpar a tela manualmente.
Utilize as opções do menu para interagir com o sistema. Digite o número correspondente à opção desejada e pressione Enter.
Aproveite o Sistema de Rastreamento de Despesas Pessoais e tenha um bom controle financeiro!

![WhatsApp Image 2023-05-25 at 08 39 12](https://github.com/burle77/Trabalhos-Cesar-School/assets/110929191/fc77ebd1-2bd0-40b8-a31b-b3b1dc65b225)

