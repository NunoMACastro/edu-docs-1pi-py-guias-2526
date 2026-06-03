![Header](../Images/Header.png)

# Relatório técnico - Funções do Mastermind

Este relatório explica as constantes, as estruturas e as funções criadas no ficheiro `21_mini_projeto_mastermind.c`.

## 1. Constantes principais

| Constante                     | Significado                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| `TAMANHO_CODIGO`              | Quantidade de números do código secreto e de cada tentativa.  |
| `VALOR_MINIMO`                | Menor número permitido numa tentativa.                        |
| `VALOR_MAXIMO`                | Maior número permitido numa tentativa.                        |
| `MAX_TENTATIVAS`              | Número máximo de tentativas válidas.                          |
| `TAMANHO_LINHA`               | Tamanho máximo usado para ler uma linha do terminal.          |
| `OPCAO_SAIR`                  | Opção usada para sair no menu inicial.                        |
| `OPCAO_JOGAR`                 | Opção usada para começar uma partida.                         |
| `OPCAO_REGRAS`                | Opção usada para mostrar as regras.                           |
| `OPCAO_INVALIDA`              | Valor usado quando a opção escrita não é válida.              |
| `OPCAO_FIM_ENTRADA`           | Valor usado quando a entrada termina inesperadamente.         |
| `ESTADO_EM_CURSO`             | Indica que o jogo ainda está a decorrer.                      |
| `ESTADO_VITORIA`              | Indica que o jogador descobriu o código.                      |
| `ESTADO_DERROTA`              | Indica que o jogador gastou todas as tentativas.              |
| `ESTADO_DESISTENCIA`          | Indica que o jogador desistiu.                                |
| `VALIDACAO_OK`                | Indica que uma tentativa é válida.                            |
| `VALIDACAO_ERRO_LEITURA`      | Indica que a tentativa não tem exatamente 4 números inteiros. |
| `VALIDACAO_FIM_ENTRADA`       | Indica que a entrada terminou inesperadamente.                |
| `VALIDACAO_FORA_INTERVALO`    | Indica que existe um número fora de 1 a 6.                    |
| `VALIDACAO_NUMEROS_REPETIDOS` | Indica que existem números repetidos.                         |
| `VALIDACAO_DESISTENCIA`       | Indica que o jogador escreveu `0` durante a partida.          |

## 2. Estruturas principais

### `struct Tentativa`

Guarda uma tentativa válida feita pelo jogador.

| Campo            | Tipo     | Significado                                     |
| ---------------- | -------- | ----------------------------------------------- |
| `valores`        | `int[4]` | Os 4 números introduzidos pelo jogador.         |
| `certos_posicao` | `int`    | Quantidade de números certos na posição certa.  |
| `certos_errada`  | `int`    | Quantidade de números certos na posição errada. |

### `struct Jogo`

Guarda os dados principais da partida.

| Campo               | Tipo            | Significado                             |
| ------------------- | --------------- | --------------------------------------- |
| `codigo_secreto`    | `int[4]`        | Código que o jogador tenta descobrir.   |
| `historico`         | `Tentativa[10]` | Array com as tentativas válidas.        |
| `tentativas_usadas` | `int`           | Número de tentativas válidas já usadas. |
| `estado`            | `int`           | Estado atual da partida.                |

## 3. Funções

### `void mostrar_titulo(void)`

| Aspeto  | Descrição                            |
| ------- | ------------------------------------ |
| Faz     | Mostra o título do jogo no terminal. |
| Recebe  | Nada.                                |
| Altera  | Nada.                                |
| Devolve | Nada.                                |

### `void mostrar_regras(void)`

| Aspeto  | Descrição                            |
| ------- | ------------------------------------ |
| Faz     | Mostra as regras principais do jogo. |
| Recebe  | Nada.                                |
| Altera  | Nada.                                |
| Devolve | Nada.                                |

