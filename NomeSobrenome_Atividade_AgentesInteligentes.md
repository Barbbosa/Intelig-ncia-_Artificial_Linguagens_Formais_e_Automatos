# Atividade — Agentes Inteligentes (Capítulo 2)

## Identificação

| Campo | Informação |
|---|---|
| Nome | *(preencher)* |
| Matrícula | *(preencher)* |
| Curso | *(preencher)* |
| Disciplina | Inteligência Artificial, Linguagens Formais e Autômatos |
| Professora | Kadidja Valéria |
| Data da aula | 19/10/2026 |
| Material-base | Capítulo 2 — Agentes inteligentes |

---

# Exercício 2.3 — Verdadeiro ou falso

Termos-chave do capítulo usados nas respostas:

- **Racionalidade** (Seção 2.2.1): para cada sequência de percepções possível, o agente racional escolhe a ação que se **espera** maximizar sua medida de desempenho, dada a evidência das percepções e o conhecimento interno. Ela depende de quatro fatores: medida de desempenho, conhecimento prévio, ações possíveis e sequência de percepções.
- **Racionalidade ≠ onisciência ≠ perfeição** (Seção 2.2.2): a racionalidade maximiza o desempenho *esperado*; a perfeição maximiza o desempenho *real*.

## a) "Um agente que detecta apenas informações parciais sobre o estado não pode ser perfeitamente racional."

**Resposta: FALSO.**

**Justificativa.** A definição de racionalidade só exige maximizar o desempenho esperado com base na sequência de percepções e no conhecimento interno. Não exige observabilidade completa. Informação parcial limita o que o agente pode saber, mas não impede que ele escolha a melhor ação possível com o que sabe. Racionalidade não é onisciência.

**Exemplo (contraexemplo da afirmação).** O agente aspirador de pó simples (Fig. 2.3) só percebe o quadrado em que está e se ele está sujo; não vê o outro quadrado, então o ambiente é parcialmente observável. Mesmo assim, o capítulo afirma que, sob as suposições listadas, ele é racional: seu desempenho é pelo menos tão alto quanto o de qualquer outro agente.

**Condições do cenário.** Medida de 1 ponto por quadrado limpo por passo, em 1.000 passos; geografia conhecida; sujeira e posição inicial desconhecidas; sensores corretos para posição e sujeira local; ações Esquerda, Direita e Aspirar.

## b) "Existem ambientes de tarefa nos quais nenhum agente reativo puro pode comportar-se racionalmente."

**Resposta: VERDADEIRO.**

**Justificativa.** O agente reativo simples decide só pela percepção atual, sem memória. Em ambientes parcialmente observáveis, a ação correta pode depender de informação que só existe no histórico. O capítulo observa que esses agentes só funcionam se a decisão correta puder ser tomada pela percepção atual, ou seja, se o ambiente for completamente observável, e que laços infinitos são frequentemente inevitáveis em ambientes parcialmente observáveis.

**Exemplo.** Aspirador sem sensor de posição, com apenas as percepções [Sujo] e [Limpo]. Em [Limpo], mover-se para a Esquerda falha sempre se ele começa em A, e mover-se para a Direita falha sempre se começa em B. Outro exemplo: um carro à frente com luzes de freio antigas, em que um único quadro de vídeo não permite saber se ele está freando; o agente reativo simples frearia sem necessidade ou nunca frearia.

**Condições do cenário.** "Reativo puro" é entendido como reativo simples determinístico, sem estado interno. O capítulo lembra que a aleatoriedade ajuda nesse caso, mas em ambientes de agente único ela em geral não é racional e é possível fazer melhor com agentes determinísticos mais sofisticados (com estado).

## c) "Existe um ambiente de tarefa em que todo agente é racional."

**Resposta: VERDADEIRO.**

**Justificativa.** Se o desempenho esperado é o mesmo para qualquer ação, todas as ações maximizam a medida de desempenho, e portanto qualquer agente é racional.

**Exemplo.** Um mundo do aspirador em que todos os quadrados já estão limpos e permanecem limpos, e a medida de desempenho só pontua quadrados limpos, sem penalizar movimentos nem energia. Qualquer função de agente (aspirar, mover-se ou não fazer nada) obtém a mesma pontuação máxima.

