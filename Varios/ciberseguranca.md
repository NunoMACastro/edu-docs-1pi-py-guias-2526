![Header](Images/Header.png)

# Aula de Cibersegurança

## Autenticação, autorização, tokens, chaves, encriptação, hashing e proteção de sistemas

## 1. Objetivos da aula

No final da aula, os alunos devem conseguir explicar:

- A diferença entre autenticação e autorização.
- O que são sessões, cookies, tokens e JWTs.
- O que são chaves de autenticador, passkeys e códigos de segundo fator.
- A diferença entre encriptação e hashing.
- Porque é que palavras-passe nunca devem ser guardadas em texto simples.
- Como falhas comuns podem levar a acessos indevidos.
- Como proteger contas pessoais e sistemas informáticos.
- Porque é que a segurança deve ser pensada desde o início de um projeto.

Também devem compreender uma ideia muito importante: a maioria dos ataques não acontece por "magia" nem por génios a escrever código impossível. Muitos ataques exploram falhas simples: palavras-passe fracas, sistemas desatualizados, configurações erradas, falta de validação, permissões mal definidas, engenharia social ou dados demasiado expostos.

---

## 2. O que é cibersegurança?

Cibersegurança é o conjunto de práticas, tecnologias e decisões usadas para proteger sistemas digitais, redes, dispositivos, aplicações e dados contra acesso indevido, alteração, destruição ou abuso.

Uma forma clássica de pensar em segurança é através de três objetivos:

| Objetivo          | Pergunta principal                                | Exemplo                                                          |
| ----------------- | ------------------------------------------------- | ---------------------------------------------------------------- |
| Confidencialidade | Quem pode ver a informação?                       | Só o aluno e professores autorizados devem ver uma nota.         |
| Integridade       | A informação foi alterada indevidamente?          | Uma nota não deve poder ser modificada por alguém sem permissão. |
| Disponibilidade   | O sistema continua acessível quando é necessário? | A plataforma deve estar disponível durante uma avaliação.        |

Estes três objetivos são conhecidos como a tríade CIA: Confidentiality, Integrity, Availability.

Em sistemas reais também se fala frequentemente de:

- Autenticidade: garantir que uma entidade é realmente quem diz ser.
- Não repúdio: impedir que alguém negue uma ação que realizou, quando existe prova técnica válida.
- Rastreabilidade: conseguir perceber quem fez o quê, quando e a partir de onde.

Segurança não é um produto que se instala no fim. É uma propriedade do sistema inteiro: código, configuração, infraestrutura, utilizadores, processos, logs, backups, políticas e cultura.

---

## 3. Ameaças, vulnerabilidades e risco

Antes de falar de mecanismos técnicos, convém distinguir três conceitos.

### Ameaça

Uma ameaça é algo que pode causar dano.

Exemplos:

- Um atacante externo.
- Um aluno que tenta aceder a dados de outros alunos.
- Malware num computador da escola.
- Um funcionário enganado por phishing.
- Uma falha de energia ou perda de disco.

### Vulnerabilidade

Uma vulnerabilidade é uma fraqueza que pode ser explorada.

Exemplos:

- Palavra-passe fraca.
- Servidor sem atualizações.
- Base de dados exposta na internet.
- Falta de validação de permissões no backend.
- Tokens sem expiração.
- Dados sensíveis em logs.

### Risco

Risco é a combinação entre probabilidade e impacto.

Uma vulnerabilidade difícil de explorar e com impacto baixo pode ser menos urgente. Uma vulnerabilidade fácil de explorar e com impacto alto deve ser tratada rapidamente.

Uma pergunta prática para avaliar risco:

> Se isto falhar, quem fica prejudicado, que dados são expostos, que serviços param, e quanto tempo demoramos a recuperar?

---

## 4. Autenticação

Autenticação responde à pergunta:

> Quem és?

Quando um utilizador faz login, o sistema tenta confirmar a identidade desse utilizador.

Exemplos de autenticação:

- Entrar numa conta com email e palavra-passe.
- Usar impressão digital no telemóvel.
- Introduzir um código recebido numa aplicação autenticadora.
- Usar uma passkey.
- Inserir um cartão físico ou uma chave de segurança.

### 4.1. Fatores de autenticação

Os fatores de autenticação costumam dividir-se em categorias:

| Categoria      | Ideia                     | Exemplos                           |
| -------------- | ------------------------- | ---------------------------------- |
| Algo que sabes | Um segredo memorizado     | Palavra-passe, PIN                 |
| Algo que tens  | Um objeto ou dispositivo  | Telemóvel, chave FIDO2, smart card |
| Algo que és    | Característica biométrica | Impressão digital, rosto           |

MFA, ou multi-factor authentication, significa usar mais do que um fator. Por exemplo:

- Palavra-passe + código da aplicação autenticadora.
- Palavra-passe + chave física.
- Passkey protegida por biometria local.

Isto é mais seguro porque roubar apenas uma parte deixa de ser suficiente.

### 4.2. Como funciona um login simples

Um fluxo simplificado de login pode ser assim:

1. O utilizador introduz email e palavra-passe.
2. O browser envia esses dados ao servidor através de HTTPS.
3. O servidor procura o utilizador na base de dados.
4. O servidor compara a palavra-passe recebida com o hash guardado.
5. Se a autenticação estiver correta, o servidor cria uma sessão ou emite um token.
6. O cliente passa a enviar essa sessão ou token nos pedidos seguintes.

Ponto importante: num sistema bem desenhado, a base de dados não guarda a palavra-passe original. Guarda um hash seguro da palavra-passe.

### 4.3. Erros comuns na autenticação

Erros graves:

