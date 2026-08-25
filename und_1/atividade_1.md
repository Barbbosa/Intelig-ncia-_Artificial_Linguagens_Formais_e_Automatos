# Linguagens Formais — minhas anotações

## Alfabeto Σ = {a, b, c}

- Tem **3 símbolos** nesse alfabeto.
- Os símbolos são: `a`, `b`, `c`.
- O `a` tá no alfabeto? **Sim**, tranquilo.
- E o `d`? **Não**, esse aí não faz parte.
- Uma palavra usando esses símbolos: `caba`, `aba` — dá pra montar várias combinando eles.

---

## Alfabeto Σ = {0, 1}

Testando se umas sequências são palavras válidas:

| Sequência | Válida? | Por quê |
|---|---|---|
| 0101 | Sim | só tem 0 e 1, que estão no alfabeto |
| 00110 | Sim | mesma ideia |
| 012 | Não | o `2` não existe nesse alfabeto |
| 111 | Sim | só usa símbolos válidos |
| 10a | Não | o `a` não pertence a Σ |

A regra é simples: se **todo símbolo** da sequência estiver dentro de Σ, a palavra é válida. Se aparecer um intruso, já era.

---

## Verdadeiro ou falso — Σ = {0, 1}

- `0 ∈ Σ` → **Verdadeiro**, o 0 está no conjunto.
- `1 ∈ Σ` → **Verdadeiro**, o 1 também está.
- `01 ∈ Σ` → **Falso**. Cuidado aqui: `01` é uma palavra (dois símbolos juntos), não um símbolo isolado, então não pertence ao alfabeto.
- `01 ∈ Σ*` → **Verdadeiro**. Isso sim, porque Σ* é o fecho de Kleene — todas as combinações possíveis de símbolos do alfabeto, incluindo palavras com mais de um caractere.
- `2 ∈ Σ` → **Falso**, não existe esse símbolo aqui.
- `101 ∈ Σ*` → **Verdadeiro**, é uma sequência formada só com 0 e 1, então está no fecho de Kleene.

💡 Resumindo: **Σ** guarda só os símbolos individuais. **Σ*** guarda todas as palavras possíveis feitas com esses símbolos (inclusive a palavra vazia).

---

## Linguagem L = {0, 01, 011, 0111}

Essa aqui é simples: só pertence à linguagem quem tá literalmente na lista.

- `0 ∈ L` → Sim
- `01 ∈ L` → Sim
- `0111 ∈ L` → Sim
- `10 ∈ L` → Não (não tá na lista)
- `111 ∈ L` → Não (não tá na lista)
- `011 ∈ L` → Sim

---

## Linguagem L = { bⁿ | n ≥ 1 }

- As cinco primeiras palavras: `b`, `bb`, `bbb`, `bbbb`, `bbbbb`
- O que significa `bⁿ`? É simplesmente "*n* repetições do símbolo b" — bota quantos `b`s o `n` mandar.
- `bbbbbb` pertence à linguagem? **Sim**, é só um monte de b's seguidos (6 no caso).
- E a palavra vazia (`ε`)? **Não**, porque a condição é `n ≥ 1`, ou seja, precisa ter **pelo menos um** b.

---

## L = ∅ vs L = {ε}

Isso aqui costuma confundir, mas a diferença é simples:

- **L = ∅** → é uma linguagem **vazia**, sem nenhuma palavra dentro. Nem a palavra vazia está lá — é tipo uma caixa completamente vazia.
- **L = {ε}** → é uma linguagem que **tem uma palavra**, e essa palavra é a palavra vazia. É tipo uma caixa que não tá vazia, só que dentro dela tem "nada escrito" (o ε).

Respondendo direto:

- Qual das duas tem uma palavra? **{ε}**
- Qual não tem nenhuma? **∅**
- Qual o tamanho da palavra ε? **Zero** (ela não tem símbolo nenhum, só existe como conceito)

---

## Gramática G = (S, A, {0,1}, P, S)

- Variáveis: `{S, A}`
- Terminais: `{0, 1}`
- Produções: `S → 0A` e `A → 1`
- Símbolo inicial: `S`
- Palavra que ela gera: `{01}`

É bem direta: começa no `S`, troca por `0A`, depois troca o `A` por `1`, e pronto, chegou em `01`.

---

## Aplicando a regra várias vezes (S → 0S | 0A → 1, tipo recursiva)

- 1 vez: `S → 0A → 01`
- 2 vezes: `S → 0A → 01 → 001`
- 3 vezes: `S → 0A → 01 → 001 → 0001`
- Derivação completa: `S → 0A → 01 → 001 → 0001`

Basicamente cada vez que aplica de novo, entra mais um `0` na frente.

---

## Gerando `aaab`

Regra tipo `S → aS | b`:

```
S → aS → aaS → aaaS → aaab
```

Cada passo troca o `S` por `a` seguido de um novo `S`, até no final trocar o `S` por `b` e fechar a palavra.

---

## Testando se palavras são geradas pela gramática (regra tipo S → 0S | 1)

- `1` → **Sim**, derivação: `S → 0S → 01`
- `01` → **Sim**, mesma derivação: `S → 0S → 01`
- `001` → **Sim**, derivação: `S → 0S → 01`
- `0001` → **Sim**, derivação: `S → 0S → 01`
- `101` → **Não**
- `1001` → **Não**

*(obs: dá pra notar que as derivações acima parecem repetidas — só cabe revisar se cada palavra realmente exige um número diferente de aplicações da regra `S → 0S`, tipo `001` deveria ser `S → 0S → 00S → 001`)*