**Condições do cenário.** O ambiente é determinístico, a medida de desempenho independe das ações do agente e as ações não alteram o resultado.

## d) "A entrada para o programa de agente é a mesma que a entrada para a função de agente."

**Resposta: FALSO.**

**Justificativa.** A função de agente recebe a **sequência completa de percepções** (o histórico) e a mapeia para uma ação. O programa de agente recebe **apenas a percepção atual**, porque nada mais está disponível do ambiente (Seção 2.4.1). Se a ação depende do histórico, o programa precisa memorizar as percepções.

**Exemplo.** O AGENTE-DIRIGIDO-POR-TABELA (Fig. 2.7) recebe a percepção atual, mas a anexa a uma lista interna de percepções e usa a sequência acumulada para consultar a tabela. Foi preciso criar uma memória para simular a entrada da função.

**Condições do cenário.** Vale para qualquer agente artificial em que o programa execute em uma arquitetura que entrega uma percepção por vez.

## e) "Toda função de agente é implementável por uma combinação de programa/máquina."

**Resposta: FALSO.**

**Justificativa.** A função de agente é uma descrição matemática abstrata, e existem funções que nenhuma máquina real consegue implementar. O capítulo mostra que a tabela da função é, para a maioria dos agentes, infinita se não houver limite no tamanho das sequências, e que nenhum agente físico teria espaço para armazená-la. Além disso, a função pode exigir algo não computável.

**Exemplo.** Uma função que, para qualquer sequência de percepções, escolhe a ação "Parar" se um programa codificado na sequência termina e "Continuar" se não termina exigiria resolver um problema indecidível. Outro caso é uma função que depende de lembrar sequências arbitrariamente longas, o que exige memória ilimitada, impossível em uma máquina com um número finito de bits.

**Condições do cenário.** A arquitetura tem memória e tempo de computação finitos.

## f) "Suponha que um agente selecione sua ação uniformemente ao acaso do conjunto de ações possíveis. Existe um ambiente de tarefa determinista em que esse agente é racional."

**Resposta: VERDADEIRO.**

**Justificativa.** Se, no ambiente determinístico, todas as ações possíveis resultam no mesmo desempenho, escolher ao acaso é tão bom quanto qualquer outra escolha e maximiza o desempenho esperado. É um caso degenerado: o capítulo diz que, em ambientes de agente único, a aleatoriedade em geral *não* é racional, e aqui ela é racional apenas porque nada diferencia as ações.

**Exemplo.** O mesmo mundo do item (c): tudo limpo, sem penalidade por movimento. Esquerda, Direita, Aspirar ou Nada produzem o mesmo resultado, então o agente aleatório é racional.

**Condições do cenário.** Ambiente determinístico, medida de desempenho insensível à escolha da ação e nenhum custo por ação.

## g) "É possível para um dado agente ser perfeitamente racional em dois ambientes de tarefa distintos."

**Resposta: VERDADEIRO.**

**Justificativa.** A racionalidade depende de medida de desempenho, conhecimento prévio, ações e percepções. Se dois ambientes de tarefa diferentes levam à mesma ação ótima para cada sequência de percepções, o mesmo agente é racional nos dois. O capítulo também define o agente racional para uma *classe* de ambientes, aquele que maximiza o desempenho médio sobre ela.

**Exemplo.** O aspirador simples é racional no mundo A/B com 1.000 passos e continua racional no mesmo mundo com outra distribuição inicial de sujeira (outro ambiente da mesma classe). Também o é em um ambiente que só difere por ter, por exemplo, 500 passos de vida, desde que a medida continue sendo "quadrados limpos por passo".

**Condições do cenário.** As circunstâncias relevantes à racionalidade (medida de desempenho, ações e conhecimento) continuam compatíveis com a mesma função de agente. O capítulo mostra que o mesmo agente seria irracional se a medida penalizasse movimentos.

## h) "Todo agente é racional em um ambiente não observável."

**Resposta: FALSO.**

**Justificativa.** Sem sensores o agente não recebe percepções, mas ainda precisa escolher ações que maximizem o desempenho esperado com base no conhecimento prévio. Nem todas as ações o fazem. O capítulo menciona que, mesmo nesses casos, os objetivos do agente ainda podem ser alcançáveis, e em alguns casos com certeza. Isso exige escolher bem a sequência de ações, e nem todo agente o faz.

