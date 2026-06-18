![Header](../Images/Header.png)

# Python + IA - Chatbot sobre PDF com modelo local e fallback para OpenAI

> **Objetivo deste ficheiro**  
> Construir uma pequena aplicação de consola onde um aluno pode fazer perguntas sobre um PDF.  
> O programa tenta primeiro encontrar uma resposta localmente. Se a confiança for baixa, usa a OpenAI API como fallback.

---

## 0) O que vais construir

Vais criar uma aplicação chamada **PDF Chatbot**.

A aplicação permite:

- pedir o caminho de um ficheiro PDF;
- extrair texto do PDF;
- dividir o texto em blocos pequenos;
- receber perguntas do utilizador;
- procurar os blocos mais relevantes do PDF;
- responder localmente quando a confiança é suficiente;
- usar a OpenAI API quando o modelo local não consegue responder bem;
- proteger a API key com um ficheiro `.env`.

Esta ficha usa Python básico, mas introduz ideias muito importantes de aplicações modernas com IA:

- APIs;
- chaves de API;
- modelos;
- confiança;
- fallback;
- variáveis de ambiente;
- segurança de secrets;
- extração de texto;
- pesquisa local;
- contexto enviado para um modelo.

---

## 1) Ideia principal da aplicação

O programa vai funcionar assim:

```text
PDF
 |
 v
Extrair texto
 |
 v
Dividir em blocos
 |
 v
Aluno faz pergunta
 |
 v
Modelo local procura blocos relevantes
 |
+-----------------------------+
|                             |
v                             v
Confiança alta                Confiança baixa
 |                             |
 v                             v
Resposta local                 OpenAI API responde usando excertos do PDF
```

O objetivo não é criar logo uma IA perfeita. O objetivo é perceber uma arquitetura simples:

1. usar primeiro uma solução local, barata e controlada;
2. medir se essa solução parece suficiente;
3. chamar uma API externa apenas quando for necessário.

---

## 2) Vocabulário essencial

### O que é uma API?

Uma **API** é uma forma de um programa falar com outro programa.

Exemplo simples:

- o teu programa Python envia uma pergunta para um serviço externo;
- esse serviço processa o pedido;
- o serviço devolve uma resposta.

No nosso caso, a OpenAI API recebe texto e devolve uma resposta gerada por um modelo.

Uma API é como uma porta de entrada controlada. Não precisas de saber como o serviço funciona por dentro, mas tens de respeitar as regras de entrada:

- que dados enviar;
- que formato usar;
- como autenticar;
- como tratar erros.

---

### O que é uma chave de API?

Uma **chave de API** é uma credencial secreta que identifica quem está a usar a API.

Pensa nela como uma password para o teu programa.

Por isso:

- não deve aparecer no código;
- não deve ser partilhada com colegas;
- não deve ser enviada para GitHub;
- deve ficar em variáveis de ambiente ou num ficheiro `.env` local.

Errado:

```python
client = OpenAI(api_key="sk-...")
```

Certo:

```python
client = OpenAI()
```

O cliente da OpenAI consegue ler automaticamente a variável `OPENAI_API_KEY` a partir do ambiente.

---

### O que é um modelo?

Um **modelo** é um sistema que recebe uma entrada e produz uma saída.

Nesta ficha vamos usar dois tipos de modelo:

1. **Modelo local simples**
    - feito por nós em Python;
    - compara palavras da pergunta com palavras dos blocos do PDF;
    - devolve os excertos mais relevantes;
    - não precisa de internet;
    - não tem custo por utilização.

2. **Modelo da OpenAI**
    - chamado através da API;
    - consegue escrever respostas mais naturais;
    - recebe a pergunta e alguns excertos do PDF;
    - deve responder apenas com base nesses excertos.

O modelo local é mais simples, mas é útil. Ele faz a primeira triagem.

---

### Como funciona o nosso modelo local?

O nosso modelo local não "compreende" o texto como uma pessoa. Ele faz uma aproximação:

1. transforma a pergunta em palavras importantes;
2. transforma cada bloco do PDF em palavras;
3. conta quantas palavras da pergunta aparecem em cada bloco;
4. calcula uma pontuação;
5. escolhe os blocos com melhor pontuação.

Exemplo:

Pergunta:

