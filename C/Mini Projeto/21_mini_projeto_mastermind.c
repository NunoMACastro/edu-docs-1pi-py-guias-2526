/*
 * Mini projeto: Mastermind numérico em consola.
 *
 * Este programa implementa uma versão simples do jogo Mastermind.
 * O jogador tenta descobrir um código secreto com 4 números diferentes.
 * Cada número deve estar entre 1 e 6.
 *
 * O código está dividido em funções para ser mais fácil de ler, testar e
 * corrigir. Foram usados arrays, structs, constantes, funções e apontadores.
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Número de valores existentes no código secreto e em cada tentativa. */
#define TAMANHO_CODIGO 4

/* Limites permitidos para cada número. */
#define VALOR_MINIMO 1
#define VALOR_MAXIMO 6

/* Número máximo de tentativas válidas que o jogador pode usar. */
#define MAX_TENTATIVAS 10

/* Tamanho máximo de uma linha lida do terminal. */
#define TAMANHO_LINHA 100

/* Opções do menu inicial. */
#define OPCAO_SAIR 0
#define OPCAO_JOGAR 1
#define OPCAO_REGRAS 2
#define OPCAO_INVALIDA -1
#define OPCAO_FIM_ENTRADA -2

/* Estados possíveis do jogo. */
#define ESTADO_EM_CURSO 0
#define ESTADO_VITORIA 1
#define ESTADO_DERROTA 2
#define ESTADO_DESISTENCIA 3

/* Resultados possíveis da validação de uma tentativa. */
#define VALIDACAO_OK 0
#define VALIDACAO_ERRO_LEITURA 1
#define VALIDACAO_FIM_ENTRADA 2
#define VALIDACAO_FORA_INTERVALO 3
#define VALIDACAO_NUMEROS_REPETIDOS 4
#define VALIDACAO_DESISTENCIA 5

/*
 * A struct Tentativa guarda uma jogada válida feita pelo jogador.
 *
 * valores:
 *   Guarda os 4 números escritos pelo jogador.
 *
 * certos_posicao:
 *   Guarda quantos números estavam certos e na posição certa.
 *
 * certos_errada:
 *   Guarda quantos números existiam no código secreto, mas estavam
 *   numa posição errada.
 */
typedef struct {
    int valores[TAMANHO_CODIGO];
    int certos_posicao;
    int certos_errada;
} Tentativa;

/*
 * A struct Jogo guarda todos os dados importantes de uma partida.
 *
 * codigo_secreto:
 *   Guarda o código que o jogador tenta descobrir.
 *
 * historico:
 *   Guarda todas as tentativas válidas feitas pelo jogador.
 *
 * tentativas_usadas:
 *   Guarda quantas tentativas válidas já foram usadas.
 *
 * estado:
 *   Guarda a situação atual do jogo.
 */
typedef struct {
    int codigo_secreto[TAMANHO_CODIGO];
    Tentativa historico[MAX_TENTATIVAS];
    int tentativas_usadas;
    int estado;
} Jogo;

/*
 * Mostra o título do jogo no terminal.
 *
 * Recebe: nada.
 * Devolve: nada.
 */
void mostrar_titulo(void)
{
    printf("=== Mastermind Numerico ===\n");
}

/*
 * Mostra as regras principais ao jogador.
 *
 * Recebe: nada.
 * Devolve: nada.
 */
void mostrar_regras(void)
{
    printf("\nRegras:\n");
    printf("- O codigo secreto tem %d numeros.\n", TAMANHO_CODIGO);
    printf("- Cada numero esta entre %d e %d.\n", VALOR_MINIMO, VALOR_MAXIMO);
    printf("- Nao existem numeros repetidos no codigo nem nas tentativas.\n");
    printf("- Uma tentativa invalida nao conta como tentativa usada.\n");
    printf("- Tens %d tentativas validas para descobrir o codigo.\n", MAX_TENTATIVAS);
    printf("- Durante a partida, escreve 0 para desistir.\n");
}

/*
 * Mostra um array com 4 números na mesma linha.
 *
 * Recebe:
 * - valores: array com os números que devem ser mostrados.
 *
 * Devolve: nada.
 */