**Contraexemplo.** Um aspirador sem nenhum sensor, em um mundo em que a sujeira pode estar em A ou B. Um agente que nunca aspira e só fica parado é claramente pior do que um que alterna Aspirar e movimentos, então não é racional.

**Condições do cenário.** O ambiente é inobservável (sem sensores) e a medida de desempenho premia quadrados limpos.

## i) "Um agente jogador de pôquer perfeitamente racional nunca perde."

**Resposta: FALSO.**

**Justificativa.** Racionalidade não é perfeição. A racionalidade maximiza o desempenho *esperado*, enquanto a perfeição maximiza o desempenho *real*. O pôquer é parcialmente observável (as cartas dos oponentes são ocultas), multiagente e estocástico (Fig. 2.6), então mesmo uma decisão ótima pode levar a uma perda por azar.

**Exemplo.** Um jogador com a melhor mão estatística (por exemplo, probabilidade alta de vencer a rodada) aposta tudo e perde porque o oponente, com mão pior, recebe a carta que precisava. A decisão foi racional e o resultado foi ruim. É análogo ao caso do pedestre atingido pela porta do avião, citado no capítulo.

**Condições do cenário.** Ambiente parcialmente observável e estocástico, com oponentes.

---

# Exercício 2.4 — Descrição PEAS e propriedades dos ambientes

Convenções: **P** = medida de desempenho; **E** = ambiente; **A** = atuadores; **S** = sensores. As propriedades seguem a Seção 2.3.2. Quando a classificação depende da forma de definir o problema, as hipóteses estão explícitas (o capítulo observa, na Fig. 2.6, que as respostas dependem da definição da tarefa).

## 1) Jogar futebol

**Agente e hipóteses.** O agente é um jogador de linha (humano ou robô) em partida oficial, com companheiros, adversários e árbitro. Considera-se o jogo em si, não o campeonato.

| | |
|---|---|
| **P** | Gols a favor, gols evitados, vitória da equipe, poucas faltas e lesões, bons passes |
| **E** | Campo, bola, companheiros, adversários, árbitro, torcida, clima |
| **A** | Pernas e pés (correr, chutar, driblar), cabeça, tronco, voz e gestos (comunicação) |
| **S** | Visão, audição, propriocepção, tato |

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O jogador não vê tudo ao mesmo tempo nem sabe o que os outros pretendem |
| Agentes | Multiagente (cooperativo e competitivo) | Cooperativo com a própria equipe e competitivo com a adversária |
| Determinismo | Estocástico | A trajetória da bola e o comportamento dos outros não se prevê com exatidão; a observabilidade parcial faz o ambiente parecer estocástico |
| Episódico/sequencial | Sequencial | Uma ação (posicionar-se, passar) afeta as futuras |
| Estático/dinâmico | Dinâmico | O jogo continua enquanto o agente delibera |
| Discreto/contínuo | Contínuo | Posição, velocidade e tempo variam continuamente |
| Conhecido/desconhecido | Conhecido | Regras e física são conhecidas; o comportamento dos adversários é incerto |

## 2) Explorar os oceanos subterrâneos de Titã (hipotético)

**Agente e hipóteses.** O agente é uma sonda/submarino robótico autônomo que atravessa a crosta de gelo e explora um oceano líquido sob ela. Hipótese: a comunicação com a Terra tem atraso grande (da ordem de uma hora ou mais), o que obriga o agente a decidir sozinho. Não há outros agentes conhecidos.

