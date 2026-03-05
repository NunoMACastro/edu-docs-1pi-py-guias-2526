# Guia Prático de Terminal e Consola (Windows, Linux e macOS)

> **Objetivo:**  
> Ensinar os comandos essenciais da linha de comandos, de forma simples e comparativa entre **Windows**, **Linux** e **macOS**.

---

## 1. Conceitos Fundamentais

| Termo                  | Explicação                                                             |
| ---------------------- | ---------------------------------------------------------------------- |
| **Terminal / Consola** | Janela onde escreves comandos de texto para controlar o sistema.       |
| **Shell**              | Programa que interpreta os comandos (ex.: CMD, PowerShell, Bash, Zsh). |
| **Diretório / Pasta**  | Local onde ficheiros e subpastas estão organizados.                    |
| **Caminho (path)**     | Endereço de uma pasta ou ficheiro.                                     |
| **Comando**            | Instrução executada no terminal (ex.: `cd`, `ls`, `mkdir`).            |

---

## 2. Que terminal usar em cada sistema

| Sistema Operativo | Ferramentas comuns                                          |
| ----------------- | ----------------------------------------------------------- |
| **Windows**       | `CMD` (Prompt de Comando), `PowerShell`, `Windows Terminal` |
| **Linux**         | `Terminal` com `Bash` (ou `Zsh`)                            |
| **macOS**         | `Terminal` com `Zsh` (padrão atual)                         |

> No dia a dia, **Linux e macOS** usam comandos muito semelhantes.

---

## 3. Navegação entre pastas (o mais importante)

| Tarefa                          | Windows (CMD/PowerShell)                           | Linux/macOS        |
| ------------------------------- | -------------------------------------------------- | ------------------ |
| Ver pasta atual                 | `cd`                                               | `pwd`              |
| Listar conteúdo da pasta        | `dir`                                              | `ls`               |
| Entrar numa pasta               | `cd nome_da_pasta`                                 | `cd nome_da_pasta` |
| Voltar uma pasta atrás          | `cd ..`                                            | `cd ..`            |
| Ir para a raiz do disco/sistema | `cd \`                                             | `cd /`             |
| Ir para a pasta pessoal         | `cd %USERPROFILE%` (CMD) / `cd $HOME` (PowerShell) | `cd ~`             |
| Limpar o ecrã                   | `cls`                                              | `clear`            |

Exemplo rápido:

```bash
cd Documentos
cd Projetos
cd ..
```

---

## 4. Criar, copiar, mover e apagar

| Tarefa               | Windows (CMD/PowerShell)                                               | Linux/macOS              |
| -------------------- | ---------------------------------------------------------------------- | ------------------------ |
| Criar pasta          | `mkdir nova_pasta`                                                     | `mkdir nova_pasta`       |
| Criar ficheiro vazio | `type nul > ficheiro.txt` (CMD) / `New-Item ficheiro.txt` (PowerShell) | `touch ficheiro.txt`     |
| Copiar ficheiro      | `copy a.txt b.txt` (CMD) / `Copy-Item a.txt b.txt`                     | `cp a.txt b.txt`         |
| Mover ficheiro       | `move a.txt pasta\` (CMD) / `Move-Item a.txt pasta\`                   | `mv a.txt pasta/`        |
| Renomear ficheiro    | `ren antigo.txt novo.txt` (CMD) / `Rename-Item`                        | `mv antigo.txt novo.txt` |
| Apagar ficheiro      | `del ficheiro.txt` / `Remove-Item ficheiro.txt`                        | `rm ficheiro.txt`        |
| Apagar pasta vazia   | `rmdir pasta`                                                          | `rmdir pasta`            |

> Atenção: comandos de remoção (`del`, `rm`, `Remove-Item`) podem apagar dados de forma permanente.

---

## 5. Caminhos: regras importantes

| Tema                  | Windows                    | Linux/macOS                                   |
| --------------------- | -------------------------- | --------------------------------------------- |
| Separador de pastas   | `\`                        | `/`                                           |
| Exemplo absoluto      | `C:\Users\Nuno\Desktop`    | `/home/nuno/Desktop` ou `/Users/nuno/Desktop` |
| Maiúsculas/minúsculas | Normalmente menos sensível | Sensível (`Ficheiro.txt` ≠ `ficheiro.txt`)    |

Se o nome da pasta tiver espaços, usa aspas:

```bash
cd "Primeiro Ano"
```

---

## 6. Comandos de ajuda

| Tarefa              | Windows      | Linux/macOS      |
| ------------------- | ------------ | ---------------- |
| Ajuda geral         | `help` (CMD) | `man`            |
| Ajuda de um comando | `comando /?` | `comando --help` |

Exemplos:

```bash
mkdir --help
ls --help
```

```powershell
Get-Help cd
```

---

## 7. Comandos úteis no estudo de programação

| Tarefa                       | Windows                                  | Linux/macOS           |
| ---------------------------- | ---------------------------------------- | --------------------- |
| Ver versão do Python         | `python --version` ou `py --version`     | `python3 --version`   |
| Executar programa Python     | `python programa.py` ou `py programa.py` | `python3 programa.py` |
| Abrir VS Code na pasta atual | `code .`                                 | `code .`              |

---

## 8. Fluxo recomendado para aulas

```text
1. Abrir o terminal
2. Ir para a pasta do projeto com cd
3. Listar ficheiros (dir / ls)
4. Executar o programa (python / python3)
5. Corrigir e repetir
```

---

## 9. Mini-Exercícios

1. Navega para uma pasta de trabalho e volta uma pasta atrás.
2. Cria uma pasta chamada `aula_terminal` e entra nela.
3. Cria um ficheiro chamado `notas.txt`.
4. Renomeia `notas.txt` para `comandos.txt`.
5. Lista o conteúdo da pasta para confirmar as alterações.

---

## 10. Resumo Rápido (Cheat Sheet)

```text
Navegar:
- cd nome_pasta
- cd ..
- cd / (Linux/macOS) | cd \ (Windows)

Listar:
- ls (Linux/macOS)
- dir (Windows)

Criar:
- mkdir pasta
- touch ficheiro.txt (Linux/macOS)

Apagar:
- rm ficheiro.txt (Linux/macOS)
- del ficheiro.txt (Windows)
```

---

## 11. Erros comuns (e como evitar)

- Esquecer aspas em nomes com espaços.
- Usar `\` em Linux/macOS (deve ser `/`).
- Apagar ficheiros sem confirmar primeiro o caminho.
- Tentar executar Python sem estar na pasta certa.

---

## 12. Ajuda extra

- Experimenta os comandos com calma numa pasta de teste.
- Usa `comando --help` ou `comando /?` sempre que tiveres dúvidas.
- Pratica os mesmos exercícios nos três sistemas para ganhar confiança.
