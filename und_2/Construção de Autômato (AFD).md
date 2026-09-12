# Atividade Prática - Construção de Autômato (AFD)

## Problema

Construir um **Autômato Finito Determinístico (AFD)** que reconheça todas as palavras sobre o alfabeto:

**Σ = {0, 1}**

que **terminam com `00`**.

---

## Definição dos Estados

### q0 — Estado Inicial

Não existe um `0` relevante no final da palavra.

### q1

A palavra termina com um único `0`.

### q2 — Estado Final

A palavra termina com `00`.

---

## Tabela de Transições

| Estado Atual | Entrada `0` | Entrada `1` |
| ------------ | ----------- | ----------- |
| q0           | q1          | q0          |
| q1           | q2          | q0          |
| q2           | q2          | q0          |

---

## Diagrama do Autômato

```text
           0
      +---------+
      |         v
->  (q0) -----> (q1)
     ^  1         | 0
     |            v
     +--------- (q2*)
          1       ^
                  |
                  +-- 0
```

**Legenda:**

* `->` Estado inicial
* `*` Estado final

---

## Testes Documentados

### Teste 1

**Palavra:** `100`

**Caminho:**

```text
q0 --1--> q0 --0--> q1 --0--> q2
```

**Resultado:** ✅ Aceita

---

### Teste 2

**Palavra:** `1100`

**Caminho:**

```text
q0 --1--> q0 --1--> q0 --0--> q1 --0--> q2
```

**Resultado:**  Aceita

---

### Teste 3

**Palavra:** `1010`

**Caminho:**

```text
q0 --1--> q0 --0--> q1 --1--> q0 --0--> q1
```

**Resultado:**  Rejeitada

---

## Explicação da Lógica

O autômato mantém o controle dos últimos símbolos lidos:

* **q0**: a palavra não termina em `0`.
* **q1**: a palavra termina em um único `0`.
* **q2**: a palavra termina em `00`.

Sempre que um símbolo `1` é lido, o autômato retorna para **q0**, pois a sequência final deixa de terminar em `00`.

A palavra será **aceita somente se, ao final da leitura, o autômato estiver em q2**, garantindo que os dois últimos caracteres sejam `00`.

---

## Conjunto Formal do AFD

O AFD pode ser representado formalmente por:

**M = (Q, Σ, δ, q0, F)**

Onde:

* **Q = {q0, q1, q2}**
* **Σ = {0, 1}**
* **q0 = q0**
* **F = {q2}**

### Função de Transição

As transições do autômato são:

**δ(q0, 0) = q1**

**δ(q0, 1) = q0**

**δ(q1, 0) = q2**

**δ(q1, 1) = q0**

**δ(q2, 0) = q2**

**δ(q2, 1) = q0**

---

## Conclusão

O AFD proposto reconhece corretamente todas as palavras do alfabeto **{0, 1}** que **terminam com `00`**, satisfazendo os requisitos da atividade.
