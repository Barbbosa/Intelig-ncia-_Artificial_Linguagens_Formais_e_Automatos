# Atividade — Agentes Inteligentes (Capítulo 2)

## Exercício 2.3 — Verdadeiro ou falso

**a) "Um agente que detecta apenas informações parciais sobre o estado não pode ser perfeitamente racional."**
**Falso.** Ser racional é fazer a melhor escolha com o que se sabe, não saber tudo. O aspirador simples só vê o quadrado em que está e mesmo assim age bem.

**b) "Existem ambientes de tarefa nos quais nenhum agente reativo puro pode comportar-se racionalmente."**
**Verdadeiro.** O agente reativo decide só pelo que vê agora, sem lembrar do passado. Se a decisão certa depende do que aconteceu antes, ele não consegue. Exemplo: um aspirador sem sensor de posição não sabe se deve ir para a esquerda ou para a direita.

**c) "Existe um ambiente de tarefa em que todo agente é racional."**
**Verdadeiro.** Se qualquer ação dá o mesmo resultado, qualquer agente é racional. Exemplo: um mundo em que tudo já está limpo e nada muda, não importa o que o aspirador faça.

**d) "A entrada para o programa de agente é a mesma que a entrada para a função de agente."**
**Falso.** A função recebe toda a sequência de percepções (o histórico). O programa recebe só a percepção atual e, se precisar do histórico, tem que guardá-lo.

**e) "Toda função de agente é implementável por uma combinação de programa/máquina."**
**Falso.** Algumas funções exigiriam memória infinita ou resolver problemas impossíveis de calcular, e uma máquina real tem limites de memória e tempo.

**f) "Suponha que um agente selecione sua ação uniformemente ao acaso do conjunto de ações possíveis. Existe um ambiente de tarefa determinista em que esse agente é racional."**
**Verdadeiro.** Se todas as ações dão o mesmo resultado (como no mundo já limpo), escolher ao acaso é tão bom quanto qualquer outra escolha.

**g) "É possível para um dado agente ser perfeitamente racional em dois ambientes de tarefa distintos."**
**Verdadeiro.** Se nos dois ambientes a melhor ação for a mesma, o mesmo agente serve nos dois. Exemplo: o aspirador simples funciona bem em duas casas com sujeira em lugares diferentes.

**h) "Todo agente é racional em um ambiente não observável."**
**Falso.** Mesmo sem perceber nada, nem toda ação é boa. Um aspirador sem sensores que fica parado é pior do que um que aspira e se move.

**i) "Um agente jogador de pôquer perfeitamente racional nunca perde."**
**Falso.** Ser racional é tomar a melhor decisão possível, não garantir o resultado. No pôquer há sorte e cartas escondidas, então dá para fazer a melhor jogada e perder mesmo assim.

---

## Exercício 2.4 — Descrição PEAS e propriedades

Legenda: **P** = desempenho, **E** = ambiente, **A** = atuadores, **S** = sensores.

### 1) Jogar futebol
- **P:** gols marcados, gols evitados, vitória do time, poucas faltas
- **E:** campo, bola, companheiros, adversários, árbitro
- **A:** pernas e pés, cabeça, voz e gestos
- **S:** visão, audição, tato
- **Propriedades:** parcialmente observável, vários agentes (colaboram com o time e competem com o adversário), imprevisível, sequencial, dinâmico, contínuo, regras conhecidas.

### 2) Explorar os oceanos subterrâneos de Titã
- **P:** dados e amostras coletados, área explorada, equipamento preservado, pouca energia gasta
- **E:** gelo, oceano debaixo dele, pressão e temperatura extremas, correntes
- **A:** propulsores, broca para o gelo, braço coletor, antena de rádio
- **S:** câmeras, sonar, sensores de temperatura e pressão, sensores químicos, medidor de bateria
- **Propriedades:** parcialmente observável, um agente só, imprevisível, sequencial, dinâmico, contínuo, ambiente desconhecido (o robô tem que aprender).

### 3) Comprar livros usados de IA na Internet
- **P:** conseguir os livros certos, em bom estado, pelo menor preço total (com frete), dentro do prazo
- **E:** lojas e sites de venda, vendedores, outros compradores, pagamento, entrega
- **A:** pesquisar, abrir páginas, colocar no carrinho, pagar, mandar mensagem ao vendedor
- **S:** conteúdo das páginas (preço, descrição, fotos, avaliações), confirmação do pedido, rastreamento
- **Propriedades:** parcialmente observável, vários agentes (competição), imprevisível, sequencial, dinâmico (preços mudam), discreto, parcialmente conhecido.

### 4) Jogar uma partida de tênis
- **P:** ganhar pontos, games, sets e a partida; cometer poucos erros
- **E:** quadra, bola, rede, adversário, juiz
- **A:** braço e raquete, pernas
- **S:** visão, audição, tato
- **Propriedades:** parcialmente observável, vários agentes (competição), imprevisível, sequencial, dinâmico, contínuo, regras conhecidas.