void mostrar_sequencia(const int valores[])
{
    int i;

    for (i = 0; i < TAMANHO_CODIGO; i++) {
        printf("%d", valores[i]);

        /*
         * Só escreve espaço entre números.
         * Depois do último número não é necessário escrever espaço.
         */
        if (i < TAMANHO_CODIGO - 1) {
            printf(" ");
        }
    }
}

/*
 * Procura um valor dentro de uma parte de um array.
 *
 * Recebe:
 * - valores: array onde a pesquisa vai ser feita.
 * - tamanho: quantidade de posições que devem ser verificadas.
 * - valor: número que se pretende encontrar.
 *
 * Devolve:
 * - 1 se o valor existir no array.
 * - 0 se o valor não existir no array.
 */
int valor_existe_no_array(const int valores[], int tamanho, int valor)
{
    int i;

    for (i = 0; i < tamanho; i++) {
        if (valores[i] == valor) {
            return 1;
        }
    }

    return 0;
}

/*
 * Copia os valores de um array para outro array.
 *
 * Recebe:
 * - destino: array que vai receber os valores.
 * - origem: array de onde os valores vão ser copiados.
 *
 * Devolve: nada.
 */
void copiar_valores(int destino[], const int origem[])
{
    int i;

    for (i = 0; i < TAMANHO_CODIGO; i++) {
        destino[i] = origem[i];
    }
}

/*
 * Cria o código secreto usado nesta partida.
 *
 * Recebe:
 * - codigo: array onde o código secreto vai ser guardado.
 *
 * Devolve: nada.
 *
 * O código é gerado com números aleatórios.
 * Cada número fica entre VALOR_MINIMO e VALOR_MAXIMO.
 * Os números repetidos são rejeitados para respeitar as regras do jogo.
 */
void criar_codigo_secreto(int codigo[])
{
    int quantidade_gerada = 0;

    /*
     * O ciclo continua até o array ter os 4 números necessários.
     * A variável quantidade_gerada indica quantas posições já foram
     * preenchidas corretamente.
     */
    while (quantidade_gerada < TAMANHO_CODIGO) {
        int candidato;

        /*
         * rand() gera um número inteiro pseudoaleatório.
         * O resto da divisão limita esse número ao intervalo pretendido.
         */
        candidato = VALOR_MINIMO + rand() % (VALOR_MAXIMO - VALOR_MINIMO + 1);

        /*
         * O candidato só é guardado se ainda não existir nas posições já
         * preenchidas do código secreto.
         */
        if (!valor_existe_no_array(codigo, quantidade_gerada, candidato)) {
            codigo[quantidade_gerada] = candidato;
            quantidade_gerada++;
        }
    }
}

/*
 * Verifica se um número está dentro do intervalo permitido.
 *
 * Recebe:
 * - valor: número que vai ser verificado.
 *
 * Devolve:
 * - 1 se o número estiver entre VALOR_MINIMO e VALOR_MAXIMO.
 * - 0 se estiver fora desse intervalo.
 */
int valor_esta_no_intervalo(int valor)
{
    return valor >= VALOR_MINIMO && valor <= VALOR_MAXIMO;
}

/*
 * Verifica se todos os valores de uma tentativa estão dentro do intervalo.
 *
 * Recebe:
 * - valores: array com 4 números.
 *
 * Devolve:
 * - 1 se todos os números estiverem entre 1 e 6.
 * - 0 se pelo menos um número estiver fora do intervalo.
 */
int valores_estao_no_intervalo(const int valores[])
{
    int i;

    for (i = 0; i < TAMANHO_CODIGO; i++) {
        if (!valor_esta_no_intervalo(valores[i])) {
            return 0;
        }
    }

    return 1;
}

/*
 * Verifica se existem números repetidos num array.
 *
 * Recebe:
 * - valores: array com 4 números.
 *
 * Devolve:
 * - 1 se existir pelo menos um número repetido.
 * - 0 se todos os números forem diferentes.
 */
