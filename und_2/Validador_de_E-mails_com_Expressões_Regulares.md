# Validador de E-mails com Expressões Regulares

Atividade da disciplina de **Linguagens Formais e Autômatos (LFA)**.

## Sobre o projeto

O programa solicita cinco endereços de e-mail, valida cada um com uma expressão regular,
separa os válidos dos inválidos e, ao final, mostra os dois grupos junto com o
motivo da rejeição de cada entrada inválida.

## A expressão regular

```
^[A-Za-z0-9_%+-]+(\.[A-Za-z0-9_%+-]+)*@([A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}$
```

- **Usuário:** `bloco(.bloco)*` — o ponto só aparece entre blocos, o que impede
  ponto no início, ponto imediatamente antes do `@` e dois pontos consecutivos.
- **Domínio:** cada parte começa e termina com letra ou dígito, deixando o hífen
  apenas no meio; no fim, um domínio de topo com 2 ou mais letras.

## Casos de teste

| Endereço | Resultado | Motivo |
|---|---|---|
| maria@gmail.com | válido | — |
| joao.silva@udf.edu.br | válido | — |
| estudante_01@faculdade.com | válido | — |
| pedro.gmail.com | inválido | não tem o símbolo `@` |
| ana@dominio | inválido | o domínio não tem `.com`, `.br`, etc. |

## Como executar

O arquivo é um notebook do Google Colab. Faça o download e abra em
**Arquivo → Fazer upload de notebook**, ou rode localmente com Jupyter.

📎 **Arquivo do projeto:** [validador_emails_colab.ipynb](https://colab.research.google.com/drive/1w8BaqU8e2DHpp3oOXp_ZU2HJJbQR-RW9?usp=drive_link)