| | |
|---|---|
| **P** | Amostras e dados científicos válidos, extensão mapeada, sobrevivência do equipamento, uso eficiente de energia, evitar contaminação |
| **E** | Crosta de gelo, oceano subterrâneo, pressão e temperatura extremas, correntes, possíveis formas de vida desconhecidas |
| **A** | Propulsores e lemes, broca ou derretedor de gelo, braço coletor, aquecedores, transmissor de rádio |
| **S** | Câmeras, sonar, termômetros, sensores de pressão, espectrômetros e sensores químicos, giroscópio, medidor de bateria, receptor de rádio |

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Visibilidade limitada na água e no gelo; muito do ambiente é desconhecido |
| Agentes | Agente único | Hipótese: não há outros agentes; correntes e gelo são tratados como processos físicos |
| Determinismo | Estocástico | Falhas, correntes e gelo se comportam de forma imprevisível |
| Episódico/sequencial | Sequencial | Energia gasta, caminho percorrido e danos afetam todas as decisões futuras |
| Estático/dinâmico | Dinâmico | Correntes e movimento do gelo continuam enquanto o agente decide |
| Discreto/contínuo | Contínuo | Estado, tempo e ações (empuxo, ângulos) são contínuos |
| Conhecido/desconhecido | Desconhecido | As "leis" locais são mal conhecidas, então o agente deve aprender como o ambiente funciona (aprendizagem) |

É o tipo de caso difícil descrito no capítulo: parcialmente observável, estocástico, sequencial, dinâmico, contínuo e desconhecido (aqui com agente único).

## 3) Comprar livros usados de IA na Internet

**Agente e hipóteses.** O agente é um softbot comprador que pesquisa lojas e marketplaces on-line, compara ofertas e conclui compras. Hipóteses: orçamento e prazo definidos, lista de títulos/edições desejados, pagamento autorizado pelo usuário.

| | |
|---|---|
| **P** | Obter os livros desejados em bom estado, com o menor custo total (preço + frete), dentro do orçamento e do prazo, com vendedores confiáveis |
| **E** | Sites de lojas e marketplaces, catálogos, vendedores, outros compradores, sistema de pagamento, transportadoras |
| **A** | Enviar buscas, abrir páginas, filtrar, adicionar ao carrinho, fazer pedido e pagamento, enviar mensagens a vendedores |
| **S** | Conteúdo das páginas e APIs (preços, descrições, fotos, avaliações), confirmações de pedido, e-mails de rastreamento |

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O agente não vê o estoque real, o verdadeiro estado do livro, a confiabilidade do vendedor nem os preços futuros |
| Agentes | Multiagente (competitivo, parcialmente cooperativo) | Vendedores e outros compradores disputam as mesmas ofertas; o vendedor também coopera ao fechar a venda |
| Determinismo | Estocástico | Pedidos podem ser cancelados, estoques acabam e entregas atrasam |
| Episódico/sequencial | Sequencial | Gastar o orçamento em uma compra limita as seguintes |
| Estático/dinâmico | Dinâmico | Preços e estoques mudam enquanto o agente delibera |
| Discreto/contínuo | Discreto | Itens, páginas, ofertas e ações são finitos e distintos (preços em centavos) |
| Conhecido/desconhecido | Parcialmente desconhecido | O agente precisa aprender como cada site funciona e a quem confiar |

## 4) Jogar uma partida de tênis

**Agente e hipóteses.** O agente é um jogador em partida de simples contra outro jogador, com juiz e placar oficial.

| | |
|---|---|
| **P** | Ganhar pontos, games, sets e a partida; poucos erros; evitar lesão |
| **E** | Quadra, bola, rede, adversário, juiz, vento e luz |
| **A** | Braço e raquete (saques, golpes), pernas (deslocamento), tronco |
| **S** | Visão, audição, propriocepção, tato na empunhadura |

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Não se conhece a intenção do adversário nem o efeito exato (giro) da bola |
| Agentes | Multiagente competitivo | O adversário maximiza a própria medida, que minimiza a do agente, como no xadrez |
| Determinismo | Estocástico | O giro, o vento e as ações do adversário não se preveem com exatidão |
| Episódico/sequencial | Sequencial | Cada golpe e cada ponto influencia o resto do jogo (placar, cansaço) |
| Estático/dinâmico | Dinâmico | A bola e o adversário se movem enquanto o agente decide |
| Discreto/contínuo | Contínuo | Posições, velocidades e movimentos são contínuos |
| Conhecido/desconhecido | Conhecido | Regras e física são conhecidas |

## 5) Praticar tênis contra uma parede

**Agente e hipóteses.** O agente é o jogador treinando sozinho. A parede é tratada como objeto que obedece às leis da física, não como agente, pois seu comportamento não é descrito como maximização de uma medida de desempenho.