### `void mostrar_sequencia(const int valores[])`

| Aspeto  | Descrição                                               |
| ------- | ------------------------------------------------------- |
| Faz     | Mostra 4 números na mesma linha, separados por espaços. |
| Recebe  | Um array de inteiros com 4 posições.                    |
| Altera  | Nada.                                                   |
| Devolve | Nada.                                                   |

### `int valor_existe_no_array(const int valores[], int tamanho, int valor)`

| Aspeto  | Descrição                                                        |
| ------- | ---------------------------------------------------------------- |
| Faz     | Procura um número nas primeiras `tamanho` posições de um array.  |
| Recebe  | O array onde pesquisa, o tamanho pesquisado e o valor procurado. |
| Altera  | Nada.                                                            |
| Devolve | `1` se encontrar o valor, `0` se não encontrar.                  |

### `void copiar_valores(int destino[], const int origem[])`

| Aspeto  | Descrição                                                    |
| ------- | ------------------------------------------------------------ |
| Faz     | Copia os 4 valores do array `origem` para o array `destino`. |
| Recebe  | Um array de destino e um array de origem.                    |
| Altera  | O array `destino`.                                           |
| Devolve | Nada.                                                        |

### `void criar_codigo_secreto(int codigo[])`

| Aspeto  | Descrição                                                                             |
| ------- | ------------------------------------------------------------------------------------- |
| Faz     | Gera 4 números aleatórios entre 1 e 6, sem repetições, e guarda-os no array recebido. |
| Recebe  | Um array de inteiros.                                                                 |
| Altera  | O array `codigo`.                                                                     |
| Devolve | Nada.                                                                                 |

### `int valor_esta_no_intervalo(int valor)`

| Aspeto  | Descrição                                                         |
| ------- | ----------------------------------------------------------------- |
| Faz     | Verifica se um número está entre `VALOR_MINIMO` e `VALOR_MAXIMO`. |
| Recebe  | Um inteiro.                                                       |
| Altera  | Nada.                                                             |
| Devolve | `1` se o valor estiver no intervalo, `0` caso contrário.          |

### `int valores_estao_no_intervalo(const int valores[])`

| Aspeto  | Descrição                                                               |
| ------- | ----------------------------------------------------------------------- |
| Faz     | Verifica se todos os números de uma tentativa estão entre 1 e 6.        |
| Recebe  | Um array de inteiros com 4 posições.                                    |
| Altera  | Nada.                                                                   |
| Devolve | `1` se todos os valores forem válidos, `0` se algum valor for inválido. |

### `int tem_valores_repetidos(const int valores[])`

| Aspeto  | Descrição                                                          |
| ------- | ------------------------------------------------------------------ |
| Faz     | Compara os números da tentativa para descobrir se algum se repete. |
| Recebe  | Um array de inteiros com 4 posições.                               |
| Altera  | Nada.                                                              |
| Devolve | `1` se houver repetição, `0` se todos os valores forem diferentes. |

### `int validar_tentativa(const int tentativa[])`

| Aspeto  | Descrição                                                                    |
| ------- | ---------------------------------------------------------------------------- |
| Faz     | Valida se a tentativa está dentro do intervalo e sem números repetidos.      |
| Recebe  | Um array com a tentativa.                                                    |
| Altera  | Nada.                                                                        |
| Devolve | `VALIDACAO_OK`, `VALIDACAO_FORA_INTERVALO` ou `VALIDACAO_NUMEROS_REPETIDOS`. |

### `int linha_tem_apenas_zero(const char linha[])`

| Aspeto  | Descrição                                       |
| ------- | ----------------------------------------------- |
| Faz     | Verifica se a linha escrita pelo jogador é `0`. |
| Recebe  | Uma linha de texto.                             |
| Altera  | Nada.                                           |
| Devolve | `1` se a linha tiver apenas `0`, `0` se não.    |

