![Header](../../Images/Header.png)

# Planificação - Mini Projeto Mastermind em C

## 1. Compreensão do problema

| Pergunta                                                          | Resposta                                                                                                                                     |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| O que significa ganhar o jogo?                                    | Ganhar significa introduzir uma tentativa exatamente igual ao código secreto, com os 4 números nas posições corretas.                        |
| O que significa perder o jogo?                                    | Perder significa gastar todas as tentativas válidas sem descobrir o código secreto.                                                          |
| O que torna uma tentativa válida?                                 | A tentativa tem exatamente 4 números inteiros, todos entre 1 e 6, sem números repetidos.                                                     |
| O que torna uma tentativa inválida?                               | Uma tentativa é inválida se tiver menos ou mais de 4 números, valores fora de 1 a 6, texto em vez de números ou números repetidos.           |
| Uma tentativa inválida deve gastar uma tentativa?                 | Não. Como a tentativa não respeita as regras do jogo, não deve ser guardada nem contar como tentativa usada.                                 |
| Que informação o jogador precisa de ver depois de cada tentativa? | Precisa de ver quantos números estão certos na posição certa e quantos números existem no código, mas estão na posição errada.               |
| Que informação o programa precisa de guardar?                     | O código secreto, o histórico das tentativas válidas, o resultado de cada tentativa, o número de tentativas usadas e o estado atual do jogo. |

## 2. Requisitos funcionais

| Nº  | Requisito funcional                                                                     |
| --- | --------------------------------------------------------------------------------------- |
| 1   | O programa deve guardar um código secreto com 4 números.                                |
| 2   | O programa deve garantir que cada número do código secreto está entre 1 e 6.            |
| 3   | O programa deve garantir que o código secreto não tem números repetidos.                |
| 4   | O programa deve mostrar um menu inicial com as opções jogar, regras e sair.             |
| 5   | O programa deve permitir ao jogador introduzir uma tentativa com 4 números.             |
| 6   | O programa deve validar se a tentativa tem exatamente 4 números inteiros.               |
| 7   | O programa deve rejeitar tentativas com números fora do intervalo 1 a 6.                |
| 8   | O programa deve rejeitar tentativas com números repetidos.                              |
| 9   | O programa deve garantir que uma tentativa inválida não conta como tentativa usada.     |
| 10  | O programa deve comparar uma tentativa válida com o código secreto.                     |
| 11  | O programa deve mostrar os números certos na posição certa.                             |
| 12  | O programa deve mostrar os números certos na posição errada.                            |
| 13  | O programa deve guardar o histórico das tentativas válidas.                             |
| 14  | O programa deve terminar com vitória quando o código for descoberto.                    |
| 15  | O programa deve terminar com derrota quando forem usadas todas as tentativas.           |
| 16  | O programa deve permitir que o jogador desista ao escrever `0` durante a partida.       |

## 3. Entradas

| Entrada                      | Tipo em C | Exemplo válido | Exemplo inválido |
| ---------------------------- | --------- | -------------- | ---------------- |
| Opção do menu inicial        | `int`     | `1`, `2`, `0`  | `9`              |
| Opção de desistência         | `int`     | `0`            | `sair`           |
| Primeiro número da tentativa | `int`     | `3`            | `8`              |
| Segundo número da tentativa  | `int`     | `5`            | `0`              |
| Terceiro número da tentativa | `int`     | `1`            | `abc`            |
| Quarto número da tentativa   | `int`     | `6`            | `2.5`            |
| Tentativa completa           | `int[4]`  | `3 6 1 5` ou `3615` | `1 2 2 4`        |

## 4. Saídas

| Situação                         | Saída esperada                                                          |
| -------------------------------- | ----------------------------------------------------------------------- |
| Início do jogo                   | Título do jogo e regras principais.                                     |
| Menu inicial                     | Opções jogar, regras e sair.                                            |
| Estado da partida                | Tentativas usadas e histórico antes de pedir a próxima tentativa.       |
| Tentativa válida                 | Número de certos na posição certa e número de certos na posição errada. |
| Tentativa inválida por intervalo | Mensagem a indicar que todos os números devem estar entre 1 e 6.        |
| Tentativa inválida por repetição | Mensagem a indicar que não é permitido repetir números.                 |
| Vitória                          | Mensagem de parabéns e número de tentativas usadas.                     |
| Derrota                          | Mensagem a indicar que foram gastas todas as tentativas.                |
| Desistência                      | Mensagem a indicar que o jogador desistiu.                              |
| Fim do jogo                      | Código secreto gerado e resumo das tentativas válidas.                  |

## 5. Estruturas de dados escolhidas

| Estrutura                 | Utilização                                                              | Justificação                                                             |
| ------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `int codigo_secreto[4]`   | Guarda o código secreto gerado.                                         | O código tem sempre 4 números inteiros.                                  |
| `int tentativa[4]`        | Guarda temporariamente a tentativa atual.                               | A tentativa tem a mesma estrutura do código secreto.                     |
| Constantes de estado      | Representam se o jogo está em curso, vitória, derrota ou desistência.   | Tornam o código mais legível do que usar números sem nome.               |
| Constantes de validação   | Representam o resultado da validação de uma tentativa.                  | Permitem distinguir erros diferentes.                                    |
| `struct Tentativa`        | Guarda os valores de uma tentativa e os dois resultados da comparação.  | Cada tentativa válida precisa de ficar no histórico com o seu resultado. |
| `struct Jogo`             | Guarda o código secreto, histórico, tentativas usadas e estado do jogo. | Junta os dados principais da partida numa estrutura simples.             |
| `Tentativa historico[10]` | Guarda até 10 tentativas válidas.                                       | É um array estático de structs, como pedido no enunciado.                |