| | |
|---|---|
| **P** | Maior número de rebatidas consecutivas, precisão e controle, baixa taxa de erros |
| **E** | Parede, bola, piso, espaço de treino |
| **A** | Braço e raquete, pernas, tronco |
| **S** | Visão, audição, propriocepção, tato |

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O giro da bola e as irregularidades do piso e da parede não são totalmente percebidos, embora seja bem mais observável do que contra uma pessoa |
| Agentes | Agente único | Não há outro agente (hipótese acima) |
| Determinismo | Estocástico (de baixa incerteza) | Pequenas imprecisões e irregularidades; o retorno da parede é regido pela física |
| Episódico/sequencial | Sequencial | A posição e o ritmo de um golpe afetam o seguinte |
| Estático/dinâmico | Dinâmico | A bola continua em movimento enquanto o agente decide |
| Discreto/contínuo | Contínuo | Posição e velocidade contínuas |
| Conhecido/desconhecido | Conhecido | A física é conhecida e não há adversário |

## 6) Realizar um salto de altura

**Agente e hipóteses.** O agente é o atleta em uma competição de salto em altura. Hipótese: analisa-se uma tentativa de salto; os outros atletas saltam em turnos separados e não interferem no salto do agente (a disputa é só pela colocação).

| | |
|---|---|
| **P** | Maior altura transposta sem derrubar o sarrafo, menos tentativas gastas, sem lesões |
| **E** | Pista de corrida, sarrafo e suportes, colchão de queda, regras, vento, juízes, outros atletas (indiretamente) |
| **A** | Pernas (corrida e impulsão), tronco e braços (rotação e posição no ar) |
| **S** | Visão, equilíbrio (sistema vestibular), propriocepção, tato dos pés, orientação do treinador |

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Durante o voo o atleta não percebe com exatidão a posição do corpo em relação ao sarrafo |
| Agentes | Agente único (hipótese) | Os outros atletas não alteram a mecânica de um salto; só afetam a colocação |
| Determinismo | Estocástico | Pequenas variações de corrida, vento e impulsão mudam o resultado |
| Episódico/sequencial | Episódico (por tentativa) | Hipótese: cada tentativa é tratada como episódio independente. Sequencial se se considerar a escolha de alturas e a fadiga ao longo da competição, como o torneio de xadrez do capítulo |
| Estático/dinâmico | Semidinâmico | O ambiente não muda enquanto o atleta delibera, mas há tempo limite por tentativa que afeta o desempenho |
| Discreto/contínuo | Contínuo | Movimento do corpo, tempo e altura variam continuamente |
| Conhecido/desconhecido | Conhecido | Regras e física são conhecidas |

## 7) Licitações de um item em um leilão

**Agente e hipóteses.** O agente é um licitante (humano ou software) em leilão inglês ascendente de um único item. Hipóteses: o agente tem um valor máximo privado *v* para o item e um orçamento; os outros licitantes e seus limites são desconhecidos.

| | |
|---|---|
| **P** | Vencer o item pagando o menor preço possível, nunca acima de *v* (maximizar *v* − preço); não estourar o orçamento |
| **E** | Plataforma ou casa de leilões, leiloeiro, item, outros licitantes, regras e relógio do leilão |
| **A** | Dar lance (com valor definido), desistir, aguardar |
| **S** | Lance atual, lances dos outros, tempo restante, descrição e fotos do item, mensagens do leiloeiro |

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | O valor e o orçamento dos outros licitantes e a autenticidade do item não são observáveis |
| Agentes | Multiagente competitivo | Os outros licitantes maximizam a própria medida, que reduz a do agente (apenas um vence) |
| Determinismo | Estocástico | O comportamento futuro dos outros licitantes é incerto |
| Episódico/sequencial | Sequencial | Lances anteriores revelam informação e alteram o preço corrente e as decisões seguintes |
| Estático/dinâmico | Dinâmico | Novos lances podem chegar enquanto o agente delibera; o relógio corre |
| Discreto/contínuo | Discreto | Lances em incrementos fixos, número finito de ações e rodadas |
| Conhecido/desconhecido | Conhecido (regras) | As regras do leilão são conhecidas; só o comportamento dos outros é incerto |

