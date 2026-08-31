# Linguagens Formais

## 1 Considere Σ = a , b , c

Responda:

    Quantos símbolos existem no alfabeto? 3
    Quais são os símbolos? a,b, c
    O símbolo a pertence ao alfabeto? Sim
    O símbolo d pertence ao alfabeto? Não
    Escreva uma palavra formada por símbolos desse alfabeto. acaba,baba,babaca.

---

## 2 Considere Alfabeto Σ = {0, 1}

Classifique cada sequência como palavra válida ou não válida: 

| Sequência | Válida? | Por quê |
|---|---|---|
| 0101 | Sim | só tem 0 e 1, que estão no alfabeto |
| 00110 | Sim | mesma ideia |
| 012 | Não | o `2` não existe nesse alfabeto |
| 111 | Sim | só usa símbolos válidos |
| 10a | Não | o `a` não pertence a Σ |

**Todo símbolo** da sequência estiver dentro de Σ, a palavra é válida.

---

## 3 Considere: Σ = 0 , 1

Determine se as afirmações são verdadeiras ou falsas:


- `0 ∈ Σ` → **Verdadeiro**.
- `1 ∈ Σ` → **Verdadeiro**.
- `01 ∈ Σ` → **Falso**.
- `01 ∈ Σ*` → **Verdadeiro**. Σ* é o fecho de Kleene — todas as combinações possíveis de símbolos do alfabeto, incluindo palavras com mais de um caractere.
- `2 ∈ Σ` → **Falso**.
- `101 ∈ Σ*` → **Verdadeiro**, é uma sequência formada só com 0 e 1, então está no fecho de Kleene.

**Σ** guarda só os símbolos individuais. **Σ*** guarda todas as palavras possíveis feitas com esses símbolos (inclusive a palavra vazia).

---

## 4 Considere: L = 0 , 01 , 011 , 0111

Determine se cada palavra pertence à linguagem:

- `0 ∈ L` → Sim
- `01 ∈ L` → Sim
- `0111 ∈ L` → Sim
- `10 ∈ L` → Não 
- `111 ∈ L` → Não
- `011 ∈ L` → Sim

---

## 5 Considere: L = b n ∣ n ≥ 1

    Escreva as cinco primeiras palavras. b, bb, bbb, bbbb, bbbbb
    Explique o significado de b^n. n ocorrencias de b
    A palavra bbbbbb pertence à linguagem? Sim
    A palavra vazia ( ε ) pertence à linguagem? Não
---

## 6 Exercício para o estudante

Explique, com suas próprias palavras, a diferença entre:
A) L = ∅
B) L = ε

Depois responda:

    Qual delas possui uma palavra? B
    Qual delas não possui nenhuma palavra? A
    Qual é o comprimento da palavra ε ? Zero



---

## 7 Considere G = (S,A,0,1,P,S) com P=S→0A, A→1

Identifique
    Conjunto de variáveis**: {S, A}
    Conjunto de terminais**: {0, 1}
    Conjunto de produções**: {S → 0 A, A → 1}
    Símbolo inicial**: S
    Palavras geradas**: {01}

-------------------------------------------------

## 8 Considere S→0S
Começando com S: 
    Aplique a regra uma vez.  S→0S→01
    Aplique a regra duas vezes. S→0S → 00S →001
    Aplique a regra três vezes. S→0S→00S→000S→0001

------------------------------------------------

## 9 Utilizando:G:{S→aSS→b}
gere:aaab


Escreva todos os passos da derivação.
 S→aS→aaS→aaaS→aaab

---

## 10 Considere novamente:G:{S→0SS→1}
Determine se cada palavra pode ser gerada:
1
01
001
0001
101
1001
Para as palavras que podem ser geradas, apresente a derivação completa.

 **1**: Sim, derivação: S → 0 S → 0 1
 **01**: Sim, derivação: S → 0 S → 0 1
 **001**: Sim, derivação: S → 0 S → 0 1
 **0001**: Sim, derivação: S → 0 S → 0 1
 **101**: Não
 **1001**: Não