```text
O que é uma variável de ambiente?
```

Palavras úteis:

```text
variável, ambiente
```

Se um bloco do PDF contém essas palavras, provavelmente é relevante.

Limitação: se o PDF disser "configuração externa" em vez de "variável de ambiente", o modelo local pode não perceber que o significado é parecido. Essa é uma das razões para existir fallback.

---

### O que é confiança?

**Confiança** é um valor que indica o quão seguro o programa está de que encontrou uma boa resposta.

Nesta ficha, a confiança local é calculada assim:

```text
número de palavras importantes encontradas / número total de palavras importantes da pergunta
```

Exemplo:

- pergunta tem 4 palavras importantes;
- um bloco contém 2 dessas palavras;
- confiança = `2 / 4 = 0.50`.

Se a confiança for alta, o programa mostra uma resposta local.

Se a confiança for baixa, o programa chama a OpenAI API.

> Atenção: esta confiança é uma métrica simples. Não prova que a resposta está correta. Apenas indica que o bloco parece relevante.

---

### O que são variáveis de ambiente?

**Variáveis de ambiente** são valores guardados fora do código, mas que o programa consegue ler.

Servem para guardar configurações que podem mudar entre computadores:

- API keys;
- nomes de modelos;
- URLs;
- passwords;
- modo de execução.

Exemplo:

```env
OPENAI_API_KEY=coloca_a_tua_chave_aqui
OPENAI_MODEL=gpt-5.5
```

No Python:

```python
import os

model = os.getenv("OPENAI_MODEL")
```

---

### O que é um ficheiro `.env`?

Um ficheiro `.env` guarda variáveis de ambiente para desenvolvimento local.

Exemplo de `.env`:

```env
OPENAI_API_KEY=coloca_a_tua_chave_aqui
OPENAI_MODEL=gpt-5.5
```

O ficheiro `.env` deve ficar no computador do aluno, mas não deve ir para o Git.

Por isso criamos também um `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
```

E podemos criar um `.env.example`, que pode ir para GitHub porque não tem secrets reais:

```env
OPENAI_API_KEY=coloca_a_tua_chave_aqui
OPENAI_MODEL=gpt-5.5
```

---

### O que é fallback?

**Fallback** é um plano B.

Nesta aplicação:

- plano A: tentar responder localmente;
- plano B: chamar a OpenAI API.

Isto é útil porque:

- reduz chamadas à API;
- reduz custos;
- torna a app mais rápida quando a resposta local chega;
- permite que parte da app funcione mesmo sem internet;
- ensina uma arquitetura comum em sistemas reais.

---

### O que é contexto?

Um modelo de linguagem responde melhor quando recebe contexto relevante.

Em vez de enviar o PDF inteiro para a API, vamos enviar apenas os blocos mais relevantes.

Isto tem vantagens:

- menos texto enviado;
- menor custo;
- resposta mais focada;
- menos risco de o modelo inventar;
- maior controlo sobre a fonte da resposta.

---

### O que são alucinações?

Em IA, uma **alucinação** acontece quando o modelo responde algo que parece correto, mas não está apoiado nos dados fornecidos.

Para reduzir esse risco, vamos dizer ao modelo:

```text
Usa apenas o contexto retirado do PDF.
Se a resposta não estiver no contexto, diz que não encontraste informação suficiente.
```

Esta instrução não é uma garantia perfeita, mas melhora o comportamento.

---

## 3) Competências trabalhadas

Nesta ficha vais praticar:

1. organização de projeto Python;
2. leitura de ficheiros;
3. uso de bibliotecas externas;
4. criação de funções com responsabilidades claras;
5. extração de texto de PDFs;
6. divisão de texto em blocos;
7. normalização de texto;
8. cálculo de pontuações simples;
9. uso de variáveis de ambiente;
10. integração com uma API externa;
11. tratamento de erros;
12. pensamento crítico sobre IA.

---

## 4) Pré-requisitos

Precisas de:

- Python 3.10 ou superior;
- acesso ao terminal;
- um PDF com texto selecionável;
- uma API key da OpenAI para testar o fallback.

Verifica a versão do Python:

```bash
python --version
```

Em alguns computadores, o comando pode ser:

```bash
python3 --version
```

---

## 5) Criar o projeto