int tem_valores_repetidos(const int valores[])
{
    int i;
    int j;

    /*
     * Compara cada valor com os valores que aparecem depois dele.
     * Assim, cada par de posições é comparado apenas uma vez.
     */
    for (i = 0; i < TAMANHO_CODIGO - 1; i++) {
        for (j = i + 1; j < TAMANHO_CODIGO; j++) {
            if (valores[i] == valores[j]) {
                return 1;
            }
        }
    }

    return 0;
}

/*
 * Valida uma tentativa do jogador.
 *
 * Recebe:
 * - tentativa: array com os 4 números introduzidos.
 *
 * Devolve:
 * - VALIDACAO_OK se a tentativa for válida.
 * - VALIDACAO_FORA_INTERVALO se algum número não estiver entre 1 e 6.
 * - VALIDACAO_NUMEROS_REPETIDOS se existir algum número repetido.
 */
int validar_tentativa(const int tentativa[])
{
    if (!valores_estao_no_intervalo(tentativa)) {
        return VALIDACAO_FORA_INTERVALO;
    }

    if (tem_valores_repetidos(tentativa)) {
        return VALIDACAO_NUMEROS_REPETIDOS;
    }

    return VALIDACAO_OK;
}

/*
 * Verifica se um caractere deve ser tratado como espaço.
 *
 * Recebe:
 * - caractere: caractere que vai ser analisado.
 *
 * Devolve:
 * - 1 se for espaço, mudança de linha ou tabulação.
 * - 0 caso contrário.
 */
int caractere_e_espaco(char caractere)
{
    return caractere == ' ' || caractere == '\n' || caractere == '\t' || caractere == '\r';
}

/*
 * Verifica se uma linha tem apenas o número 0.
 *
 * Recebe:
 * - linha: texto escrito pelo jogador.
 *
 * Devolve:
 * - 1 se a linha tiver apenas o número 0.
 * - 0 caso contrário.
 */
int linha_tem_apenas_zero(const char linha[])
{
    int i = 0;

    while (caractere_e_espaco(linha[i])) {
        i++;
    }

    if (linha[i] != '0') {
        return 0;
    }

    i++;

    while (caractere_e_espaco(linha[i])) {
        i++;
    }

    return linha[i] == '\0';
}

/*
 * Tenta ler uma tentativa escrita com 4 dígitos.
 *
 * Recebe:
 * - linha: texto escrito pelo jogador.
 * - tentativa: array onde os dígitos vão ser guardados.
 *
 * Devolve:
 * - 1 se conseguir ler exatamente 4 dígitos.
 * - 0 se a linha tiver letras, símbolos ou uma quantidade errada de dígitos.
 *
 * Esta função permite aceitar entradas como 1256, além do formato 1 2 5 6.
 */
int ler_tentativa_por_digitos(const char linha[], int tentativa[])
{
    int i = 0;
    int quantidade_lida = 0;

    while (linha[i] != '\0') {
        if (caractere_e_espaco(linha[i])) {
            i++;
        } else if (linha[i] >= '0' && linha[i] <= '9') {
            if (quantidade_lida >= TAMANHO_CODIGO) {
                return 0;
            }

            tentativa[quantidade_lida] = linha[i] - '0';
            quantidade_lida++;
            i++;
        } else {
            return 0;
        }
    }

    return quantidade_lida == TAMANHO_CODIGO;
}

/*
 * Escolhe a mensagem certa para um resultado de validação.
 *
 * Recebe:
 * - resultado: número que representa o resultado da validação.
 *
 * Devolve:
 * - uma mensagem de texto constante.
 */
const char *mensagem_validacao(int resultado)
{
    if (resultado == VALIDACAO_ERRO_LEITURA) {
        return "Tentativa invalida: escreve exatamente 4 numeros, separados por espacos ou juntos.";
    }

    if (resultado == VALIDACAO_FIM_ENTRADA) {
        return "Entrada terminada.";
    }

    if (resultado == VALIDACAO_FORA_INTERVALO) {
        return "Tentativa invalida: todos os numeros devem estar entre 1 e 6.";
    }

    if (resultado == VALIDACAO_NUMEROS_REPETIDOS) {
        return "Tentativa invalida: nao podes repetir numeros.";
    }

    if (resultado == VALIDACAO_DESISTENCIA) {
        return "Desistencia.";
    }

    return "Tentativa valida.";
}