## Comparação entre os casos

**Tênis contra uma pessoa × contra a parede.**
Contra uma pessoa, o ambiente é **multiagente competitivo**: o adversário escolhe golpes para minimizar o desempenho do agente, tem intenções ocultas e pode variar a estratégia, o que aumenta a observabilidade parcial e a incerteza. Contra a parede, o ambiente é de **agente único**: o retorno da bola obedece à física e é muito mais previsível, então só há incerteza residual (giro e irregularidades). Por isso é um ambiente mais simples, bom para treinar técnica. Em ambos o ambiente é sequencial, dinâmico, contínuo e conhecido.

**Informações incompletas na compra de livros.**
O agente não observa o estoque real das lojas, o estado verdadeiro do livro (a descrição pode ser imprecisa), a confiabilidade do vendedor nem a evolução futura dos preços e dos prazos. Por isso o ambiente é **parcialmente observável** e **estocástico**, e o agente precisa de estado interno (histórico de preços, vendedores avaliados) para estimar o "melhor palpite" sobre o estado atual, como no agente baseado em modelo.

**Influência de outros agentes no futebol e no leilão.**
No futebol, os outros agentes são **cooperativos** (companheiros) e **competitivos** (adversários): suas ações alteram o estado do jogo e a medida de desempenho de cada jogador, então a comunicação e a antecipação de intenções fazem parte do comportamento racional. No leilão, os outros licitantes são **competitivos**: cada lance de um altera o preço e o resultado dos demais, e o comportamento deles só pode ser previsto de forma probabilística. Nos dois casos, para decidir bem o agente precisa tratar as outras entidades como agentes (cujo comportamento busca maximizar uma medida) e não apenas como objetos físicos.

---

# Exercício 2.5 — Definições com minhas palavras

1. **Agente.** É qualquer coisa capaz de perceber o ambiente por sensores e agir sobre ele por atuadores. A noção serve como ferramenta de análise de sistemas, não como rótulo absoluto.
   *Exemplo:* um robô aspirador que percebe sujeira e se move/aspira.

2. **Função de agente.** É a descrição matemática, externa e abstrata, do comportamento do agente: mapeia cada sequência de percepções possível para uma ação. Pode ser pensada como uma tabela (em geral enorme ou infinita).
   *Exemplo:* a tabela parcial da Fig. 2.3: [A, Sujo] → Aspirar; [A, Limpo] → Direita.

3. **Programa de agente.** É a implementação concreta da função de agente, executada em uma arquitetura (agente = arquitetura + programa). Recebe só a percepção atual e devolve uma ação; se precisar do histórico, tem de memorizá-lo.
   *Exemplo:* o pseudocódigo AGENTE-ASPIRADOR-DE-PÓ-REATIVO (Fig. 2.8), muito menor que a tabela que implementa.

4. **Racionalidade.** É escolher, para cada sequência de percepções, a ação que se espera maximizar a medida de desempenho, dados a evidência das percepções e o conhecimento interno. Maximiza o desempenho *esperado*, não o real, e não exige onisciência.
   *Exemplo:* o pedestre que atravessa a rua sem tráfego é racional, mesmo que seja atingido por uma porta de avião que cai.

5. **Autonomia.** É a capacidade de o agente se apoiar nas próprias percepções e aprendizado, e não só no conhecimento que o projetista lhe deu. Um agente sem autonomia é frágil quando as suposições do projeto falham.
   *Exemplo:* um aspirador que aprende onde e quando aparece mais sujeira, ao contrário da vespa Sphex, que repete o plano inato mesmo com a lagarta afastada.

6. **Agente reativo (reativo simples).** Escolhe a ação só pela percepção atual, por regras condição-ação, ignorando o histórico. É simples, mas só funciona bem se o ambiente for completamente observável.
   *Exemplo:* "se carro-da-frente-está-freando então começar-a-frear".

7. **Agente baseado em modelo.** É um agente reativo que mantém um estado interno, atualizado com um modelo de como o mundo evolui e do que suas ações fazem, para acompanhar aspectos que não vê agora. Serve para ambientes parcialmente observáveis.
   *Exemplo:* o táxi que guarda o quadro anterior da câmera para saber se as luzes de freio do carro à frente acenderam, ou que lembra onde estão os outros carros ao trocar de pista.