## 6. Funções previstas

| Ação necessária                | Nome da função               | Recebe dados? | Altera dados? | Devolve resultado? |
| ------------------------------ | ---------------------------- | ------------- | ------------- | ------------------ |
| Inicializar a partida          | `inicializar_jogo`           | Sim           | Sim           | Não                |
| Criar o código secreto         | `criar_codigo_secreto`       | Sim           | Sim           | Não                |
| Mostrar o título               | `mostrar_titulo`             | Não           | Não           | Não                |
| Mostrar as regras              | `mostrar_regras`             | Não           | Não           | Não                |
| Mostrar o menu inicial         | `mostrar_menu_inicial`       | Não           | Não           | Não                |
| Mostrar o estado da partida    | `mostrar_estado_partida`     | Sim           | Não           | Não                |
| Mostrar o histórico            | `mostrar_historico`          | Sim           | Não           | Não                |
| Ler a opção do menu            | `ler_opcao`                  | Não           | Não           | Sim                |
| Ler uma tentativa              | `ler_tentativa`              | Sim           | Sim           | Sim                |
| Validar uma tentativa          | `validar_tentativa`          | Sim           | Não           | Sim                |
| Verificar o intervalo          | `valores_estao_no_intervalo` | Sim           | Não           | Sim                |
| Verificar repetições           | `tem_valores_repetidos`      | Sim           | Não           | Sim                |
| Verificar desistência          | `linha_tem_apenas_zero`      | Sim           | Não           | Sim                |
| Verificar espaços              | `caractere_e_espaco`         | Sim           | Não           | Sim                |
| Ler tentativa por dígitos      | `ler_tentativa_por_digitos`  | Sim           | Sim           | Sim                |
| Comparar tentativa e código    | `comparar_tentativa`         | Sim           | Sim           | Não                |
| Guardar tentativa no histórico | `guardar_tentativa`          | Sim           | Sim           | Não                |
| Processar uma tentativa        | `processar_tentativa`        | Sim           | Sim           | Não                |
| Jogar uma partida              | `jogar_partida`              | Não           | Sim           | Não                |
| Mostrar o resumo final         | `mostrar_resumo_final`       | Sim           | Não           | Não                |

## 7. Algoritmo de comparação

O algoritmo percorre as 4 posições da tentativa.

1. Se `tentativa[i] == codigo_secreto[i]`, o número está certo e na posição certa.
2. Se os valores forem diferentes, a função verifica se `tentativa[i]` existe noutra posição do código secreto.
3. Se existir, conta como certo na posição errada.
4. Como o código e a tentativa não têm números repetidos, não é necessário marcar números já usados.

Exemplo teórico com código secreto `3 6 1 5` e tentativa `6 3 5 1`:

| Posição | Código secreto | Tentativa | Resultado                                        |
| ------- | -------------- | --------- | ------------------------------------------------ |
| 1       | `3`            | `6`       | O `6` existe no código, mas está noutra posição. |
| 2       | `6`            | `3`       | O `3` existe no código, mas está noutra posição. |
| 3       | `1`            | `5`       | O `5` existe no código, mas está noutra posição. |
| 4       | `5`            | `1`       | O `1` existe no código, mas está noutra posição. |

Resultado: `0` certos na posição certa e `4` certos na posição errada.

## 8. Registo dos testes obrigatórios

Para compilar o programa, usei:

```bash
cc -Wall -Wextra -std=c11 "C/Mini Projeto/21_mini_projeto_mastermind.c" -o /tmp/mastermind
```

O código secreto é gerado automaticamente no início de cada partida.

| Teste | O que foi testado                  | Dados introduzidos                                                          | Resultado esperado                                                            | Resultado obtido                                               |
| ----- | ---------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------- |
| A     | Valor fora do intervalo            | Menu `1`, tentativa `1239`                                                  | A tentativa é recusada e não conta.                                           | A tentativa é recusada e o contador de tentativas não aumenta. |
| B     | Número repetido                    | Menu `1`, tentativa `1224`                                                  | A tentativa é recusada e não conta.                                           | A tentativa é recusada e o contador de tentativas não aumenta. |
| C     | Nenhum número certo                | Não existe uma tentativa válida possível com estas regras.                  | O enunciado pede `0` e `0`, mas isso é matematicamente impossível neste jogo. | Teste registado como impossível sem alterar as regras.         |
| D     | Valores certos em posições erradas | Uma tentativa com valores do código gerado, mas noutra ordem.                | O programa conta esses valores como certos na posição errada.                 | O programa mostra os valores certos na posição errada.         |
| E     | Vitória                            | Uma tentativa igual ao código gerado nessa partida.                          | O jogo termina com vitória.                                                   | O jogo termina com mensagem de vitória.                        |
| F     | Derrota                            | Dez tentativas válidas incorretas.                                           | O jogo termina com derrota após 10 tentativas válidas.                        | O jogo termina com mensagem de derrota.                        |
| G     | Desistência                        | Menu `1`, depois tentativa `0`                                              | O jogo termina com mensagem de desistência.                                   | O jogo termina com mensagem de desistência.                    |

### Nota sobre o Teste C

Com os números disponíveis entre `1` e `6`, tanto o código secreto como a tentativa têm 4 números diferentes. Isso significa que dois conjuntos de 4 números escolhidos de um conjunto total de 6 têm sempre pelo menos 2 números em comum. Por isso, uma tentativa válida com `0` números certos não pode acontecer nesta versão do jogo.

![Footer](../../Images/Footer.png)