### 5) Praticar tênis contra uma parede
- **P:** mais rebatidas seguidas, precisão, poucos erros
- **E:** parede, bola, piso
- **A:** braço e raquete, pernas
- **S:** visão, audição, tato
- **Propriedades:** parcialmente observável, um agente só (a parede é só um objeto), pouco imprevisível, sequencial, dinâmico, contínuo, conhecido.

### 6) Realizar um salto de altura
- **P:** altura mais alta sem derrubar o sarrafo, poucas tentativas gastas, sem lesão
- **E:** pista, sarrafo, colchão, regras, vento
- **A:** pernas (corrida e impulso), tronco e braços
- **S:** visão, equilíbrio, sensação do próprio corpo
- **Propriedades:** parcialmente observável, um agente só (os outros atletas saltam em outro momento), imprevisível, cada tentativa é separada, contínuo, conhecido.

### 7) Licitações de um item em um leilão
- **P:** ganhar o item pagando o menos possível, sem passar do limite
- **E:** casa ou site de leilão, leiloeiro, item, outros licitantes
- **A:** dar lance, esperar, desistir
- **S:** lance atual, lances dos outros, tempo restante, descrição do item
- **Propriedades:** parcialmente observável (não sabe o limite dos outros), vários agentes (competição), imprevisível, sequencial, dinâmico, discreto, regras conhecidas.

### Comparações

**Tênis contra uma pessoa × contra a parede.** Contra uma pessoa, o adversário pensa, muda de estratégia e tenta te vencer, então é mais difícil de prever. Contra a parede, a bola volta de forma previsível e não há ninguém tentando te atrapalhar, então é mais simples.

**Informações incompletas na compra de livros.** O agente não sabe o estoque real, se o livro está mesmo como descrito, se o vendedor é confiável, nem como os preços vão mudar. Por isso precisa guardar o histórico (preços, avaliações) para fazer o melhor palpite.

**Outros agentes no futebol e no leilão.** No futebol, os companheiros ajudam e os adversários atrapalham, então é preciso adivinhar o que cada um vai fazer. No leilão, cada lance dos outros muda o preço e o resultado, então o agente precisa considerar o que eles podem fazer antes de decidir.

---

## Exercício 2.5 — Definições com minhas palavras

1. **Agente:** qualquer coisa que percebe o ambiente por sensores e age nele por atuadores. *Exemplo:* um robô aspirador.
2. **Função de agente:** a "tabela" que diz qual ação tomar para cada sequência de percepções possível. *Exemplo:* [A, sujo] → aspirar; [A, limpo] → ir para a direita.
3. **Programa de agente:** o código que realmente roda e implementa a função de agente, recebendo a percepção atual e devolvendo uma ação. *Exemplo:* o código do aspirador reativo.
4. **Racionalidade:** escolher a ação que se espera que dê o melhor resultado, com base no que o agente percebeu e sabe. *Exemplo:* atravessar uma rua vazia é racional, mesmo que algo improvável aconteça.
5. **Autonomia:** quando o agente aprende e decide com base na própria experiência, e não só no que o projetista programou. *Exemplo:* um aspirador que aprende em quais horários a casa fica mais suja.
6. **Agente reativo:** age só pelo que percebe agora, com regras do tipo "se isso, então aquilo". *Exemplo:* se o carro da frente frear, frear também.
7. **Agente baseado em modelo:** guarda uma noção do estado do mundo, para lidar com o que não consegue ver no momento. *Exemplo:* um carro que lembra onde estavam os outros veículos ao trocar de pista.
8. **Agente baseado em objetivos:** escolhe as ações pensando em alcançar um objetivo. *Exemplo:* um táxi que decide virar à esquerda ou à direita conforme o destino do passageiro.
9. **Agente baseado em utilidade:** compara as opções e escolhe a que for "melhor" no conjunto (rapidez, segurança, custo). *Exemplo:* um táxi que escolhe a rota que equilibra tempo, segurança e preço.
10. **Agente com aprendizagem:** melhora com a experiência, aprendendo com os acertos e erros. *Exemplo:* um táxi que percebe que uma manobra brusca irrita os outros motoristas e deixa de fazê-la.

---

## Síntese com autômatos

**Cenário:** licitação em um leilão (caso 7), com um limite máximo de preço para o agente.

**Estados**
- **S0:** disputando, mas outro está na frente
- **S1:** liderando, com o lance mais alto
- **S2:** fora do leilão

**Percepções**
- **p1:** outro licitante deu um lance que ainda cabe no meu limite
- **p2:** outro licitante deu um lance acima do meu limite
- **p3:** o leilão acabou

**Ações**
- **a1:** dar lance
- **a2:** esperar
- **a3:** desistir

**Regras**
- **R1:** (S0, p1) → (S1, a1): se o lance do rival cabe no meu limite, eu cubro e passo a liderar.
- **R2:** (S0, p2) → (S2, a3): se o rival passou do meu limite, eu desisto.

**Como o estado guarda o passado:** só ver o último lance não diz se eu já dei lance ou se ainda estou no leilão. O estado guarda isso: S1 lembra que estou na frente, S0 que estou disputando e S2 que já saí.

**Limitação:** com só três estados, o modelo não guarda o preço atual, o dinheiro que me resta nem o que os outros licitantes podem fazer, que são partes importantes do leilão. Ele também não aprende com leilões anteriores.