### `int caractere_e_espaco(char caractere)`

| Aspeto  | Descrição                                                     |
| ------- | ------------------------------------------------------------- |
| Faz     | Verifica se um caractere é espaço, mudança de linha ou tab.   |
| Recebe  | Um caractere.                                                 |
| Altera  | Nada.                                                         |
| Devolve | `1` se for espaço, `0` se não for.                            |

### `int ler_tentativa_por_digitos(const char linha[], int tentativa[])`

| Aspeto  | Descrição                                                              |
| ------- | ---------------------------------------------------------------------- |
| Faz     | Tenta ler uma tentativa escrita com 4 dígitos juntos, como `1256`.     |
| Recebe  | Uma linha de texto e o array onde a tentativa será guardada.           |
| Altera  | O array `tentativa`.                                                   |
| Devolve | `1` se conseguir ler exatamente 4 dígitos, `0` caso contrário.         |

### `const char *mensagem_validacao(int resultado)`

| Aspeto  | Descrição                                                  |
| ------- | ---------------------------------------------------------- |
| Faz     | Escolhe a mensagem adequada para o resultado da validação. |
| Recebe  | Um número que representa o resultado da validação.         |
| Altera  | Nada.                                                      |
| Devolve | Uma mensagem de texto constante.                           |

### `void inicializar_jogo(Jogo *jogo)`

| Aspeto  | Descrição                                                                                                                  |
| ------- | -------------------------------------------------------------------------------------------------------------------------- |
| Faz     | Prepara a partida, cria o código secreto, coloca as tentativas usadas a zero, define o estado inicial e limpa o histórico. |
| Recebe  | Um apontador para `Jogo`.                                                                                                  |
| Altera  | A struct `Jogo` recebida.                                                                                                  |
| Devolve | Nada.                                                                                                                      |

### `void mostrar_historico(const Jogo *jogo)`

| Aspeto  | Descrição                                                                    |
| ------- | ---------------------------------------------------------------------------- |
| Faz     | Mostra todas as tentativas válidas já realizadas e os respetivos resultados. |
| Recebe  | Um apontador para `Jogo`.                                                    |
| Altera  | Nada.                                                                        |
| Devolve | Nada.                                                                        |

### `void mostrar_menu_inicial(void)`

| Aspeto  | Descrição                                |
| ------- | ---------------------------------------- |
| Faz     | Mostra as opções jogar, regras e sair.   |
| Recebe  | Nada.                                    |
| Altera  | Nada.                                    |
| Devolve | Nada.                                    |

### `void mostrar_estado_partida(const Jogo *jogo)`

| Aspeto  | Descrição                                               |
| ------- | ------------------------------------------------------- |
| Faz     | Mostra as tentativas usadas e o histórico da partida.   |
| Recebe  | Um apontador para `Jogo`.                               |
| Altera  | Nada.                                                   |
| Devolve | Nada.                                                   |

### `int ler_opcao(void)`

| Aspeto  | Descrição                                                 |
| ------- | --------------------------------------------------------- |
| Faz     | Lê uma linha do terminal e tenta obter uma opção inteira. |
| Recebe  | Nada.                                                     |
| Altera  | Nada fora da própria função.                              |
| Devolve | A opção lida, `OPCAO_INVALIDA` ou `OPCAO_FIM_ENTRADA`.    |

### `int ler_tentativa(int tentativa[])`

| Aspeto  | Descrição                                               |
| ------- | ------------------------------------------------------- |
| Faz     | Lê `0` para desistir ou 4 números escritos com espaços ou juntos. |
| Recebe  | Um array onde os números serão guardados.               |
| Altera  | O array `tentativa`.                                    |
| Devolve | Um dos valores de validação definidos pelas constantes. |

### `void comparar_tentativa(const int codigo_secreto[], const int tentativa[], int *certos_posicao, int *certos_errada)`