/*
 * Inicializa uma nova partida.
 *
 * Recebe:
 * - jogo: apontador para a struct Jogo que deve ser preparada.
 *
 * Devolve: nada.
 *
 * Esta função recebe um apontador porque precisa de alterar a struct original
 * criada na função main.
 */
void inicializar_jogo(Jogo *jogo)
{
    int i;
    int j;

    if (jogo == NULL) {
        return;
    }

    criar_codigo_secreto(jogo->codigo_secreto);
    jogo->tentativas_usadas = 0;
    jogo->estado = ESTADO_EM_CURSO;

    /*
     * Coloca o histórico a zero.
     * Isto deixa a partida num estado inicial limpo e previsível.
     */
    for (i = 0; i < MAX_TENTATIVAS; i++) {
        for (j = 0; j < TAMANHO_CODIGO; j++) {
            jogo->historico[i].valores[j] = 0;
        }

        jogo->historico[i].certos_posicao = 0;
        jogo->historico[i].certos_errada = 0;
    }
}

/*
 * Mostra o histórico de tentativas válidas.
 *
 * Recebe:
 * - jogo: apontador para consultar os dados da partida.
 *
 * Devolve: nada.
 */
void mostrar_historico(const Jogo *jogo)
{
    int i;

    if (jogo->tentativas_usadas == 0) {
        printf("Ainda nao existem tentativas validas.\n");
        return;
    }

    printf("\nHistorico:\n");

    for (i = 0; i < jogo->tentativas_usadas; i++) {
        printf("%2d) ", i + 1);
        mostrar_sequencia(jogo->historico[i].valores);
        printf(" -> posicao certa: %d, posicao errada: %d\n",
               jogo->historico[i].certos_posicao,
               jogo->historico[i].certos_errada);
    }
}

/*
 * Mostra o menu inicial.
 *
 * Recebe: nada.
 * Devolve: nada.
 */
void mostrar_menu_inicial(void)
{
    printf("\n==========================\n");
    printf("1 - Jogar\n");
    printf("2 - Regras\n");
    printf("0 - Sair\n");
}

/*
 * Mostra o estado atual da partida.
 *
 * Recebe:
 * - jogo: apontador para consultar o número de tentativas e o histórico.
 *
 * Devolve: nada.
 */
void mostrar_estado_partida(const Jogo *jogo)
{
    printf("\n==========================\n");
    printf("Tentativas usadas: %d/%d\n", jogo->tentativas_usadas, MAX_TENTATIVAS);
    mostrar_historico(jogo);
}

/*
 * Lê a opção escolhida no menu inicial.
 *
 * Recebe: nada.
 *
 * Devolve:
 * - a opção escrita pelo jogador, se for lida corretamente.
 * - OPCAO_INVALIDA se a entrada não for uma opção simples.
 * - OPCAO_FIM_ENTRADA se a entrada terminar inesperadamente.
 */
int ler_opcao(void)
{
    char linha[TAMANHO_LINHA];
    char extra;
    int opcao;
    int lidos;

    printf("Opcao: ");

    if (fgets(linha, TAMANHO_LINHA, stdin) == NULL) {
        return OPCAO_FIM_ENTRADA;
    }

    /*
     * Tenta ler um número inteiro.
     * A variável extra serve para detetar texto a mais depois da opção.
     */
    lidos = sscanf(linha, " %d %c", &opcao, &extra);

    if (lidos != 1) {
        return OPCAO_INVALIDA;
    }

    return opcao;
}

/*
 * Lê uma tentativa com 4 números ou a opção de desistir.
 *
 * Recebe:
 * - tentativa: array onde vão ser guardados os números lidos.
 *
 * Devolve:
 * - VALIDACAO_OK se a tentativa for lida e for válida.
 * - VALIDACAO_ERRO_LEITURA se não forem escritos exatamente 4 números.
 * - VALIDACAO_FIM_ENTRADA se a entrada terminar.
 * - VALIDACAO_DESISTENCIA se o jogador escrever apenas 0.
 * - outro resultado de validação se os números não cumprirem as regras.
 */
