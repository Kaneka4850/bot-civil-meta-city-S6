# 🚔 Bot Civil — MetaCity S6

Bot de gerenciamento interno da **Polícia Civil** do servidor de GTA RP **MetaCity**, desenvolvido com `discord.py 2.x`. Automatiza fluxos administrativos da corporação: cadastro de oficiais, registro de ações, sistema disciplinar, corregedoria, cursos e muito mais.

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Requisitos](#requisitos)
- [Instalação e Configuração](#instalação-e-configuração)
- [Comandos Disponíveis](#comandos-disponíveis)
- [Cogs (Módulos)](#cogs-módulos)
- [Banco de Dados](#banco-de-dados)
- [Aviso de Segurança](#aviso-de-segurança)

---

## Visão Geral

O bot gerencia toda a burocracia interna da corporação diretamente pelo Discord, eliminando processos manuais. Cada módulo (cog) é independente e cobre uma área específica da administração policial.

---

## Funcionalidades

| Módulo | Descrição |
|---|---|
| 🪪 Cadastro | Registro e aprovação de novos recrutas com atribuição automática de cargo e apelido |
| ⚠️ Advertências | Sistema de penalidades em 4 níveis com atribuição de cargos e log automático |
| 🎯 Registro de Ações | Painel para registro de operações táticas com controle de vagas e participação |
| 📊 Status de Ações | Estatísticas globais e ranking individual de participação em ações |
| 🔒 Registro de Prisão | Formulário guiado por canal temporário com upload de provas fotográficas |
| 🕵️ Corregedoria | Sistema de tickets para denúncias internas com transcript automático ao fechar |
| 📚 Cursos | Agendamento e inscrição em cursos com controle por cargo e fila de espera |
| 🗓️ Alinhamento | Convocação formal de oficiais para reuniões com notificação por DM |
| 🚪 Ausência | Formulário de solicitação de afastamento com registro em canal de logs |
| 📂 Provas | Criação de categoria individual para upload de evidências de provas |

---

## Estrutura do Projeto

```
Bot civil meta city s6/
├── main.py                         # Ponto de entrada, carregamento de cogs e eventos
├── .env                            # Variáveis de ambiente (token do bot)
├── .gitattributes
│
├── cogs/                           # Módulos de funcionalidades
│   ├── acao.py                     # Registro de ações táticas
│   ├── advertencia.py              # Sistema disciplinar de advertências
│   ├── alinhamento.py              # Convocação para alinhamentos/reuniões
│   ├── ausencia.py                 # Solicitação de ausência
│   ├── cadastro.py                 # Registro e aprovação de recrutas
│   ├── corregedoria.py             # Sistema de tickets de corregedoria
│   ├── cursos.py                   # Gerenciamento de cursos
│   ├── provas.py                   # Criação de abas individuais de provas
│   ├── registro_prisao.py          # Formulário de registro de prisões
│   └── status_acao.py              # Estatísticas e ranking de ações
│
├── data/                           # Camada de acesso a dados (SQLAlchemy)
│   ├── crud.py                     # Operações CRUD genéricas
│   ├── db_session.py               # Gerenciamento de sessões
│   └── db_setup.py                 # Setup do engine SQLAlchemy
│
├── database/                       # Modelos e serviços de domínio
│   ├── membro_service.py           # Modelos Membro, Prisão, Advertência
│   ├── adevertencia_service.py     # Helpers de advertência
│   ├── corregedoria_service.py     # Helpers de corregedoria
│   └── prisao_service.py           # Helpers de prisão
│
├── services/
│   └── membro_service.py           # Serviço de membros (SQLite direto)
│
├── interfaces/
│   └── views/
│       └── menu_persistente.py     # View persistente de menu
│
└── eventos.db                      # Banco SQLite de eventos
```

---

## Requisitos

- Python **3.10+**
- Dependências listadas abaixo

```
discord.py>=2.3.0
python-dotenv
sqlalchemy
aiohttp
chat-exporter
```

> **Instale com:**
> ```bash
> pip install -r requirements.txt
> ```

---

## Instalação e Configuração

**1. Clone o repositório**
```bash
git clone https://github.com/SEU_USUARIO/bot-civil-metacity.git
cd bot-civil-metacity
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Configure o arquivo `.env`**

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
DISCORD_TOKEN=seu_token_aqui
```

> ⚠️ **NUNCA suba o arquivo `.env` para o repositório.** Certifique-se que `.env` está no `.gitignore`.

**4. Configure os IDs no código**

Cada cog possui uma seção de constantes no topo do arquivo com os IDs do servidor (canais, cargos, categorias). Substitua pelos IDs do seu servidor antes de iniciar:

```python
# Exemplo em advertencia.py
CARGOS_PERMITIDOS   = [ID_DO_CARGO_AQUI]
CANAL_PENALIDADES_ID = ID_DO_CANAL_AQUI
CANAL_LOG_ADV_ID     = ID_DO_CANAL_LOG_AQUI
```

**5. Inicie o bot**
```bash
python main.py
```

---

## Comandos Disponíveis

| Comando | Permissão | Descrição |
|---|---|---|
| `!setup_provas` | Administrador | Cria o painel permanente de provas |
| `!setup_registro` | Administrador | Cria o painel de cadastro de recrutas |
| `!painel_acao` | Administrador | Cria o painel de registro de ações táticas |
| `!listar_registros` | Todos | Lista todos os registros aprovados |
| `!setup_ausencia` | Administrador | Cria o menu de solicitação de ausência |
| `!setup_cursos` | Administrador | Cria o menu de gerenciamento de cursos |
| `!demitir` | Administrador | Exonera um agente da corporação |
| `!convocar` | Perm. Advertência | Convoca um membro para alinhamento |
| `!advertir` | Perm. Advertência | Aplica uma advertência a um membro |
| `!prisao` | Curso de Prisão | Abre formulário guiado de registro de prisão |
| `!status_acao` | Todos | Exibe estatísticas globais por tipo de ação |
| `!status_membro [@usuário]` | Todos | Ranking top-15 ou ficha individual de membro |
| `!setup_status` | Administrador | Posta o embed global de estatísticas no canal |
| `!sync_acoes [N]` | Administrador | Importa histórico retroativo de ações (padrão: 200 msgs) |
| `!comandos` | Todos | Lista todos os comandos disponíveis |

---

## Cogs (Módulos)

### 🪪 `cadastro.py`
Gerencia o fluxo completo de admissão de novos oficiais. Ao se registrar, o candidato preenche um formulário com nome, ID, telefone e usuário. O registro aguarda aprovação de um membro com o cargo de recrutamento. Ao aprovar, o bot atribui automaticamente o cargo de Polícia Civil e formata o apelido no padrão `ID | Nome`.

### ⚠️ `advertencia.py`
Sistema disciplinar com 4 níveis de advertência (ADV1 a ADV4), onde ADV4 resulta em exoneração imediata. O aplicador preenche um modal com o ID do oficial, tipo, duração (opcional, em dias) e motivo. O bot atribui o cargo correspondente, registra no canal de penalidades e envia log detalhado.

### 🎯 `acao.py`
Painel de registro de operações táticas com view persistente. Inclui botões para **Confirmar Participação** e **Cancelar Confirmação**, com controle de vagas (formato `X/Y`). O embed da ação é enviado automaticamente para o canal de registro configurado.

### 📊 `status_acao.py`
Dependente do cog `acao.py`. Mantém um banco SQLite (`acoesmembros.db`) com todas as participações. Oferece:
- `!status_acao` — embed global com wins/losses por tipo de ação (Banco Central, Nióbio, Joalheria etc.)
- `!status_membro` — ranking top-15 ou ficha individual com histórico por tipo de ação
- `!setup_status` — embed fixo de estatísticas globais em canal dedicado
- `!sync_acoes` — importação retroativa de histórico de mensagens

### 🔒 `registro_prisao.py`
Formulário de prisão conduzido em canal temporário privado. O fluxo guiado coleta: suspeito, crime, local, data/hora e **fotos de evidências** (com download e re-upload para evitar URLs expiradas). Ao finalizar, o canal temporário é deletado e o relatório é enviado ao canal de registro.

### 🕵️ `corregedoria.py`
Sistema completo de tickets internos. Ao abrir um ticket, o usuário preenche um modal com categoria e descrição da denúncia. Proteção contra tickets duplicados. Botões de controle: **Solicitar**, **Assumir**, **Fechar** e **Pokar**. Ao fechar, gera um transcript HTML via `chat_exporter` e tenta enviá-lo por DM ao requerente antes de excluir o canal.

### 📚 `cursos.py`
Instrutores com o cargo correspondente agendam cursos via modal (nome, ID do cargo, data, hora, local). O bot cria um embed de aviso no canal de cursos e uma fila de solicitação para os interessados. Controle de permissão por cargo e proteção contra escalada de privilégios.

### 🗓️ `alinhamento.py`
Permite convocar um oficial para reunião via modal com ID do agente, data e horário. Valida os formatos `DD/MM/AAAA` e `00h00 / 00:00`. Envia um embed no canal de alinhamento com menção ao convocado e registra a ação no canal de logs.

### 🚪 `ausencia.py`
Modal com QRA, data de início, data de término e motivo. Valida as datas no formato `DD/MM/YYYY`. Envia um embed de registro no canal de logs da corporação.

### 📂 `provas.py`
Ao clicar no botão, cria automaticamente uma categoria privada com o nome do oficial, contendo os canais: `identidade`, `chat`, `provas` e `boletins-de-ocorrencia`. Acesso restrito ao oficial e ao bot.

---

## Banco de Dados

O projeto utiliza dois mecanismos de persistência:

**SQLAlchemy + SQLite** — para membros, advertências e prisões (`oficiais-policia-civil.db`):

| Tabela | Campos |
|---|---|
| `membros` | `id`, `nome`, `user_id`, `telefone`, `usuario`, `discord_id`, `aprovado` |

**SQLite direto** — para estatísticas de ações (`acoesmembros.db`):

| Tabela | Campos |
|---|---|
| `participacoes` | `id`, `discord_id`, `tipo_acao`, `resultado` (win/loss), `timestamp`, `message_id` |

**JSON** — estatísticas globais cacheadas em `acoes_stats.json`.

---

## Aviso de Segurança

> ⚠️ O arquivo `.env` original **não deve ser incluído no repositório**. Caso o token já tenha sido exposto, **revogue-o imediatamente** no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications) e gere um novo.

Adicione ao `.gitignore`:

```
.env
*.db
__pycache__/
*.pyc
```

---