Cria uma pasta:

```bash
mkdir pdf-chatbot
cd pdf-chatbot
```

Cria um ambiente virtual:

```bash
python -m venv .venv
```

Ativa o ambiente virtual.

No macOS/Linux:

```bash
source .venv/bin/activate
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 6) Estrutura final do projeto

No fim, a pasta deve ficar assim:

```text
pdf-chatbot/
├─ .env
├─ .env.example
├─ .gitignore
├─ requirements.txt
└─ pdf_chatbot.py
```

---

## 7) Dependências

Cria o ficheiro `requirements.txt`:

```txt
openai
python-dotenv
pypdf
```

Instala:

```bash
pip install -r requirements.txt
```

Para que servem estas bibliotecas?

- `openai`: permite chamar a OpenAI API;
- `python-dotenv`: carrega variáveis do ficheiro `.env`;
- `pypdf`: lê ficheiros PDF e tenta extrair texto.

---

## 8) Configuração segura

Cria o ficheiro `.env`:

```env
OPENAI_API_KEY=coloca_a_tua_chave_aqui
OPENAI_MODEL=gpt-5.5
```

Cria o ficheiro `.env.example`:

```env
OPENAI_API_KEY=coloca_a_tua_chave_aqui
OPENAI_MODEL=gpt-5.5
```

Cria o ficheiro `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

**Checkpoint**

- Existe um `.env`.
- Existe um `.env.example`.
- O `.env` está no `.gitignore`.
- A chave real não aparece em nenhum ficheiro que possa ser entregue ou publicado.

---

## 9) Fase 1 - Esqueleto da aplicação

Ideia desta fase:

- criar o ficheiro principal;
- confirmar que o programa corre.

Cria `pdf_chatbot.py`:

```python
"""
PDF Chatbot.

Esta aplicação permite fazer perguntas sobre um PDF.
Primeiro tenta responder localmente.
Se a confiança local for baixa, usa a OpenAI API como fallback.
"""


def main():
    """
    Executa o programa principal.

    Nesta primeira fase apenas confirma que o ficheiro corre.
    """
    print("PDF Chatbot")
    print("Aplicação pronta para começar.")


if __name__ == "__main__":
    main()
```

Corre:

```bash
python pdf_chatbot.py
```

**Checkpoint A**

- O terminal mostra `PDF Chatbot`.
- Não há erros.

---

## 10) Fase 2 - Ler texto de um PDF

Ideia desta fase:

- usar `pypdf`;
- receber o caminho de um PDF;
- extrair texto.

Substitui `pdf_chatbot.py` por:

```python
"""
PDF Chatbot.

Nesta fase o programa lê um PDF e mostra uma pequena amostra do texto extraído.
"""

from pathlib import Path

from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extrai texto de um ficheiro PDF.

    Args:
        pdf_path: caminho para o ficheiro PDF.

    Returns:
        Uma string com o texto extraído de todas as páginas.

    Raises:
        FileNotFoundError: se o ficheiro não existir.
    """
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"O ficheiro não existe: {pdf_path}")

    reader = PdfReader(str(path))
    pages_text = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            pages_text.append(f"[Página {page_number}]\n{text.strip()}")

    return "\n\n".join(pages_text)


def main():
    """
    Pede um PDF ao utilizador e mostra uma amostra do texto.
    """
    pdf_path = input("Caminho do PDF: ").strip()

    try:
        text = extract_text_from_pdf(pdf_path)
    except FileNotFoundError as error:
        print(error)
        return

    if not text.strip():
        print("Não foi possível extrair texto deste PDF.")
        print("Talvez seja um PDF digitalizado como imagem.")
        return

    print("\nTexto extraído com sucesso.")
    print("\nAmostra:")
    print(text[:1000])


if __name__ == "__main__":
    main()
```

**Checkpoint B**

- O programa pede o caminho do PDF.
- Se o PDF existir, mostra uma amostra do texto.
- Se o PDF não existir, mostra uma mensagem de erro.

---

## 11) Fase 3 - Dividir o texto em blocos

Ideia desta fase:

- um PDF pode ter muito texto;
- vamos dividir o texto em blocos mais pequenos;
- cada bloco será analisado pelo modelo local.

Acrescenta estas constantes:

```python
CHUNK_SIZE = 900
CHUNK_OVERLAP = 150
```

Acrescenta esta função:

```python
def split_text_into_chunks(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """
    Divide texto em blocos com alguma sobreposição.

    Args:
        text: texto completo do PDF.
        chunk_size: tamanho máximo aproximado de cada bloco.
        overlap: número de caracteres repetidos entre blocos.

    Returns:
        Uma lista de blocos de texto.
    """
    if chunk_size <= overlap:
        raise ValueError("chunk_size deve ser maior do que overlap.")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - overlap

    return chunks
```

No `main`, depois de extrair o texto:

```python
chunks = split_text_into_chunks(text)

print(f"\nPDF dividido em {len(chunks)} blocos.")
print("\nPrimeiro bloco:")
print(chunks[0][:700])
```

**Checkpoint C**

- O programa mostra quantos blocos foram criados.
- O primeiro bloco aparece no terminal.

---

## 12) Fase 4 - Normalizar texto

Ideia desta fase:

- para comparar pergunta e PDF, precisamos de limpar o texto;
- vamos colocar tudo em minúsculas;
- vamos separar palavras;
- vamos ignorar palavras muito comuns.

Acrescenta estes imports:

```python
import re
```

Acrescenta esta constante:

```python
STOP_WORDS = {
    "a", "as", "ao", "aos", "o", "os", "um", "uma", "uns", "umas",
    "de", "da", "das", "do", "dos", "em", "no", "na", "nos", "nas",
    "por", "para", "com", "sem", "que", "se", "e", "ou", "é", "são",
    "como", "qual", "quais", "porque", "isto", "isso", "este", "esta",
}
```

Acrescenta esta função:

```python
def normalize_words(text):
    """
    Converte texto numa lista de palavras úteis.

    Args:
        text: texto original.

    Returns:
        Lista de palavras normalizadas.
    """
    words = re.findall(r"[a-zA-ZÀ-ÿ0-9]+", text.lower())

    useful_words = []

    for word in words:
        if len(word) > 2 and word not in STOP_WORDS:
            useful_words.append(word)

    return useful_words
```

Testa temporariamente no `main`:

```python
question = input("\nEscreve uma pergunta de teste: ").strip()
print(normalize_words(question))
```

**Checkpoint D**

- A pergunta é transformada numa lista de palavras.
- Palavras muito comuns são removidas.

---

## 13) Fase 5 - Calcular confiança local

Ideia desta fase:

- comparar a pergunta com cada bloco;
- calcular uma pontuação;
- ordenar os blocos por relevância.

Acrescenta:

```python
TOP_CHUNKS = 3
```

Acrescenta estas funções:

```python
def score_chunk(question, chunk):
    """
    Calcula uma pontuação de relevância entre uma pergunta e um bloco.

    Args:
        question: pergunta feita pelo utilizador.
        chunk: bloco de texto retirado do PDF.

    Returns:
        Um número entre 0 e 1.
    """
    question_words = set(normalize_words(question))
    chunk_words = set(normalize_words(chunk))

    if not question_words:
        return 0

    matches = question_words.intersection(chunk_words)
    return len(matches) / len(question_words)


def find_relevant_chunks(question, chunks, top_n=TOP_CHUNKS):
    """
    Encontra os blocos mais relevantes para uma pergunta.

    Args:
        question: pergunta feita pelo utilizador.
        chunks: lista de blocos do PDF.
        top_n: número de blocos a devolver.

    Returns:
        Lista de tuplos no formato (pontuação, bloco).
    """
    scored_chunks = []

    for chunk in chunks:
        score = score_chunk(question, chunk)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda item: item[0])

    return scored_chunks[:top_n]
```

Testa no `main`:

```python
question = input("\nPergunta de teste: ").strip()
relevant_chunks = find_relevant_chunks(question, chunks)

for score, chunk in relevant_chunks:
    print("\n---")
    print(f"Pontuação: {score:.2f}")
    print(chunk[:500])
```

**Checkpoint E**

- O programa mostra os blocos mais relevantes.
- Cada bloco tem uma pontuação.

---

## 14) Fase 6 - Resposta local

Ideia desta fase:

- se a confiança for suficiente, respondemos sem API;
- a resposta local será um excerto do PDF.

Acrescenta:

```python
LOCAL_CONFIDENCE_THRESHOLD = 0.30
```

Acrescenta esta função:

```python
def build_local_answer(question, chunks):
    """
    Tenta criar uma resposta local a partir do PDF.

    Args:
        question: pergunta feita pelo utilizador.
        chunks: lista de blocos do PDF.

    Returns:
        Uma tupla com:
        - resposta local ou None;
        - confiança do melhor bloco;
        - blocos relevantes encontrados.
    """
    relevant_chunks = find_relevant_chunks(question, chunks)

    if not relevant_chunks:
        return None, 0, []

    best_score, best_chunk = relevant_chunks[0]

    if best_score >= LOCAL_CONFIDENCE_THRESHOLD:
        answer = (
            "Encontrei este excerto relevante no PDF:\n\n"
            f"{best_chunk[:900]}"
        )
        return answer, best_score, relevant_chunks

    return None, best_score, relevant_chunks
```

**Checkpoint F**

- Perguntas com palavras que existem no PDF devolvem excertos.
- Perguntas sem correspondência suficiente devolvem `None`.

---

## 15) Fase 7 - Fallback com OpenAI API

Ideia desta fase:

- carregar `.env`;
- criar cliente OpenAI;
- enviar pergunta e excertos relevantes;
- pedir ao modelo para responder apenas com base no PDF.

Acrescenta os imports:

```python
import os

from dotenv import load_dotenv
from openai import OpenAI
```

Acrescenta esta função:

```python
def ask_openai(client, model, question, relevant_chunks):
    """
    Usa a OpenAI API para responder com base nos excertos do PDF.

    Args:
        client: cliente da OpenAI API.
        model: nome do modelo configurado.
        question: pergunta feita pelo utilizador.
        relevant_chunks: blocos mais relevantes encontrados localmente.

    Returns:
        Texto da resposta gerada pela API.
    """
    context_parts = []

    for score, chunk in relevant_chunks:
        if score > 0:
            context_parts.append(chunk)

    context = "\n\n---\n\n".join(context_parts)

    if not context.strip():
        context = "Não foram encontrados excertos claramente relevantes no PDF."

    response = client.responses.create(
        model=model,
        instructions=(
            "Responde em português de Portugal. "
            "Usa apenas o contexto retirado do PDF. "
            "Se a resposta não estiver no contexto, diz que não encontraste "
            "informação suficiente no PDF."
        ),
        input=(
            f"Contexto retirado do PDF:\n{context}\n\n"
            f"Pergunta do aluno:\n{question}"
        ),
    )

    return response.output_text.strip()
```

No início do `main`, carrega o `.env`:

```python
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-5.5")
client = OpenAI() if api_key else None
```

**Checkpoint G**

- Se existir API key, o programa consegue chamar a OpenAI API.
- Se não existir API key, a app deve continuar a conseguir usar respostas locais.

---

## 16) Fase 8 - Ciclo de perguntas

Ideia desta fase:

- manter o programa aberto;
- permitir várias perguntas sobre o mesmo PDF;
- sair com `sair`, `exit` ou `quit`.

No `main`, depois de carregar os blocos:

```python
print("\nPDF carregado.")
print("Escreve 'sair' para terminar.\n")

while True:
    question = input("Aluno: ").strip()

    if question.lower() in {"sair", "exit", "quit"}:
        print("Bot: Até já!")
        break

    if not question:
        continue

    answer, confidence, relevant_chunks = build_local_answer(question, chunks)

    if answer is not None:
        print(f"\nBot: {answer}")
        print(f"[fonte: local | confiança: {confidence:.2f}]\n")
        continue

    if client is None:
        print("\nBot: Não tenho confiança suficiente para responder localmente.")
        print("Também não existe OPENAI_API_KEY configurada para usar fallback.\n")
        continue

    try:
        answer = ask_openai(client, model, question, relevant_chunks)
    except Exception as error:
        print(f"\nErro ao chamar a OpenAI API: {error}\n")
        continue

    print(f"\nBot: {answer}")
    print(f"[fonte: OpenAI API | confiança local: {confidence:.2f}]\n")
```

**Checkpoint H**

- A app aceita várias perguntas.
- Mostra se a resposta veio do modelo local ou da API.
- Sai corretamente quando o utilizador escreve `sair`.