- Guardar palavras-passe em texto simples.
- Usar hashes rápidos e inadequados para passwords, como MD5 ou SHA-1.
- Não usar salt por utilizador.
- Permitir palavras-passe muito fracas.
- Não limitar tentativas de login.
- Mostrar mensagens como "o email existe, mas a password está errada", facilitando enumeração de contas.
- Enviar palavras-passe por email.
- Usar perguntas de segurança fáceis de descobrir.
- Não proteger o processo de recuperação de conta.
- Não invalidar sessões antigas depois de uma alteração de palavra-passe.
- Permitir contas administrativas sem MFA.

### 4.4. Boas práticas na autenticação

Boas práticas técnicas:

- Usar HTTPS em todas as páginas e APIs autenticadas.
- Guardar passwords com algoritmos próprios para password hashing, como Argon2id, bcrypt ou scrypt.
- Usar salt único por password.
- Considerar pepper guardado fora da base de dados, quando adequado.
- Ativar MFA para contas sensíveis.
- Aplicar rate limiting e proteções contra brute force.
- Usar mensagens de erro genéricas.
- Registar eventos importantes: login, falha de login, alteração de password, ativação de MFA.
- Alertar o utilizador quando há login a partir de um novo dispositivo ou localização incomum.
- Ter um processo seguro de recuperação de conta.

Boas práticas para utilizadores:

- Usar palavras-passe longas e únicas.
- Usar um gestor de palavras-passe.
- Ativar MFA sempre que possível.
- Preferir aplicações autenticadoras ou chaves físicas a SMS, quando disponível.
- Nunca reutilizar a password do email principal noutros sites.
- Verificar cuidadosamente links de login.

---

## 5. Autorização

Autorização responde à pergunta:

> O que podes fazer?

Depois de saber quem é o utilizador, o sistema precisa de decidir que ações esse utilizador pode executar.

Autenticação e autorização não são a mesma coisa.

Exemplo:

- Autenticação: "Este utilizador é a professora Ana."
- Autorização: "A professora Ana pode ver as notas da sua turma, mas não pode alterar as notas de outra turma."

### 5.1. Exemplos simples

Numa plataforma escolar:

| Papel            | Pode fazer                                       |
| ---------------- | ------------------------------------------------ |
| Aluno            | Ver os seus próprios dados e submeter trabalhos. |
| Professor        | Ver alunos das suas turmas e avaliar trabalhos.  |
| Diretor de turma | Ver informação adicional da turma.               |
| Administrador    | Gerir utilizadores, turmas e configurações.      |

O erro perigoso é assumir que, por o utilizador estar autenticado, pode aceder a tudo.

### 5.2. Modelos de autorização

#### RBAC

RBAC significa Role-Based Access Control.

As permissões dependem do papel do utilizador.

Exemplo:

- `student`
- `teacher`
- `admin`

É simples e comum, mas pode ser insuficiente quando há regras mais específicas.

#### ABAC

ABAC significa Attribute-Based Access Control.

A decisão usa atributos do utilizador, do recurso, da ação e do contexto.

Exemplo:

> Um professor pode ver uma avaliação se pertence à disciplina, a turma está ativa e a avaliação ainda não foi arquivada.

ABAC é mais flexível, mas também exige mais cuidado.

#### Ownership

Ownership significa verificar se o recurso pertence ao utilizador ou ao seu âmbito.

Exemplo:

> Um aluno pode ver `/submissions/123` apenas se a submissão 123 for dele.

Esta verificação é essencial. Não basta esconder botões na interface.

### 5.3. Erros comuns na autorização

Erros frequentes:

- Verificar permissões apenas no frontend.
- Confiar no campo `role` enviado pelo cliente.
- Permitir acesso a recursos por IDs previsíveis sem verificar dono.
- Ter endpoints administrativos sem proteção adequada.
- Esquecer verificações em rotas novas.
- Misturar dados de escolas, turmas ou clientes diferentes.
- Dar privilégios administrativos a contas que não precisam.

Um caso clássico é IDOR: Insecure Direct Object Reference.

Exemplo conceptual:

```text
/api/alunos/1001/notas
/api/alunos/1002/notas
```

Se o aluno autenticado consegue mudar o ID no URL e ver dados de outro aluno, há uma falha grave de autorização.

### 5.4. Boas práticas na autorização

Boas práticas:

- Verificar autorização no servidor, em todos os pedidos.
- Usar deny by default: se não há permissão explícita, o acesso é negado.
- Centralizar regras de autorização quando possível.
- Separar autenticação de autorização no código.
- Aplicar o princípio do menor privilégio.
- Validar sempre que o recurso pertence ao utilizador, turma, escola ou organização correta.
- Criar testes para acessos permitidos e negados.
- Fazer logs de ações sensíveis.
- Rever permissões periodicamente.

---

## 6. Sessões, cookies e tokens

Depois do login, o sistema precisa de se lembrar de que aquele utilizador já foi autenticado. Para isso, usa normalmente sessões ou tokens.

### 6.1. Sessão tradicional

Numa sessão tradicional:

1. O utilizador faz login.
2. O servidor cria um identificador de sessão.
3. O servidor guarda informação da sessão numa base de dados, cache ou memória.
4. O browser guarda o identificador num cookie.
5. Em pedidos seguintes, o browser envia o cookie automaticamente.
6. O servidor consulta a sessão e identifica o utilizador.

Vantagem: o servidor pode invalidar a sessão a qualquer momento.

Desvantagem: exige armazenamento de sessão no servidor.

### 6.2. Cookies

Cookies são pequenos dados que o browser guarda para um site.

Um cookie de sessão deve ser configurado com cuidado:

- `HttpOnly`: impede acesso ao cookie através de JavaScript.
- `Secure`: envia o cookie apenas por HTTPS.
- `SameSite`: ajuda a reduzir ataques CSRF.
- `Expires` ou `Max-Age`: define a duração.

Exemplo conceptual de configuração segura:

```text
Set-Cookie: sessionId=valor_aleatorio; HttpOnly; Secure; SameSite=Lax; Path=/
```

O valor do cookie deve ser imprevisível. Nunca deve conter informação sensível em texto simples.

### 6.3. Tokens

Um token é um valor que representa uma autorização, uma identidade autenticada ou uma permissão temporária.

Exemplos:

- Token de sessão.
- Access token.
- Refresh token.
- Token de recuperação de password.
- Token de confirmação de email.

Tokens devem ser tratados como segredos. Quem possui um token válido pode, muitas vezes, agir como o utilizador.

### 6.4. JWT

JWT significa JSON Web Token.

Um JWT costuma ter três partes:

```text
header.payload.signature
```

- Header: informação sobre o tipo de token e algoritmo.
- Payload: claims, ou seja, dados como `sub`, `exp`, `iss`, `aud`.
- Signature: assinatura que permite verificar se o token foi alterado.

Importante:

- Um JWT assinado não é automaticamente secreto.
- A parte do payload pode ser lida se alguém tiver o token.
- Assinatura garante integridade, não confidencialidade.
- Não se devem guardar passwords, dados médicos, notas ou informação sensível no payload.

Claims comuns:

| Claim | Significado                             |
| ----- | --------------------------------------- |
| `sub` | Subject: identificador do utilizador.   |
| `exp` | Expiration time: quando o token expira. |
| `iat` | Issued at: quando foi emitido.          |
| `iss` | Issuer: quem emitiu o token.            |
| `aud` | Audience: para quem o token se destina. |

### 6.5. Access tokens e refresh tokens

Um access token é usado para aceder a recursos. Deve ter curta duração.

Um refresh token é usado para obter novos access tokens. Deve ser mais protegido.

Exemplo conceptual:

1. O utilizador faz login.
2. O servidor emite um access token curto.
3. O servidor emite um refresh token mais duradouro.
4. O cliente usa o access token nas APIs.
5. Quando o access token expira, o refresh token pode pedir outro.

Riscos:

- Se um access token for roubado, pode ser usado até expirar.
- Se um refresh token for roubado, o atacante pode manter acesso durante mais tempo.

Proteções:

- Expiração curta para access tokens.
- Refresh token rotation.
- Revogação de refresh tokens.
- Armazenamento seguro.
- Deteção de reutilização de refresh tokens antigos.

---

## 7. Chaves de autenticador, MFA e passkeys

### 7.1. Códigos TOTP

Muitas apps autenticadoras usam TOTP: Time-Based One-Time Password.

Funciona assim:

1. Durante a configuração, o serviço e a app autenticadora partilham um segredo.
2. A app usa esse segredo e a hora atual para gerar um código temporário.
3. O servidor gera o mesmo código do seu lado.
4. Se os códigos coincidirem, o segundo fator é aceite.

Os códigos mudam normalmente a cada 30 segundos.

Cuidados:

- O segredo inicial deve ser protegido.
- Os códigos não devem ser partilhados.
- Se alguém fotografar o QR code de configuração, pode configurar a mesma conta noutro dispositivo.

### 7.2. SMS como segundo fator

SMS é melhor do que não ter MFA, mas tem fragilidades:

- SIM swapping.
- Interceção por malware no telemóvel.
- Phishing em tempo real.
- Dependência da rede móvel.

Sempre que possível, é preferível usar uma app autenticadora, passkey ou chave física.

### 7.3. Chaves físicas

Chaves físicas de segurança, como dispositivos FIDO2/WebAuthn, usam criptografia de chave pública.

Ideia simplificada:

- A chave cria um par de chaves: uma privada e uma pública.
- A chave privada nunca sai do dispositivo.
- O serviço guarda a chave pública.
- No login, o serviço envia um desafio.
- A chave assina o desafio com a chave privada.
- O serviço verifica a assinatura com a chave pública.

Isto reduz muito o risco de phishing, porque a chave verifica o domínio do site. Uma chave configurada para `exemplo.com` não deve autenticar automaticamente em `exemp1o.com`.

### 7.4. Passkeys

Passkeys são uma forma moderna de login baseada em chaves criptográficas, normalmente usando WebAuthn/FIDO2.

Na prática:

- Não há password tradicional para roubar.
- O utilizador confirma com biometria, PIN ou desbloqueio do dispositivo.
- O site recebe uma prova criptográfica, não uma password.
- A chave privada fica no dispositivo ou num gestor sincronizado.

Vantagens:

- Resistentes a phishing quando bem implementadas.
- Mais fáceis para muitos utilizadores.
- Evitam reutilização de passwords.

Cuidados:

- É preciso planear recuperação de conta.
- Dispositivos perdidos devem poder ser removidos.
- Contas críticas devem ter métodos de recuperação seguros.

---

## 8. Encriptação

Encriptação transforma dados legíveis em dados ilegíveis para quem não tem a chave correta.

Texto original:

```text
A nota do aluno é 17.
```

Depois de encriptado:

```text
9fK2...dados aparentemente sem sentido...Lq0
```

Com a chave correta, os dados podem ser desencriptados e voltar ao original.

### 8.1. Para que serve a encriptação?

Serve para proteger confidencialidade.

Exemplos:

- HTTPS protege dados em trânsito entre browser e servidor.
- Disco encriptado protege dados se o portátil for roubado.
- Backups encriptados protegem cópias de segurança.
- Bases de dados podem encriptar campos sensíveis.