int ler_tentativa(int tentativa[])
{
    char linha[TAMANHO_LINHA];
    char extra;
    int lidos;

    printf("Escreve %d numeros entre %d e %d, sem repeticoes, separados por espacos ou juntos, ou 0 para desistir: ",
           TAMANHO_CODIGO,
           VALOR_MINIMO,
           VALOR_MAXIMO);

    if (fgets(linha, TAMANHO_LINHA, stdin) == NULL) {
        return VALIDACAO_FIM_ENTRADA;
    }

    if (linha_tem_apenas_zero(linha)) {
        return VALIDACAO_DESISTENCIA;
    }

    /*
     * Primeiro tenta ler o formato com espaços, por exemplo: 1 2 5 6.
     * Se esse formato não resultar, tenta ler o formato junto, por exemplo: 1256.
     */
    lidos = sscanf(linha,
                   " %d %d %d %d %c",
                   &tentativa[0],
                   &tentativa[1],
                   &tentativa[2],
                   &tentativa[3],
                   &extra);

    if (lidos == TAMANHO_CODIGO) {
        return validar_tentativa(tentativa);
    }

    if (ler_tentativa_por_digitos(linha, tentativa)) {
        return validar_tentativa(tentativa);
    }

    if (lidos != TAMANHO_CODIGO) {
        return VALIDACAO_ERRO_LEITURA;
    }

    return VALIDACAO_ERRO_LEITURA;
}

/*
 * Compara uma tentativa com o código secreto.
 *
 * Recebe:
 * - codigo_secreto: array com o código que o jogador tenta descobrir.
 * - tentativa: array com os números escritos pelo jogador.
 * - certos_posicao: apontador onde fica guardado o número de valores certos
 *   na posição certa.
 * - certos_errada: apontador onde fica guardado o número de valores certos
 *   na posição errada.
 *
 * Devolve: nada.
 *
 * A função usa apontadores porque precisa de alterar dois resultados.
 */
void comparar_tentativa(const int codigo_secreto[], const int tentativa[], int *certos_posicao, int *certos_errada)
{
    int i;

    if (certos_posicao == NULL || certos_errada == NULL) {
        return;
    }

    *certos_posicao = 0;
    *certos_errada = 0;

    /*
     * Como não existem números repetidos, cada número da tentativa só pode
     * corresponder a um número do código secreto.
     */
    for (i = 0; i < TAMANHO_CODIGO; i++) {
        if (tentativa[i] == codigo_secreto[i]) {
            (*certos_posicao)++;
        } else if (valor_existe_no_array(codigo_secreto, TAMANHO_CODIGO, tentativa[i])) {
            (*certos_errada)++;
        }
    }
}

/*
 * Guarda uma tentativa válida no histórico.
 *
 * Recebe:
 * - jogo: apontador para a struct Jogo.
 * - tentativa: array com a tentativa válida.
 * - certos_posicao: resultado dos valores certos na posição certa.
 * - certos_errada: resultado dos valores certos na posição errada.
 *
 * Devolve: nada.
 */
void guardar_tentativa(Jogo *jogo, const int tentativa[], int certos_posicao, int certos_errada)
{
    int posicao_historico;

    if (jogo == NULL || jogo->tentativas_usadas >= MAX_TENTATIVAS) {
        return;
    }

    posicao_historico = jogo->tentativas_usadas;

    copiar_valores(jogo->historico[posicao_historico].valores, tentativa);
    jogo->historico[posicao_historico].certos_posicao = certos_posicao;
    jogo->historico[posicao_historico].certos_errada = certos_errada;

    /*
     * O contador só aumenta depois de guardar uma tentativa válida.
     * Por isso, tentativas inválidas não gastam tentativas.
     */
    jogo->tentativas_usadas++;
}

/*
 * Mostra o resultado de uma tentativa.
 *
 * Recebe:
 * - certos_posicao: quantidade de números certos na posição certa.
 * - certos_errada: quantidade de números certos na posição errada.
 *
 * Devolve: nada.
 */
void mostrar_resultado_tentativa(int certos_posicao, int certos_errada)
{
    printf("Certos na posicao certa: %d\n", certos_posicao);
    printf("Certos na posicao errada: %d\n", certos_errada);
}