8. **Agente baseado em objetivos.** Além do modelo, tem objetivos que descrevem situações desejáveis, e escolhe ações que levam a elas, considerando o futuro (busca e planejamento). É mais flexível, pois basta mudar o objetivo.
   *Exemplo:* o táxi que, em um entroncamento, decide virar à esquerda ou direita conforme o destino do passageiro.

9. **Agente baseado em utilidade.** Usa uma função utilidade, uma internalização da medida de desempenho, para comparar estados e escolher a ação de maior utilidade esperada. Resolve objetivos conflitantes e a incerteza, o que os objetivos sozinhos não fazem.
   *Exemplo:* o táxi que escolhe, entre as rotas ao destino, a que equilibra melhor rapidez, segurança e custo.

10. **Agente com aprendizagem.** Tem elemento de aprendizado, elemento de desempenho, crítico e gerador de problemas, e melhora seus componentes com a experiência e a realimentação. Permite operar em ambientes inicialmente desconhecidos.
    *Exemplo:* o táxi cujo crítico percebe a reação de outros motoristas a uma manobra brusca e o elemento de aprendizado cria a regra de que aquilo foi uma ação ruim.

---

# Síntese com autômatos

**Cenário escolhido:** licitação em um leilão (caso 7 do exercício 2.4), leilão inglês ascendente de um único item, com limite máximo *v* para o agente.

**Estados internos (Q)**

- **S0 — Em disputa, sem liderar:** o agente ainda participa, mas o lance mais alto é de outro.
- **S1 — Liderando:** o último lance do agente é o mais alto até agora.
- **S2 — Fora do leilão:** o agente desistiu (ou foi superado além do seu limite).

**Percepções (Σ)**

- **p1:** novo lance de outro licitante ≤ limite *v* do agente.
- **p2:** novo lance de outro licitante > limite *v*.
- **p3:** tempo esgotado (leilão encerrado).

**Ações (A)**

- **a1:** dar lance (preço atual + incremento).
- **a2:** aguardar.
- **a3:** desistir.

**Regras de transição** (formato: *(estado, percepção) → (novo estado, ação)*)

- **R1:** (S0, p1) → (S1, a1). Se o lance rival ainda cabe no limite, o agente cobre o lance e passa a liderar.
- **R2:** (S0, p2) → (S2, a3). Se o rival ultrapassa o limite, o agente desiste e sai do leilão.

(O autômato completo teria outras transições, por exemplo (S1, p1) → (S0, a2), quando um rival cobre o lance do agente, e (S1, p3) → (S1, a2), quando o leilão termina com o agente liderando.)

**Como o estado interno representa informação passada.** A percepção atual (um novo lance) sozinha não diz se o agente já deu lance nem se ainda está no jogo. O estado guarda esse resumo do histórico: S1 lembra que o último lance do agente é o mais alto, S0 que ele está disputando sem liderar e S2 que já saiu. É o papel do estado interno do agente baseado em modelo: refletir aspectos do histórico que a percepção atual não mostra. O programa do agente só recebe a percepção atual, então essa memória precisa estar no estado.

**Limitação da modelagem.** Um autômato finito com três estados é uma representação atômica e determinística: não representa o preço corrente, o orçamento restante, nem a incerteza sobre os limites e o comportamento dos outros licitantes, que são o centro do problema (ambiente parcialmente observável e estocástico). Para isso seriam necessários estado fatorado (preço, tempo restante, número de rivais) e probabilidades, como em um agente baseado em utilidade; além disso, ele não aprende com leilões anteriores.

---

# Referências

- RUSSELL, S.; NORVIG, P. **Inteligência Artificial**. Capítulo 2 — Agentes inteligentes (Seções 2.1 a 2.5 e Exercícios 2.3 a 2.5). Material disponibilizado para a aula de 19/10/2026.
- UDF Centro Universitário. **Instruções gerais da atividade**. Aula de 19/10/2026, Profa. Kadidja Valéria.

*Conferência final:* todas as respostas têm justificativa; os exemplos correspondem aos conceitos; as hipóteses estão explícitas nos casos do item 2.4; as referências consultadas foram registradas.