---

## 17) Versão final sugerida - `pdf_chatbot.py`

Esta é uma versão completa e organizada do ficheiro principal.

```python
"""
PDF Chatbot.

Aplicação de consola que permite fazer perguntas sobre um PDF.

Fluxo principal:
1. extrai texto de um PDF;
2. divide o texto em blocos;
3. tenta encontrar uma resposta local através de correspondência de palavras;
4. se a confiança local for baixa, usa a OpenAI API como fallback.
"""

import os
import re
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader


CHUNK_SIZE = 900
CHUNK_OVERLAP = 150
TOP_CHUNKS = 3
LOCAL_CONFIDENCE_THRESHOLD = 0.30

STOP_WORDS = {
    "a", "as", "ao", "aos", "o", "os", "um", "uma", "uns", "umas",
    "de", "da", "das", "do", "dos", "em", "no", "na", "nos", "nas",
    "por", "para", "com", "sem", "que", "se", "e", "ou", "é", "são",
    "como", "qual", "quais", "porque", "isto", "isso", "este", "esta",
}


def extract_text_from_pdf(pdf_path):
    """
    Extrai texto de um ficheiro PDF.

    Args:
        pdf_path: caminho para o ficheiro PDF.

    Returns:
        Texto extraído de todas as páginas que tenham conteúdo legível.

    Raises:
        FileNotFoundError: se o caminho indicado não existir.
    """
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"O ficheiro não existe: {pdf_path}")

    reader = PdfReader(str(path))
    pages_text = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            pages_text.append(f"[Página {page_number}]\n{text.strip()}")

    return "\n\n".join(pages_text)


def split_text_into_chunks(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """
    Divide texto em blocos com alguma sobreposição.

    Args:
        text: texto completo do PDF.
        chunk_size: tamanho máximo aproximado de cada bloco.
        overlap: número de caracteres repetidos entre blocos.

    Returns:
        Lista de blocos de texto.
    """
    if chunk_size <= overlap:
        raise ValueError("chunk_size deve ser maior do que overlap.")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start = end - overlap

    return chunks


def normalize_words(text):
    """
    Converte texto numa lista de palavras úteis.

    Args:
        text: texto original.

    Returns:
        Lista de palavras normalizadas.
    """
    words = re.findall(r"[a-zA-ZÀ-ÿ0-9]+", text.lower())
    useful_words = []

    for word in words:
        if len(word) > 2 and word not in STOP_WORDS:
            useful_words.append(word)

    return useful_words


def score_chunk(question, chunk):
    """
    Calcula uma pontuação de relevância entre uma pergunta e um bloco.

    Args:
        question: pergunta feita pelo utilizador.
        chunk: bloco de texto retirado do PDF.

    Returns:
        Número entre 0 e 1.
    """
    question_words = set(normalize_words(question))
    chunk_words = set(normalize_words(chunk))

    if not question_words:
        return 0

    matches = question_words.intersection(chunk_words)
    return len(matches) / len(question_words)


def find_relevant_chunks(question, chunks, top_n=TOP_CHUNKS):
    """
    Encontra os blocos mais relevantes para uma pergunta.

    Args:
        question: pergunta feita pelo utilizador.
        chunks: lista de blocos do PDF.
        top_n: número de blocos a devolver.

    Returns:
        Lista de tuplos no formato (pontuação, bloco).
    """
    scored_chunks = []

    for chunk in chunks:
        score = score_chunk(question, chunk)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda item: item[0])

    return scored_chunks[:top_n]


def build_local_answer(question, chunks):
    """
    Tenta criar uma resposta local a partir do PDF.

    Args:
        question: pergunta feita pelo utilizador.
        chunks: lista de blocos do PDF.

    Returns:
        Tupla com resposta local ou None, confiança e blocos relevantes.
    """
    relevant_chunks = find_relevant_chunks(question, chunks)

    if not relevant_chunks:
        return None, 0, []

    best_score, best_chunk = relevant_chunks[0]

    if best_score >= LOCAL_CONFIDENCE_THRESHOLD:
        answer = (
            "Encontrei este excerto relevante no PDF:\n\n"
            f"{best_chunk[:900]}"
        )
        return answer, best_score, relevant_chunks

    return None, best_score, relevant_chunks


def ask_openai(client, model, question, relevant_chunks):
    """
    Usa a OpenAI API para responder com base nos excertos do PDF.

    Args:
        client: cliente da OpenAI API.
        model: nome do modelo configurado.
        question: pergunta feita pelo utilizador.
        relevant_chunks: blocos mais relevantes encontrados localmente.

    Returns:
        Texto da resposta gerada pela API.
    """
    context_parts = []

    for score, chunk in relevant_chunks:
        if score > 0:
            context_parts.append(chunk)

    context = "\n\n---\n\n".join(context_parts)

    if not context.strip():
        context = "Não foram encontrados excertos claramente relevantes no PDF."

    response = client.responses.create(
        model=model,
        instructions=(
            "Responde em português de Portugal. "
            "Usa apenas o contexto retirado do PDF. "
            "Se a resposta não estiver no contexto, diz que não encontraste "
            "informação suficiente no PDF."
        ),
        input=(
            f"Contexto retirado do PDF:\n{context}\n\n"
            f"Pergunta do aluno:\n{question}"
        ),
    )

    return response.output_text.strip()


def main():
    """
    Executa o ciclo principal da aplicação.
    """
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-5.5")
    client = OpenAI() if api_key else None

    print("PDF Chatbot")
    print("Faz perguntas sobre um PDF.")

    if client is None:
        print("\nAviso: OPENAI_API_KEY não está configurada.")
        print("A aplicação só conseguirá responder localmente.\n")

    pdf_path = input("Caminho do PDF: ").strip()

    try:
        pdf_text = extract_text_from_pdf(pdf_path)
    except FileNotFoundError as error:
        print(error)
        return

    if not pdf_text.strip():
        print("Não foi possível extrair texto deste PDF.")
        print("Talvez seja um PDF digitalizado como imagem.")
        return

    chunks = split_text_into_chunks(pdf_text)

    print(f"\nPDF carregado com {len(chunks)} blocos.")
    print("Escreve 'sair' para terminar.\n")

    while True:
        question = input("Aluno: ").strip()

        if question.lower() in {"sair", "exit", "quit"}:
            print("Bot: Até já!")
            break

        if not question:
            continue

        answer, confidence, relevant_chunks = build_local_answer(question, chunks)

        if answer is not None:
            print(f"\nBot: {answer}")
            print(f"[fonte: local | confiança: {confidence:.2f}]\n")
            continue

        if client is None:
            print("\nBot: Não tenho confiança suficiente para responder localmente.")
            print("Também não existe OPENAI_API_KEY configurada para usar fallback.\n")
            continue

        try:
            answer = ask_openai(client, model, question, relevant_chunks)
        except Exception as error:
            print(f"\nErro ao chamar a OpenAI API: {error}\n")
            continue

        print(f"\nBot: {answer}")
        print(f"[fonte: OpenAI API | confiança local: {confidence:.2f}]\n")


if __name__ == "__main__":
    main()
```