### 8.2. Encriptação simétrica

Na encriptação simétrica, a mesma chave serve para encriptar e desencriptar.

Analogia:

> A mesma chave fecha e abre a mesma caixa.

Exemplos de uso:

- Encriptar ficheiros.
- Encriptar dados em bases de dados.
- Proteger backups.

Vantagem: é rápida.

Desafio: como partilhar a chave de forma segura?

### 8.3. Encriptação assimétrica

Na encriptação assimétrica, existem duas chaves:

- Chave pública: pode ser partilhada.
- Chave privada: deve ficar secreta.

O que uma chave faz, a outra pode verificar ou reverter, dependendo do uso.

Usos comuns:

- Troca segura de chaves.
- Assinaturas digitais.
- Certificados TLS.
- Autenticação por chave SSH.

Analogia:

> A chave pública é como uma caixa de correio onde todos podem colocar mensagens. A chave privada é a única que permite abrir a caixa e ler o conteúdo.

### 8.4. HTTPS e TLS

HTTPS é HTTP protegido por TLS.

Quando usamos HTTPS:

- O browser verifica o certificado do site.
- O browser e o servidor negociam chaves.
- Os dados passam encriptados.
- Um atacante na rede não deve conseguir ler facilmente o conteúdo.

HTTPS protege contra muitos ataques na rede, mas não resolve tudo. Se o próprio site tiver uma falha de autorização, HTTPS não impede que um utilizador autenticado aceda a dados que não devia.

### 8.5. Erros comuns com encriptação

Erros frequentes:

- Criar algoritmos próprios.
- Guardar a chave junto dos dados encriptados.
- Reutilizar nonces ou IVs quando o algoritmo exige valores únicos.
- Usar algoritmos antigos ou modos inseguros.
- Pensar que Base64 é encriptação.
- Esquecer rotação de chaves.
- Expor segredos em repositórios Git.

Regra prática:

> Não inventes criptografia. Usa bibliotecas maduras, algoritmos modernos e configurações recomendadas.

---

## 9. Hashing

Hashing transforma dados numa impressão digital de tamanho fixo.

Exemplo conceptual:

```text
Entrada: "olá"
Hash:    "b221d9dbb083a7f33428a42103a84f..."
```

Uma função de hash criptográfica deve ter propriedades importantes:

- É fácil calcular o hash de uma entrada.
- É impraticável descobrir a entrada original a partir do hash.
- Pequenas mudanças na entrada alteram muito o resultado.
- Deve ser impraticável encontrar duas entradas diferentes com o mesmo hash.

### 9.1. Hashing não é encriptação

A diferença mais importante:

| Conceito    | Dá para reverter? | Objetivo principal        |
| ----------- | ----------------- | ------------------------- |
| Encriptação | Sim, com chave    | Confidencialidade         |
| Hashing     | Não, idealmente   | Integridade e verificação |

Se algo precisa de voltar ao valor original, encriptamos.

Se só precisamos de verificar que algo corresponde, usamos hash.

### 9.2. Hashing de passwords

Passwords não devem ser guardadas em texto simples.

Fluxo correto simplificado:

1. O utilizador cria uma password.
2. O servidor gera um salt único.
3. O servidor calcula um hash lento da password com esse salt.
4. A base de dados guarda o salt e o hash.
5. No login, o servidor repete o processo com a password introduzida.
6. Se o resultado coincidir, a password está correta.

### 9.3. Porque hashes rápidos não chegam para passwords?

Algoritmos como SHA-256 são excelentes para muitos usos, mas são demasiado rápidos para passwords.

Se uma base de dados com hashes for roubada, um atacante pode tentar milhões ou milhares de milhões de passwords por segundo com hardware especializado.

Por isso, para passwords devem usar-se algoritmos lentos e ajustáveis:

- Argon2id.
- bcrypt.
- scrypt.
- PBKDF2, quando necessário por compatibilidade.

Estes algoritmos tornam ataques offline muito mais caros.

### 9.4. Salt

Salt é um valor aleatório único associado a cada password.

Serve para:

- Impedir que duas passwords iguais tenham o mesmo hash.
- Dificultar ataques com tabelas pré-calculadas.
- Obrigar o atacante a trabalhar password a password.

O salt não precisa de ser secreto. Precisa de ser único e aleatório.

### 9.5. Pepper

Pepper é um segredo adicional, normalmente guardado fora da base de dados.

Se a base de dados for roubada mas o pepper não, o atacante tem mais dificuldade em validar passwords.

Ao contrário do salt, o pepper deve ser secreto.

---

## 10. Como sistemas são comprometidos, de forma geral

Esta secção deve ser ensinada com uma postura defensiva. O objetivo é reconhecer classes de falhas e saber preveni-las, não executar ataques em sistemas reais.

### 10.1. Engenharia social

Muitos incidentes começam com pessoas, não com código.

Exemplos:

- Emails falsos a pedir login.
- Mensagens urgentes a pedir códigos MFA.
- Chamadas a fingir ser suporte técnico.
- Links que imitam páginas conhecidas.
- Anexos maliciosos.

Proteções:

- Confirmar pedidos por canais independentes.
- Não partilhar códigos MFA.
- Verificar domínio e certificado.
- Usar gestores de passwords, que ajudam a detetar domínios falsos.
- Treinar utilizadores com exemplos realistas.

### 10.2. Passwords fracas ou reutilizadas

Se alguém reutiliza a mesma password em vários sites, uma fuga num site pode comprometer outros.

Ataques comuns:

- Credential stuffing: testar combinações email/password já vazadas.
- Brute force: tentar muitas passwords.
- Password spraying: testar uma password comum em muitas contas.