/*
 * Processa uma tentativa completa.
 *
 * Recebe:
 * - jogo: apontador para a partida atual.
 *
 * Devolve: nada.
 *
 * Esta função lê a tentativa, valida, compara, guarda no histórico e verifica
 * se o jogo terminou.
 */
void processar_tentativa(Jogo *jogo)
{
    int tentativa[TAMANHO_CODIGO];
    int certos_posicao;
    int certos_errada;
    int resultado_validacao;

    if (jogo == NULL) {
        return;
    }

    resultado_validacao = ler_tentativa(tentativa);

    if (resultado_validacao == VALIDACAO_FIM_ENTRADA) {
        printf("Entrada terminada. A partida vai ser encerrada.\n");
        jogo->estado = ESTADO_DESISTENCIA;
        return;
    }

    if (resultado_validacao == VALIDACAO_DESISTENCIA) {
        jogo->estado = ESTADO_DESISTENCIA;
        return;
    }

    if (resultado_validacao != VALIDACAO_OK) {
        printf("%s\n", mensagem_validacao(resultado_validacao));
        printf("A tentativa invalida nao foi contabilizada.\n");
        return;
    }

    comparar_tentativa(jogo->codigo_secreto, tentativa, &certos_posicao, &certos_errada);
    guardar_tentativa(jogo, tentativa, certos_posicao, certos_errada);
    mostrar_resultado_tentativa(certos_posicao, certos_errada);

    if (certos_posicao == TAMANHO_CODIGO) {
        jogo->estado = ESTADO_VITORIA;
    } else if (jogo->tentativas_usadas >= MAX_TENTATIVAS) {
        jogo->estado = ESTADO_DERROTA;
    }
}

/*
 * Mostra o resumo final da partida.
 *
 * Recebe:
 * - jogo: apontador para consultar os dados finais.
 *
 * Devolve: nada.
 */
void mostrar_resumo_final(const Jogo *jogo)
{
    printf("\n=== Fim do jogo ===\n");

    if (jogo->estado == ESTADO_VITORIA) {
        printf("Parabens! Descobriste o codigo em %d tentativa(s).\n", jogo->tentativas_usadas);
    } else if (jogo->estado == ESTADO_DERROTA) {
        printf("Perdeste. Usaste todas as %d tentativas.\n", MAX_TENTATIVAS);
    } else if (jogo->estado == ESTADO_DESISTENCIA) {
        printf("Desististe do jogo.\n");
    }

    printf("Codigo secreto: ");
    mostrar_sequencia(jogo->codigo_secreto);
    printf("\n");

    printf("\nResumo das tentativas validas:\n");
    mostrar_historico(jogo);
}

/*
 * Processa uma partida completa.
 *
 * Recebe: nada.
 * Devolve: nada.
 */
void jogar_partida(void)
{
    Jogo jogo;

    inicializar_jogo(&jogo);

    while (jogo.estado == ESTADO_EM_CURSO) {
        mostrar_estado_partida(&jogo);
        processar_tentativa(&jogo);
    }

    mostrar_resumo_final(&jogo);
}

/*
 * Função principal do programa.
 *
 * Recebe: nada.
 * Devolve: 0 quando o programa termina normalmente.
 *
 * A função main mostra a sequência principal do programa:
 * 1. preparar a geração de números aleatórios;
 * 2. mostrar o menu inicial;
 * 3. jogar, mostrar regras ou sair conforme a opção escolhida.
 */
int main(void)
{
    int opcao;
    int programa_ativo = 1;

    srand((unsigned int)time(NULL));
    mostrar_titulo();

    while (programa_ativo) {
        mostrar_menu_inicial();
        opcao = ler_opcao();

        if (opcao == OPCAO_JOGAR) {
            jogar_partida();
        } else if (opcao == OPCAO_REGRAS) {
            mostrar_regras();
        } else if (opcao == OPCAO_SAIR || opcao == OPCAO_FIM_ENTRADA) {
            programa_ativo = 0;
        } else {
            printf("Opcao invalida. Escolhe 1 para jogar, 2 para ver as regras ou 0 para sair.\n");
        }
    }

    printf("Programa terminado.\n");

    return 0;
}
