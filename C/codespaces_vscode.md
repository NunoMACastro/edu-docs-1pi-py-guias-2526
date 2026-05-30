![Header](../Images/Header.png)

# Guia rápido · Primeiro programa em C no GitHub Codespaces e no VS Code

> Objetivo: conseguir escrever, compilar e executar um programa muito simples em C.

---

## 1. Programa que vamos criar

Vamos criar um ficheiro chamado:

```txt
main.c
```

Com este conteúdo:

```c
#include <stdio.h>

int main(void) {
    printf("Ola, mundo!\n");
    return 0;
}
```

---

# Parte A · Usar no GitHub Codespaces

## 2. Abrir o Codespaces

1. Entrar no GitHub.
2. Abrir o repositório do projeto.
3. Clicar no botão **Code**.
4. Abrir o separador **Codespaces**.
5. Clicar em **Create codespace on main** ou clicar no codespace que já existe.

O GitHub vai abrir um ambiente de programação no browser.

---

## 3. Criar o ficheiro `main.c`

No explorador de ficheiros do Codespaces:

1. Clicar em **New File**.
2. Criar um ficheiro chamado:

```txt
main.c
```

3. Escrever o seguinte código:

```c
#include <stdio.h>

int main(void) {
    printf("Ola, mundo!\n");
    return 0;
}
```

4. Guardar o ficheiro.

---

## 4. Abrir o terminal

No Codespaces:

1. Ir ao menu **Terminal**.
2. Escolher **New Terminal**.

Vai aparecer uma zona no fundo da janela onde podemos escrever comandos.

---

## 5. Compilar o programa

No terminal, escrever:

```bash
gcc main.c -o programa
```

Este comando significa:

```txt
gcc       -> compilador de C
main.c    -> ficheiro com o código-fonte
-o        -> define o nome do programa gerado
programa  -> nome do programa compilado
```

Se não aparecer nenhum erro, significa que o programa compilou corretamente.

---

## 6. Executar o programa

Depois de compilar, escrever:

```bash
./programa
```

Deverá aparecer:

```txt
Ola, mundo!
```

---

## 7. Compilar e executar numa só linha

Também podemos fazer tudo numa única linha:

```bash
gcc main.c -o programa && ./programa
```

---

# Parte B · Usar no VS Code local

## 8. Abrir uma pasta no VS Code

1. Abrir o VS Code.
2. Criar uma pasta para o projeto, por exemplo:

```txt
projeto-c
```

3. No VS Code, escolher:

```txt
File > Open Folder
```

4. Abrir a pasta `projeto-c`.

---

## 9. Criar o ficheiro `main.c`

Dentro da pasta, criar um ficheiro chamado:

```txt
main.c
```

Escrever:

```c
#include <stdio.h>

int main(void) {
    printf("Ola, mundo!\n");
    return 0;
}
```

Guardar o ficheiro.

---

## 10. Abrir o terminal no VS Code

No VS Code:

```txt
Terminal > New Terminal
```

---

## 11. Confirmar se o compilador existe

No terminal, escrever:

```bash
gcc --version
```

Se aparecer informação sobre a versão do `gcc`, está tudo pronto.

Se aparecer uma mensagem a dizer que o comando não existe, então o compilador C ainda não está instalado no computador.

Nesse caso, usa o GitHub Codespaces ou pede ajuda ao professor para configurar o compilador no teu sistema operativo.

---

## 12. Compilar no VS Code

No terminal:

```bash
gcc main.c -o programa
```

---

## 13. Executar no VS Code

### Em Linux ou macOS

```bash
./programa
```

### Em Windows, dependendo do terminal

Pode ser:

```bash
./programa
```

ou:

```powershell
.\programa.exe
```

![Footer](../Images/Footer.png)