Proteções:

- Passwords únicas.
- Gestor de passwords.
- MFA.
- Rate limiting.
- Deteção de logins suspeitos.
- Bloqueio progressivo ou atrasos após falhas.

### 10.3. Falhas de autorização

Uma das classes mais perigosas em aplicações web é a falta de verificação de permissões.

Exemplo conceptual:

> Um utilizador autenticado consegue alterar o ID de um recurso no URL e aceder a informação de outra pessoa.

Proteções:

- Verificação de ownership no backend.
- Testes de permissões.
- IDs imprevisíveis ajudam, mas não substituem autorização.
- Logs de acessos sensíveis.
- Revisão de endpoints novos.

### 10.4. Injeção

Injeção acontece quando dados fornecidos pelo utilizador são interpretados como código ou comandos.

Tipos comuns:

- SQL Injection.
- Command Injection.
- LDAP Injection.
- Template Injection.

Exemplo conceptual, sem payloads reais:

> Uma aplicação junta texto introduzido pelo utilizador diretamente numa query. O sistema de base de dados pode interpretar parte desse texto como instrução, e não como dado.

Proteções:

- Queries parametrizadas.
- ORMs bem usados.
- Validação de entrada.
- Escaping adequado ao contexto.
- Menor privilégio na conta da base de dados.

### 10.5. XSS

XSS significa Cross-Site Scripting.

Acontece quando um site permite que conteúdo controlado por um utilizador seja executado como JavaScript no browser de outro utilizador.

Impacto possível:

- Roubo de dados visíveis na página.
- Ações em nome do utilizador.
- Alteração do conteúdo mostrado.
- Roubo de tokens se estiverem mal armazenados.

Proteções:

- Escapar output conforme o contexto.
- Sanitizar HTML quando HTML de utilizador é mesmo necessário.
- Usar frameworks que escapam por defeito.
- Configurar Content Security Policy.
- Usar cookies `HttpOnly` para sessões.

### 10.6. CSRF

CSRF significa Cross-Site Request Forgery.

Acontece quando um site malicioso tenta fazer o browser de um utilizador autenticado enviar um pedido para outro site onde esse utilizador tem sessão ativa.

Proteções:

- Cookies `SameSite`.
- Tokens anti-CSRF.
- Verificação de origem em operações sensíveis.
- Pedir reautenticação para ações críticas.

### 10.7. Ficheiros enviados por utilizadores

Uploads são perigosos quando mal tratados.

Riscos:

- Upload de ficheiros executáveis.
- Ficheiros muito grandes que esgotam recursos.
- Conteúdo malicioso disfarçado.
- Exposição de ficheiros privados.
- Path traversal em nomes de ficheiros.

Proteções:

- Validar tipo e tamanho.
- Renomear ficheiros no servidor.
- Guardar fora da pasta pública quando apropriado.
- Fazer scanning quando necessário.
- Não confiar apenas na extensão.
- Definir permissões corretas.

### 10.8. Dependências vulneráveis

Projetos modernos usam muitas bibliotecas.

Riscos:

- Dependências desatualizadas.
- Pacotes abandonados.
- Pacotes maliciosos.
- Ataques de supply chain.

Proteções:

- Manter dependências atualizadas.
- Usar lockfiles.
- Rever novas dependências antes de adicionar.
- Usar ferramentas de auditoria.
- Remover dependências desnecessárias.
- Preferir bibliotecas conhecidas e mantidas.

### 10.9. Configurações erradas

Muitas falhas graves vêm de configuração.

Exemplos:

- Painel administrativo exposto.
- Base de dados acessível publicamente.
- Credenciais por defeito.
- Ambiente de debug em produção.
- Buckets ou diretorias públicas sem querer.
- CORS demasiado permissivo.
- Segredos em variáveis expostas ao frontend.

Proteções:

- Checklists de deploy.
- Ambientes separados: desenvolvimento, teste, produção.
- Segredos em secret managers ou variáveis protegidas.
- Revisões de configuração.
- Infraestrutura como código.
- Princípio do menor privilégio.

### 10.10. Falhas de logging e monitorização

Sem logs, pode ser impossível perceber o que aconteceu.

Mas logs também podem ser perigosos se guardarem dados sensíveis.

Boas práticas:

- Registar eventos de segurança.
- Não escrever passwords, tokens ou dados altamente sensíveis em logs.
- Proteger acesso aos logs.
- Definir alertas para eventos incomuns.
- Guardar logs tempo suficiente para investigação.

---

## 11. Como proteger um sistema

### 11.1. Princípio do menor privilégio

Cada utilizador, serviço e processo deve ter apenas as permissões necessárias.

Exemplos:

- A aplicação não deve usar uma conta de base de dados com permissões administrativas se só precisa de ler e escrever algumas tabelas.
- Um professor não deve ter permissões de administrador global se apenas gere uma turma.
- Um token de API deve ter scope limitado.

### 11.2. Defesa em profundidade

Defesa em profundidade significa ter várias camadas de proteção.

Exemplo:

1. HTTPS protege a comunicação.
2. Autenticação verifica identidade.
3. MFA reduz risco de password roubada.
4. Autorização limita ações.
5. Logs ajudam a detetar abuso.
6. Backups ajudam a recuperar.
7. Monitorização alerta sobre comportamento estranho.

Nenhuma camada é perfeita. Várias camadas reduzem o risco.

### 11.3. Validação de input

Todo o input externo deve ser tratado como não confiável.

Input externo inclui:

- Formulários.
- Parâmetros no URL.
- Headers.
- Cookies.
- Ficheiros.
- Webhooks.
- Respostas de APIs externas.

Boas práticas:

- Validar tipos, tamanhos e formatos.
- Rejeitar dados inesperados.
- Usar schemas quando possível.
- Normalizar dados antes de processar.
- Escapar output conforme o contexto.

### 11.4. Gestão de segredos

Segredos incluem:

- Passwords de bases de dados.
- API keys.
- Chaves privadas.
- Tokens.
- Secrets de JWT.
- Credenciais de email.

Boas práticas:

- Nunca guardar segredos no Git.
- Usar variáveis de ambiente ou secret managers.
- Rodar segredos quando há suspeita de exposição.
- Separar segredos por ambiente.
- Dar acesso apenas a quem precisa.

### 11.5. Backups

Backups são segurança.

Um sistema pode ser atacado, apagado, encriptado por ransomware ou corrompido por erro humano.

Boas práticas:

- Fazer backups regulares.
- Testar restauração.
- Guardar cópias fora do sistema principal.
- Encriptar backups.
- Controlar acesso aos backups.
- Definir RPO e RTO.

RPO: quantos dados podemos perder.

RTO: quanto tempo podemos demorar a recuperar.

### 11.6. Atualizações

Software desatualizado é uma das causas mais comuns de incidentes.

Boas práticas:

- Atualizar sistema operativo.
- Atualizar frameworks.
- Atualizar bibliotecas.
- Acompanhar avisos de segurança.
- Ter processo de patching.
- Testar antes de atualizar produção, quando possível.

### 11.7. Testes de segurança

Testes úteis:

- Testes unitários para regras de autorização.
- Testes de integração para endpoints protegidos.
- Análise estática de código.
- Auditoria de dependências.
- Revisão de configuração.
- Pentests autorizados.
- Exercícios de threat modeling.

Em ambiente escolar, os alunos podem praticar em laboratórios isolados, CTFs educativos e aplicações vulneráveis criadas para treino.

---

## 12. Dicas de cibersegurança para alunos e professores

### 12.1. Dicas óbvias, mas essenciais

- Usa passwords diferentes em cada serviço.
- Ativa MFA.
- Bloqueia o computador quando te afastas.
- Não partilhes contas.
- Não abras anexos inesperados.
- Atualiza o sistema e o browser.
- Não ignores avisos de segurança do browser.
- Faz logout em computadores partilhados.
- Não uses software pirata.
- Faz backups.

### 12.2. Dicas menos óbvias

- O email principal é uma conta crítica: se for comprometido, pode recuperar muitas outras contas.
- Um gestor de passwords também ajuda contra phishing, porque não preenche passwords em domínios errados.
- MFA por SMS é melhor do que nada, mas não é o método mais forte.
- Códigos de recuperação devem ser guardados em local seguro.
- QR codes podem apontar para sites maliciosos; devem ser tratados como links.
- "Ver HTTPS" não chega: sites falsos também podem ter HTTPS.
- Não publiques fotografias que revelem crachás, quadros, horários, nomes de redes ou informação interna.
- Não deixes tokens, API keys ou ficheiros `.env` em screenshots.
- Dados apagados de uma aplicação podem continuar em backups ou logs.
- Um link encurtado esconde o destino real.
- Dispositivos USB encontrados podem ser perigosos.
- Extensões de browser podem ler dados das páginas se tiverem permissões excessivas.
- Um computador desbloqueado equivale muitas vezes a uma conta aberta.
- Partilhar ecrã pode revelar notificações, separadores, passwords guardadas ou tokens.

### 12.3. Regras pessoais simples

- Desconfia de urgência artificial: "faz isto agora ou perdes acesso".
- Confirma pedidos sensíveis por outro canal.
- Não envies códigos MFA a ninguém.
- Usa passphrases longas em vez de passwords curtas e complexas, mas impossíveis de memorizar.
- Mantém software atualizado.
- Se suspeitares de compromisso, muda passwords a partir de um dispositivo confiável.
- Reporta incidentes cedo. Esconder aumenta o dano.

---

## 13. Regras de cibersegurança para equipas e escolas

### 13.1. Regras óbvias

- Cada pessoa deve ter a sua própria conta.
- Contas administrativas devem usar MFA.
- Acesso deve ser removido quando alguém sai da instituição.
- Sistemas devem estar atualizados.
- Backups devem existir e ser testados.
- Dados sensíveis devem ter acesso restrito.
- Incidentes devem ter um processo claro de reporte.

### 13.2. Regras menos óbvias

- Separar contas normais de contas administrativas.
- Rever permissões periodicamente.
- Criar contas temporárias com expiração.
- Usar logs de auditoria para ações sensíveis.
- Evitar partilha de documentos com "qualquer pessoa com o link" quando há dados sensíveis.
- Não usar contas genéricas como `admin`, `professor` ou `secretaria` sem responsabilização individual.
- Ter ambientes separados para testes e produção.
- Não usar dados reais de alunos em ambientes de teste, salvo se forem anonimizados e houver autorização.
- Criar plano de resposta a incidentes.
- Definir quem comunica com alunos, encarregados de educação e autoridades em caso de incidente.
- Testar restauração de backups antes de precisar deles.
- Documentar sistemas: sem documentação, a resposta a incidentes fica mais lenta.

### 13.3. Política mínima recomendada

Uma escola ou equipa deveria ter, no mínimo:

- Política de passwords e MFA.
- Política de acessos e permissões.
- Política de backups.
- Política de atualizações.
- Política de tratamento de dados pessoais.
- Procedimento de resposta a incidentes.
- Inventário de sistemas e responsáveis.
- Regras para uso de dispositivos pessoais.
- Plano de formação regular.

---

## 14. Como pensar como defensor

Um defensor faz perguntas sistemáticas.

