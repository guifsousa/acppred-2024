# acppred

By guilherme feijo de sousa

anticancer peptide prediction software

## Setup

Run the following command to install the acppred program(mamba is required).

```
$ make setup
```
- enviroment.yml: O enviroment é uma forma integrada de criar um ambiente. O ambiente virtual cria uma pasta que contém uma cópia para um interpretador específico. Quando se instala os pacotes nestes ambientes, ele vai acabar nesta nova pasta e portanto, isolado de outros pacotes usados por outros espaços de trabalho. É gerenciado usando o conda.

- Makefile: arquivo que centraliza os comandos para serem executados pelo programa "make".

- requirements.txt: Bibliotecas de Python que precisam ser instaladas utilizando o pip.O pip é um gerenciador de pacotes do Python que instala e atualiza pacotes.

ATIVIDADE FINAL - ENGEHARIA DE SOFTWARE PARA BIOINFORMÁTICA E APRENDIZADO DE MÁQUINA:
    By guilherme feijo de sousa

- O que é a ferramenta conda, e qual a sua utilidade no desenvolvimento de programas em Python?
    O Conda é uma ferramenta  de gerenciamento de pacotes e ambientes para várias linguagens de programação, incluindo Python. Essa ferramenta permite aos desenvolvedores instalar, configurar e gerenciar facilmente os pacotes necessários para seus projetos em Python. Ele lida automaticamente com as dependências de cada pacote, garantindo que todas as bibliotecas necessárias estejam instaladas e funcionando corretamente. Nesse sentido, o conda possibilita criar ambientes virtuais isolados uns dos outros, sendo essa funcionalidade valiosa para lidar com diversos projetos que demandam versões distintas das mesmas bibliotecas. Cada ambiente virtual pode ser configurado com seus próprios pacotes, previnindo conflitos e garantindo compatibilidade adequada.

- Como funciona a ferramenta ACPred? Qual a sua finalidade?
   O ACPred  uma ferramenta de fácil interpretação usada para prever e caracterizar as atividades anticâncer de peptídeos. O ACPed utiliza algoritmos de aprendizado de máquina (support vector machine and random forest) e técnicas de bioinformática para analisar as propriedades dos peptídeos anticâncer e prever sua atividade. Esse método se baseia nas propriedades quantitativas e qualitativas dos aminoácidos, utilizando um perfil binário para representar numericamente as sequências peptídicas. O ACPred apresenta uma estrutura geral que pode ser dividida em quatro etapas: na primeira etapa, é feita do preparo dos dados de referência; na segunda etapa,as características peptídicas são extraídas e combinadas; na terceira etapa, as características mais importantes são analisadas para a previsão de antígenos anticâncer utilizando o modelo random forest e por fim, o webservidor é construído com acesso ao público, utilizando o melhor modelo.


- O que são aplicações CLI? Quais os comandos e opções (argumentos) criadas para a ferramenta desenvolvidas no projeto?
    As aplicações CLI (Interface de linha de Comando) são ferramentas de software que interagem com o usuário por meio de uma linha de comando, em oposição a uma interface gráfica. Isso significa que o usuário digita comandos diretamente em um terminal ou prompt de comando para interagir com a aplicação. Durante o desenvolvimento de uma aplicação CLI, são definidos diversos comandos e opções (argumentos) que os usuários podem utilizar para realizar diferentes tarefas ou ajustar o funcionamento da aplicação. Esses comandos e opções são elementos essenciais que fazem parte do modo como a aplicação é utilizada e gerenciada. No caso do projeto desenvolvido ao longo da disciplina, alguns comandos específicos foram utilizados:
      **acppred
      ** conda create - criará um novo ambiente em um subdiretório do diretório de trabalho atual
      **conda activate - ativa um ambiente criado
      ** git commit - registra alterações no repositório
      ** git push - atualiza referências remotas junto com objetos associados 


- O que é back-end e front-end no contexto de aplicação web?
   No contexto de aplicação web, o back-end é responsável pelo processamento de dados e interação com o servidor. Ele vai lidar com todas as operações que acontecem nos bastidores do webservidor, como processamento dos dados, autenticação de usuários e manipulação dos arquivos. No back-end, incluem tecnologias envovlendo a linguagem Python e frameworks como o Flask. Já o front-end é a parte da aplicação web com a qual os usuários interagem diretamente, englobando tudo que é visualizado em um navegador ou dispositivo do usuário, como interfaces gráficas, formulários, menus, animações, dentre outros. No front-end, incluem tecnologias como HTML e CSS.

- O que são testes unitários? Qual a sua importância no desenvolvimento de software?
   Os testes unitários são práticas que avaliam unidades isoladas do código, como funções, métodos ou classes, para assegurar o funcionamento correto dos mesmos. Cada teste unitário atua na verificação de uma pequena parte do código, testando os possíveis cenários previstos e imprevistos para essa unidade em particular. Para o desenvolvimento de diferentes softwares, a realização dos testes unitários é muito importante, pois garante a qualidade dp código, identificando possíveis erros ou problemas;  permitem a realização de refatorações no código com confiança, sabendo que se algo der errado, os testes unitários sinalizarão as falhas, bem como garantir a estabilidade e a  do software, ajudando os desenvolvedores a escrever código robusto e confiável.
   
