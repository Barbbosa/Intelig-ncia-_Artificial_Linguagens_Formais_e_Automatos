Antes de avançar para a próxima aula, verifique se você consegue explicar:

O que é um alfabeto ∑?
- É um conjunto finito de simbolos.

O que é uma cadeia?
- Cadeia é uma sequencia finita de simbolos que pertence a uma familia.

O que significa ɛ?
- Representa uma cadeia que não possui simbolos

Por que |ɛ| = 0?
- Por que o simbilo significa vazio, as duas barras || significa o comprimento da cadeia, nesse caso ocomprimento da cadeia vazia = 0 .

O que é um prefixo?
- É uma parte da palavra que vem no inicio.
```text
EX: abacate --> prefixo A
```
O que é um sufixo?
- É uma parte da palavra que vem no final.
````text
  EX: abacate --> prefixo E
````
O que significa ∑ *?
- Significa que todas as cadeias finitas podem ser fomadas utilizando os simbolos de ∑, incluindo ɛ.
- Se:

```text
Σ = {a, b}
```

então:

```text
Σ* = {ε, a, b, aa, ab, ba, bb, aaa, ...}
````

Se Σ* possui limite de tamanho;
- Não, é infinito. Porém a cadeia individual possui tamanho finito

O que é uma linguagem formal L?
Um conjunto de cadeias

O que significa L⊆Σ∗?
- Todas as palavras / cadeias de L pertencem a Σ∗
  
O que é uma gramática formal?
- Um conjunto de regras que determinam como podemos gerar cadeias de uma linguagem

O que são terminais e não terminais?
Terminais são os símbolos que aparecem na palavra final.
````text
Exemplo: S → aS | ɛ

Aqui:

S → não terminal
a → terminal
ɛ → cadeia vazia

O não terminal é usado durante a geração.

O terminal permanece na palavra final.
````
O que é uma regra de produção?
- É uma regra que diz como substituir um símbolo por outro conjunto de símbolos.

Como ler S > aS | ɛ?
- S produz aS ou ɛ

Como gerar palavras usando uma gramática?
````text
s produz as
as produz aas
aas produz aaas
s produz ɛ
aaas produz aaaɛ
S - aS - aaS - aaaS - aaa
````