---

## 18) Critérios de aceitação obrigatórios

O trabalho está completo quando:

1. o projeto tem `requirements.txt`;
2. o projeto tem `.env.example`;
3. o `.env` não é entregue com a chave real;
4. o programa lê um PDF indicado pelo utilizador;
5. o programa divide o texto em blocos;
6. o programa aceita várias perguntas;
7. o programa mostra a fonte da resposta: local ou OpenAI API;
8. o programa não crasha se o PDF não existir;
9. o programa avisa quando não consegue extrair texto;
10. as funções principais têm docstrings claras.

---

## 19) Erros comuns e correções

### `ModuleNotFoundError: No module named 'pypdf'`

Provavelmente as dependências não foram instaladas.

Corre:

```bash
pip install -r requirements.txt
```

---

### `ModuleNotFoundError: No module named 'dotenv'`

A biblioteca chama-se `python-dotenv`, mas no código importamos `dotenv`.

Confirma que o `requirements.txt` tem:

```txt
python-dotenv
```

---

### A API key não funciona

Verifica:

- o ficheiro chama-se exatamente `.env`;
- a variável chama-se exatamente `OPENAI_API_KEY`;
- não há espaços antes ou depois do sinal `=`;
- o ambiente virtual está ativo;
- reiniciaste o terminal depois de criar o `.env`, se necessário.

