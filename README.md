# API de Gerenciamento de Carros com Django e Django REST Framework

Este projeto é uma API RESTful desenvolvida com **Django** e **Django REST Framework**, permitindo o gerenciamento de informações sobre carros associados a usuários registrados. A API suporta operações CRUD (Create, Read, Update, Delete) e implementa autenticação JWT para garantir a segurança das operações.

---

## Índice

- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Execução](#execução)
- [Endpoints da API](#endpoints-da-api)

---

## Funcionalidades

- **CRUD completo para o modelo Car**
  - Criar, listar, detalhar, atualizar e deletar carros.
- **Associação de carros a usuários registrados**
  - Cada carro está vinculado a um usuário (proprietário).
- **Autenticação e autorização utilizando JWT**
  - Proteção de endpoints sensíveis com tokens de acesso.
- **Implementação do padrão CQRS**
  - Separação de comandos (Commands) e consultas (Queries).
- **Permissões personalizadas**
  - Apenas proprietários podem editar ou deletar seus carros.
- **Organização modular do código**
  - Views organizadas em subpastas para melhor manutenção.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Frameworks:**
  - Django 5.x
  - Django REST Framework [ DRF ]
- **Autenticação:**
  - Django REST Framework Simple JWT
- **Banco de Dados:**
  - SQLite (padrão do Django)
- **Ambiente Virtual:**
  - `venv`

---

## Pré-requisitos

Antes de começar, certifique-se de ter instalado em seu sistema:

- **Python 3.x**
- **Git**

---

## Instalação

Siga os passos abaixo para configurar o ambiente e executar o projeto localmente.

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie um Ambiente Virtual

Crie e ative um ambiente virtual para isolar as dependências do projeto.
No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as Dependências

Instale as dependências necessárias utilizando o pip:

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
```

### 4. Realize as Migrações do Banco de Dados

Aplique as migrações para criar as tabelas no banco de dados:

```bash
python manage.py migrate
```

---

## Estrutura do Projeto

├── core/
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── api/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── permissions.py
│ ├── serializers.py
│ ├── urls.py
│ ├── views/
│ │ ├── **init**.py
│ │ ├── car_views.py
│ │ └── user_views.py
│ └── migrations/
│ ├── **init**.py
│ └── 0001_initial.py
├── manage.py
├── requirements.txt
└── README.md

---

## Execução

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

O servidor estará disponível em http://127.0.0.1:8000/.

---

## Endpoints da API

### **Endpoints de Carros**

- **Listar Carros**

  - **URL:** `/api/cars/`
  - **Método:** GET
  - **Descrição:** Obtém a lista de todos os carros.

- **Detalhar Carro**

  - **URL:** `/api/cars/<int:pk>/`
  - **Método:** GET
  - **Descrição:** Obtém detalhes de um carro específico.

- **Criar Carro**

  - **URL:** `/api/cars/create/`
  - **Método:** POST
  - **Autenticação:** Necessária
  - **Descrição:** Adiciona um novo carro vinculado ao usuário autenticado.

- **Atualizar Carro**

  - **URL:** `/api/cars/<int:pk>/update/`
  - **Método:** PUT/PATCH
  - **Autenticação:** Necessária
  - **Permissão:** Somente proprietário
  - **Descrição:** Atualiza informações de um carro específico.

- **Deletar Carro**
  - **URL:** `/api/cars/<int:pk>/delete/`
  - **Método:** DELETE
  - **Autenticação:** Necessária
  - **Permissão:** Somente proprietário
  - **Descrição:** Remove um carro específico.

### **Endpoints de Usuários**

- **Listar Usuários**

  - **URL:** `/api/users/`
  - **Método:** GET
  - **Descrição:** Obtém a lista de todos os usuários.

- **Detalhar Usuário**
  - **URL:** `/api/users/<int:pk>/`
  - **Método:** GET
  - **Descrição:** Obtém detalhes de um usuário específico, incluindo seus carros.

### **Endpoints de Autenticação**

- **Obter Token**

  - **URL:** `/api/token/`
  - **Método:** POST
  - **Descrição:** Gera um par de tokens JWT (access e refresh).

- **Atualizar Token**
  - **URL:** `/api/token/refresh/`
  - **Método:** POST
  - **Descrição:** Atualiza o token de acesso utilizando o token de refresh.