| Aspeto  | Descrição                                                                       |
| ------- | ------------------------------------------------------------------------------- |
| Faz     | Conta os números certos na posição certa e os números certos na posição errada. |
| Recebe  | O código secreto, a tentativa e dois apontadores para guardar os resultados.    |
| Altera  | Os valores apontados por `certos_posicao` e `certos_errada`.                    |
| Devolve | Nada.                                                                           |

### `void guardar_tentativa(Jogo *jogo, const int tentativa[], int certos_posicao, int certos_errada)`

| Aspeto  | Descrição                                                                           |
| ------- | ----------------------------------------------------------------------------------- |
| Faz     | Guarda uma tentativa válida no histórico e aumenta o contador de tentativas usadas. |
| Recebe  | Um apontador para `Jogo`, a tentativa e os dois resultados da comparação.           |
| Altera  | O histórico e `tentativas_usadas`.                                                  |
| Devolve | Nada.                                                                               |

### `void mostrar_resultado_tentativa(int certos_posicao, int certos_errada)`

| Aspeto  | Descrição                                                          |
| ------- | ------------------------------------------------------------------ |
| Faz     | Mostra os dois resultados calculados para uma tentativa.           |
| Recebe  | Dois inteiros: certos na posição certa e certos na posição errada. |
| Altera  | Nada.                                                              |
| Devolve | Nada.                                                              |

### `void processar_tentativa(Jogo *jogo)`

| Aspeto  | Descrição                                                                      |
| ------- | ------------------------------------------------------------------------------ |
| Faz     | Lê, valida, compara, guarda e avalia uma tentativa.                            |
| Recebe  | Um apontador para `Jogo`.                                                      |
| Altera  | O histórico, o número de tentativas usadas e, se necessário, o estado do jogo. |
| Devolve | Nada.                                                                          |

### `void mostrar_resumo_final(const Jogo *jogo)`

| Aspeto  | Descrição                                                                  |
| ------- | -------------------------------------------------------------------------- |
| Faz     | Mostra o resultado final, revela o código secreto e apresenta o histórico. |
| Recebe  | Um apontador para `Jogo`.                                                  |
| Altera  | Nada.                                                                      |
| Devolve | Nada.                                                                      |

### `void jogar_partida(void)`

| Aspeto  | Descrição                                                             |
| ------- | --------------------------------------------------------------------- |
| Faz     | Inicializa uma partida, pede tentativas até terminar e mostra o fim. |
| Recebe  | Nada.                                                                 |
| Altera  | A variável local `jogo`, através das funções chamadas.                |
| Devolve | Nada.                                                                 |

### `int main(void)`

| Aspeto  | Descrição                                                                                                        |
| ------- | ---------------------------------------------------------------------------------------------------------------- |
| Faz     | Mostra o menu inicial e permite jogar, ver regras ou sair.                                                      |
| Recebe  | Nada.                                                                                                            |
| Altera  | Controla a variável local `programa_ativo`.                                                                      |
| Devolve | `0`, indicando que o programa terminou normalmente.                                                              |

## 4. Funções que alteram dados através de apontadores

| Função                 | Dados alterados                                                      |
| ---------------------- | -------------------------------------------------------------------- |
| `inicializar_jogo`     | Altera a struct `Jogo`.                                              |
| `criar_codigo_secreto` | Altera o array do código secreto.                                    |
| `ler_tentativa`        | Altera o array da tentativa.                                         |
| `ler_tentativa_por_digitos` | Altera o array da tentativa.                                   |
| `comparar_tentativa`   | Altera os inteiros apontados por `certos_posicao` e `certos_errada`. |
| `copiar_valores`       | Altera o array de destino.                                           |
| `guardar_tentativa`    | Altera o histórico e o contador dentro de `Jogo`.                    |
| `processar_tentativa`  | Altera o histórico, tentativas usadas e estado do jogo.              |

![Footer](../Images/Footer.png)