---

### O PDF não extrai texto

Alguns PDFs são imagens digitalizadas.

Nesses casos, `pypdf` não consegue ler texto porque não existe texto real dentro do ficheiro.

Solução possível para uma versão futura:

- usar OCR;
- usar ferramentas como Tesseract;
- pedir outro PDF com texto selecionável.

---

### A resposta local parece fraca

Isto é esperado.

O modelo local desta ficha faz correspondência de palavras. Ele não entende sinónimos nem frases com significado parecido.

Exemplo:

- pergunta: "O que é uma credencial?"
- PDF: "Uma chave de API identifica o utilizador."

O modelo local pode não perceber que estes conceitos estão relacionados.

---

### A API responde fora do PDF

Confirma que a função `ask_openai` inclui esta instrução:

```text
Usa apenas o contexto retirado do PDF.
```

Mesmo assim, nenhum modelo é perfeito. Por isso é importante pedir respostas com base no contexto e, em projetos mais avançados, guardar citações ou páginas.

---

## 20) Desafios finais

Escolhe pelo menos dois:

1. Mostrar também a página do PDF de onde veio o excerto.
2. Permitir escolher outro PDF sem reiniciar o programa.
3. Guardar as perguntas e respostas num ficheiro `historico.txt`.
4. Criar um modo `--local-only` que nunca usa a API.
5. Criar um menu inicial com opções numeradas.
6. Melhorar as `STOP_WORDS` para português.
7. Permitir configurar `LOCAL_CONFIDENCE_THRESHOLD` no `.env`.
8. Mostrar os três excertos usados no fallback.
9. Impedir perguntas demasiado longas.
10. Criar uma pequena interface web com Flask.

---

## 21) Versão mais avançada: embeddings

Esta ficha usa pesquisa por palavras porque é mais simples.

Numa versão mais avançada, podíamos usar **embeddings**.

Um embedding transforma texto em números que representam significado.

Com embeddings, o programa conseguiria perceber melhor que estas frases estão relacionadas:

```text
O que é uma chave de API?
```

```text
Uma credencial permite autenticar pedidos a um serviço externo.
```

Mesmo sem palavras iguais, o significado é parecido.

Essa evolução chama-se frequentemente **RAG**:

```text
Retrieval-Augmented Generation
```

Ou seja:

1. procurar informação relevante;
2. passar essa informação ao modelo;
3. gerar uma resposta com base nela.

Nesta ficha já fizeste uma primeira versão simples dessa ideia.

---

## 22) Checklist de validação

Antes de entregar, confirma:

- [ ] O projeto corre com `python pdf_chatbot.py`.
- [ ] O PDF usado para teste tem texto extraível.
- [ ] O programa mostra quantos blocos foram criados.
- [ ] O programa responde localmente a perguntas simples.
- [ ] O programa usa a API quando a confiança local é baixa.
- [ ] O `.env` não é entregue com a chave real.
- [ ] O `.env.example` existe.
- [ ] O `.gitignore` contém `.env`.
- [ ] As funções têm docstrings.
- [ ] O código está organizado e legível.

---

## 23) Perguntas de revisão

1. O que é uma API?
2. Porque é que uma API key não deve ser escrita diretamente no código?
3. Qual é a diferença entre `.env` e `.env.example`?
4. O que é um modelo?
5. Qual é a diferença entre o modelo local desta ficha e o modelo da OpenAI?
6. Como é calculada a confiança local?
7. Porque é que dividimos o PDF em blocos?
8. O que é fallback?
9. O que pode correr mal ao extrair texto de um PDF?
10. Porque é que enviamos apenas excertos relevantes para a API?
11. O que é uma alucinação num modelo de IA?
12. Como poderias melhorar esta aplicação?

---

## 24) Resumo final

Nesta ficha construíste uma pequena aplicação útil:

- lê um PDF;
- permite fazer perguntas;
- procura respostas localmente;
- mede uma confiança simples;
- usa a OpenAI API apenas quando precisa;
- protege secrets com `.env`.

Mais importante do que a aplicação em si é a ideia de arquitetura:

```text
Dados próprios + pesquisa local + fallback inteligente + segurança básica
```

Esta combinação aparece em muitos sistemas reais com IA.
