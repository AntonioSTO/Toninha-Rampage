# TONINHA-RAMPAGE

Jogo criado por: - Antônio Sant'Ana de Oliveira
                 - Arthur Bandeira Salvador

Disciplina: Programação Orientada a Objetos

Professor: Filipe Wall Mutz


## Tarefa assinalada:

O trabalho consiste em desenvolver um jogo de 2 jogadores no formato de combate em arena (e.g., bomberman, dota, etc.) utilizando a linguagem Python, a biblioteca pygame e programação orientada a objetos.

O grupo deverá escolher um tema para servir de história de background do jogo como momentos históricos, assuntos estudados ao longo da vida, objetivos do desenvolvimento sustentável da ONU, etc. 


## Contexto histórico:

A fim de contextualizar o jogo criado, o grupo decidiu por tomar como base o massacre das Toninhas, ocorrido na Primeira Guerra Mundial. Todavia, para fugir um pouco da realidade, optamos por criar um universo paralelo, no qual as toninhas tomaram aspectos humanoides, e, tanto essas, quanto os soldados do "exército brasileiro" receberam um tipo de poder para dinamizar as partidas.


## Instalando o jogo:

Para fazer o jogo rodar, primeiro é necessário instalar todos os arquivos deste repositório. Dessa forma, após instalar o git no computador desejado e ter criado uma conta no Github, os seguntes passos devem ser seguidos:

1) Abra uma pasta no computador desejado
2) Nessa pasta, abra o Git BASH
3) Na janela aberta, digite 'git init' para inicializar o repositório
4) Em seguida, 'git branch -M "main"' para alterar o nome da branch principal de 'master' para 'main' (isso é uma boa prática atualmente recomendada)
5) O comando para puxar o projeto para a sua máquina é o 'git clone https://github.com/AntonioSTO/Toninha-Rampage.git'
6) Caso o usuário já tenha instalado o jogo, e haja alguma alteração posterior no código, recomendamos a execução do comando 'git pull', que puxa as alterações feitas no repositório do Github para o seu repositório local

Pronto, os arquivos estão instalados, mas falta instalar o que faz ele rodar. Desse modo, deixaremos abaixo o links de tutoriais para a instalação dessas ferramentas, e o comando de instalação do pygame.

**[Link](https://youtu.be/FTV6kZeKcbI) para instalação do interpretador python e do VS Code**

**Para instalar a biblioteca pygame, abra o terminal (linux) ou prompt de comando (windows) e digite: 'python -m pip install pygame'**

Agora, com tudo instalado, é só rodar o jogo.


## Rodando o Jogo:

O 'Toninha-Rampage' é um jogo que funciona com a junção de vários arquivos '.py' em um só, o "jogo.py", mas **ATENÇÃO** não é ele que deve ser executado.

O arquivo a ser rodado é o **main.py**, que usa a classe "Jogo_Toninha" para englobar os arquivos do projeto, e, dessa classe, usa o método "rodar" para executar todos os comandos de todos os arquivos do programa.

Em tal circunstância, abra o arquivo "main.py" e clique na setinha em formato de "play" para rodá-lo.


## Como jogar o TONINHA-RAMPAGE:

Ao rodar o arquivo "main.py", será aberta a tela inical do jogo. Apertando espaço no teclado, partimos para a tela de contexto histórico, e, mais uma vez apertando espaço, abre-se a tela de seleção do personagem do player1.

A seleção dos personagens é feita com alguns dos botões utilizados na batalha. Para selecionar o player1, utiliza-se as teclas *W* e *S* para mover o retângulo de seleção, e *espaço* para selecionar o personagem desejado pelo jogador 1. A seleção do player2 é semelhante, utilizando-se das teclas *I* e *K* para mover o "selecionador", e *espaço* para selecionar o personagem desejado pelo jogador 2.

Após a seleção do personagem 2, abre-se a tela de combate, e aí começa o embate entre o player1 e o player2, cada um representando seu respectivo time, isto é, o das toninhas, e o dos soldados.

Em cada "cena", a tecla *ESC* pode ser pressionada para voltar à cena anterior (no caso da cena final, ela é usada para fechar o programa).

O Player1 se movimenta com as teclas *W*, *A*, *S*, *D*, e utiliza as teclas *Q* e *E* para acionar habilidades normais e especiais. Do mesmo modo, o Player2 se movimenta com as teclas *I*, *J*, *K*, *L*, e utiliza as teclas *U* e *O* para acionar habilidades normais e especiais.

* NOTA:
    Os personagens "Toninha Maga" e "Soldado Atirador" usam como ataque especial um "ataque a distância", que requer a manipulação do mouse. Caso suas respectivas teclas forem pressionadas, o jogador que primeiro apertar a tecla possui o direito de utilizar o mouse, a fim de tornar a jogatina mais dinâmica e prazerosa.

Na tela de combate, temos áreas livres pelas quais os jogadores podem se mover livremente, áreas as quais o personagem sofre redução em sua velocidade, áreas de blocos inquebráveis, e um objeto quebrável na parte inferior esquerda do mapa.

O vencedor é aquele que possuir a maior vida após os 120 segundos de jogo, ou o que matar o outro personagem.

Após o termino da partida, surge a tela com o resultado final do jogo, indicando seu vencedor.


## Abaixo, encontra-se um vídeo de demonstração do TONINHA-RAMPAGE

Clique **[aqui](https://youtu.be/FT3jzhTvY4Q)** para ter acesso ao vídeo!


## OBS: easter egg

Na cena de seleção, basta apertar "a""m" e um personagem surpresa aparecerá. Tal personagem possui ataque normal do tipo físico, e especial do tipo teleporte, que funciona de acordo com a posição do mouse na tela de jogo.

Vale ressaltar que ambos os players podem jogar com esse personagem supremo, ou melhor, **SUS**PREMO.

## Esperamos que tenham uma excelente jogatina!