### 14.1. Perguntas sobre dados

- Que dados guardamos?
- Estes dados são sensíveis?
- Quem precisa mesmo de aceder?
- Quanto tempo temos de os guardar?
- Estão encriptados em repouso?
- Aparecem em logs?
- Aparecem em exports?
- Aparecem em backups?

### 14.2. Perguntas sobre utilizadores

- Como verificamos identidade?
- MFA está ativo para contas críticas?
- O que acontece quando alguém perde acesso?
- Como removemos acesso quando deixa de ser necessário?
- Existem contas partilhadas?

### 14.3. Perguntas sobre código

- Todos os endpoints verificam autorização?
- O backend valida input?
- Estamos a confiar no cliente?
- Há dados sensíveis no frontend?
- As mensagens de erro revelam demasiado?
- Existem testes para permissões?

### 14.4. Perguntas sobre operação

- Temos logs suficientes?
- Quem recebe alertas?
- Os backups foram testados?
- Como fazemos rollback?
- Que dependências usamos?
- Como reagimos a uma vulnerabilidade crítica?

---

## 15. Mini modelos mentais para explicar aos alunos

### 15.1. Autenticação vs. autorização

Analogia da escola:

- Autenticação: mostrar o cartão da escola para provar quem és.
- Autorização: mesmo com cartão, nem todas as portas podem ser abertas por toda a gente.

### 15.2. Token

Analogia do bilhete:

- Um token é como um bilhete temporário.
- Quem tem o bilhete pode entrar em certas zonas.
- Se o bilhete for roubado, outra pessoa pode tentar usá-lo.
- Por isso, bilhetes devem expirar e poder ser anulados.

### 15.3. Hash

Analogia da impressão digital:

- Um hash é como uma impressão digital de um dado.
- Ajuda a verificar se algo é igual.
- Não deve permitir reconstruir o dado original.

### 15.4. Encriptação

Analogia da caixa fechada:

- Encriptar é colocar uma mensagem numa caixa fechada.
- Só quem tem a chave certa consegue abrir.

### 15.5. MFA

Analogia da porta com duas fechaduras:

- Uma password é uma fechadura.
- MFA acrescenta outra.
- Se alguém roubar uma chave, ainda precisa da segunda.

---

## 16. Exemplos didáticos seguros

### 16.1. Exemplo: decisão de autorização

Pseudocódigo:

```text
se utilizador não está autenticado:
    negar_acesso

se recurso.pertence_ao_utilizador:
    permitir_acesso
senão se utilizador.tem_papel("admin"):
    permitir_acesso
senão:
    negar_acesso
```

Ideia principal:

> A verificação acontece no servidor e considera o recurso concreto, não apenas o facto de existir login.

### 16.2. Exemplo: password hashing

Pseudocódigo:

```text
ao_criar_conta(password):
    salt = gerar_valor_aleatório()
    hash = algoritmo_lento(password, salt)
    guardar(salt, hash)

ao_fazer_login(password_introduzida):
    salt, hash_guardado = obter_da_base_de_dados()
    hash_calculado = algoritmo_lento(password_introduzida, salt)

    se hash_calculado == hash_guardado:
        login_valido
    senão:
        login_invalido
```

Ideia principal:

> A password original não precisa de ser guardada para ser verificada.

### 16.3. Exemplo: token com expiração

Pseudocódigo:

```text
token = criar_token(
    utilizador_id = 123,
    expira_em = agora + 15_minutos,
    permissões = ["ler_perfil"]
)
```

Ideia principal:

> Tokens devem ter tempo de vida limitado e permissões limitadas.

---

## 17. Atividades para a aula

### Atividade 1: Classificar situações

Pedir aos alunos para classificarem cada situação como problema de autenticação, autorização, confidencialidade, integridade ou disponibilidade.

Exemplos:

- Um aluno descobre a password de outro aluno.
- Um aluno autenticado consegue ver notas de outra turma.
- Uma nota é alterada sem registo.
- A plataforma fica indisponível no dia de entrega.
- Um backup com dados pessoais fica público.

### Atividade 2: Desenhar um fluxo de login seguro

Os alunos devem desenhar:

1. Formulário de login.
2. Envio por HTTPS.
3. Verificação do hash.
4. MFA.
5. Criação de sessão.
6. Cookie seguro.
7. Logs.
8. Erros genéricos.

### Atividade 3: Rever permissões de uma plataforma escolar

Dar uma lista de papéis:

- Aluno.
- Professor.
- Diretor de turma.
- Secretaria.
- Administrador.

Pedir para definir:

- Que dados cada papel pode ver.
- Que dados pode alterar.
- Que ações devem ficar registadas em logs.
- Que ações exigem MFA ou reautenticação.

### Atividade 4: Detetar phishing

Mostrar exemplos simulados de mensagens e pedir aos alunos para identificar sinais de alerta:

- Urgência.
- Erros no domínio.
- Pedido de password ou código.
- Anexos estranhos.
- Remetente suspeito.
- Link encurtado.
- Tom emocional ou ameaçador.

### Atividade 5: Plano de resposta a incidente

Propor o seguinte cenário:

> Foi detetado acesso indevido a contas de alunos.

Os alunos devem responder:

- Quem deve ser avisado?
- Que sistemas devem ser verificados?
- Que logs são importantes?
- Que contas devem ser bloqueadas ou revistas?
- Como comunicar sem espalhar pânico?
- Como prevenir repetição?

---

## 18. Resposta a incidentes

Quando algo corre mal, improvisar é perigoso. É melhor ter um plano.

### 18.1. Etapas comuns

1. Preparação.
2. Identificação.
3. Contenção.
4. Erradicação.
5. Recuperação.
6. Lições aprendidas.

### 18.2. Preparação

Antes do incidente:

- Ter contactos definidos.
- Saber quem decide.
- Saber onde estão os logs.
- Ter backups testados.
- Ter inventário de sistemas.
- Ter plano de comunicação.

### 18.3. Identificação

Perceber:

- O que aconteceu?
- Quando começou?
- Que contas foram afetadas?
- Que dados podem ter sido vistos ou alterados?
- A atividade continua?

### 18.4. Contenção

Reduzir dano:

- Bloquear contas comprometidas.
- Revogar sessões e tokens.
- Isolar sistemas afetados.
- Desativar credenciais expostas.
- Preservar logs.

### 18.5. Erradicação

Remover a causa:

- Corrigir vulnerabilidade.
- Atualizar software.
- Remover malware.
- Alterar segredos.
- Rever permissões.

### 18.6. Recuperação

Voltar ao normal:

- Restaurar serviços.
- Confirmar que a falha foi corrigida.
- Monitorizar atividade.
- Comunicar medidas tomadas.

### 18.7. Lições aprendidas

Depois:

- O que falhou?
- O que funcionou?
- Como detetar mais cedo?
- Que processos devem mudar?
- Que formação é necessária?

---

## 19. Ética e legalidade

Esta parte deve ficar muito clara para os alunos.

Saber como sistemas falham não dá autorização para testar sistemas reais.

Regras:

- Não tentar aceder a contas de outras pessoas.
- Não testar sites, redes ou plataformas sem autorização.
- Não partilhar dados encontrados indevidamente.
- Não divulgar falhas publicamente antes de serem comunicadas de forma responsável.
- Não instalar ferramentas em computadores de terceiros.
- Não usar conhecimento técnico para intimidar, prejudicar ou obter vantagem.

Conduta correta:

- Reproduzir apenas em laboratório autorizado.
- Comunicar falhas a um responsável.
- Guardar evidências mínimas e não invasivas.
- Não aceder a mais dados do que o estritamente necessário para demonstrar a falha.
- Pedir orientação a professores ou responsáveis.

Uma boa frase para a turma:

> Cibersegurança não é sobre provar que conseguimos entrar. É sobre garantir que ninguém entra onde não deve.

---

## 20. Checklist rápida para projetos de alunos

Quando os alunos criarem uma aplicação com login, devem verificar:

- As passwords são guardadas com Argon2id, bcrypt, scrypt ou equivalente?
- Existe HTTPS no ambiente real?
- Os cookies de sessão usam `HttpOnly`, `Secure` e `SameSite`?
- Todos os endpoints protegidos verificam autenticação?
- Todos os endpoints verificam autorização?
- Um utilizador consegue aceder apenas aos seus próprios dados?
- Inputs são validados?
- Erros não revelam informação sensível?
- Tokens expiram?
- Existe forma de terminar sessão?
- Segredos não estão no Git?
- Logs não contêm passwords nem tokens?
- Dependências estão atualizadas?
- Existe backup dos dados importantes?
- Contas administrativas usam MFA?

---

## 21. Glossário

| Termo                  | Explicação curta                                                                 |
| ---------------------- | -------------------------------------------------------------------------------- |
| Autenticação           | Confirmar quem é o utilizador.                                                   |
| Autorização            | Decidir o que o utilizador pode fazer.                                           |
| MFA                    | Autenticação com mais do que um fator.                                           |
| Token                  | Valor usado para representar acesso, identidade ou permissão temporária.         |
| Sessão                 | Estado que permite ao sistema lembrar que o utilizador fez login.                |
| Cookie                 | Pequeno dado guardado pelo browser para um site.                                 |
| JWT                    | Formato de token com header, payload e assinatura.                               |
| Claim                  | Campo dentro de um token, como `sub` ou `exp`.                                   |
| Encriptação            | Transformar dados para que só possam ser lidos com chave.                        |
| Hashing                | Criar uma impressão digital não reversível de dados.                             |
| Salt                   | Valor aleatório usado no hashing de passwords.                                   |
| Pepper                 | Segredo adicional usado no hashing, guardado fora da base de dados.              |
| Phishing               | Tentativa de enganar alguém para revelar informação ou executar ações.           |
| Brute force            | Tentativa de muitas combinações até acertar.                                     |
| Credential stuffing    | Uso de credenciais vazadas de outros serviços.                                   |
| IDOR                   | Falha onde um utilizador acede diretamente a objetos de outro.                   |
| XSS                    | Execução de script malicioso no browser de outro utilizador.                     |
| CSRF                   | Forçar pedidos autenticados a partir do browser da vítima.                       |
| SQL Injection          | Injeção de comandos SQL através de input mal tratado.                            |
| Zero trust             | Modelo que evita confiar automaticamente em redes, dispositivos ou utilizadores. |
| Menor privilégio       | Dar apenas as permissões necessárias.                                            |
| Defesa em profundidade | Usar várias camadas de proteção.                                                 |

---

## 22. Mensagens principais para fechar a aula

- Autenticação prova identidade; autorização controla permissões.
- Tokens são como chaves temporárias: devem ser protegidos e expirar.
- Encriptação protege confidencialidade; hashing serve para verificação e integridade.
- Passwords devem ser guardadas com hashing próprio para passwords, nunca em texto simples.
- O frontend não é uma barreira de segurança.
- A segurança real vive no servidor, nas permissões, nos dados, nos processos e nas pessoas.
- Muitas falhas graves são simples e evitáveis.
- Cibersegurança é uma responsabilidade ética.
- O objetivo de aprender segurança é proteger pessoas, dados e instituições.

![Footer](Images/Footer.png)
