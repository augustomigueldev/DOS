# Projeto Django — Task Manager

Sistema completo de gerenciamento de tarefas desenvolvido em **Python/Django**, com autenticação de usuários, controle de prioridades e fluxo completo de CRUD (criar → visualizar → editar → priorizar → concluir).

## ✨ Funcionalidades

- 🔒 **Autenticação e isolamento de dados** — Cada usuário só enxerga e gerencia as próprias tarefas
- 🗂️ **Criação de tarefas** — Com título, descrição, data-limite e prioridade
- 🎯 **Sistema de prioridade** — Baixa, Média e Alta com badges coloridos
- ✅ **Marcação de conclusão** — Concluir e reabrir tarefas com um clique
- 🔍 **Filtros** — Exibir todas, apenas pendentes ou apenas concluídas
- 🖊️ **Edição completa** — Todos os campos editáveis, incluindo status e prioridade
- 👁️ **Página de detalhe** — Clique na tarefa para ver e agir sobre ela
- 🗑️ **Exclusão** — Com confirmação para evitar erros

## 🖥️ Demonstração da Aplicação Rodando

Abaixo está uma imagem real do sistema funcionando localmente:

![Projeto Rodando](screenshot.png)

---

## 🤔 Por que Django e não HTML/CSS/JS puro?

Esta é uma decisão **técnica e estratégica**, não uma simples preferência. Veja o comparativo:

| Necessidade              | HTML/CSS/JS puro         | Django (framework)                     |
|--------------------------|--------------------------|----------------------------------------|
| Rotas e URLs             | Manual e repetitivo      | ✅ Sistema de rotas embutido           |
| Banco de dados           | Precisa de backend extra | ✅ ORM integrado (SQLite, PostgreSQL…) |
| Autenticação             | Do zero, complexo        | ✅ Sistema pronto e seguro             |
| Validação de formulários | JavaScript manual        | ✅ Validação server-side automática    |
| CSRF Protection          | Implementar manualmente  | ✅ Proteção embutida por padrão        |
| Manutenção e escalabilidade | Difícil               | ✅ Estrutura MVC organizada            |

> **Conclusão:** O Django reduz drasticamente o tempo de desenvolvimento ao evitar que o programador reinvente funcionalidades básicas. Mesmo num projeto aparentemente simples como um To-Do, a escolha do framework é uma **decisão de engenharia** que visa criar um sistema mais robusto, seguro, reutilizável e escalável — diferente de uma página estática sem persistência de dados ou segurança real.

---

## Guia de Comandos Rápidos (Cheat Sheet)

Aqui estão listados os principais comandos utilizados no ciclo de vida de um projeto em Django. Útil tanto para referência no Linux quanto no Windows:

**1 - Criar ambiente virtual**
```bash
python3 -m venv venv
```

**2 - Ativar ambiente virtual (Linux / macOS)**
```bash
source venv/bin/activate
```

**2.1 - Ativar ambiente virtual (Windows)**
```bash
.\venv\Scripts\activate
```

**3 - Instalar Django**
```bash
pip install django
```
*(Para instalar as versões exatas desse projeto, use `pip install -r requirements.txt`)*

**3.1 - Verificar a instalação do pip e pacotes (Exportar)**
```bash
pip freeze
```

**4 - Criar projeto (do zero)**
```bash
django-admin startproject nome_do_projeto
```

**5 - Rodar o servidor**
*((Lembre-se de estar na mesma pasta do arquivo `manage.py`))*
```bash
python3 manage.py runserver
```

**6 - Mudar a porta do servidor**
```bash
python3 manage.py runserver 8080
```

**7 - Criar aplicação app**
```bash
python3 manage.py startapp nome_do_app
```

**8 - Criação das tabelas no banco de dados e alterações no esquema do bd**
```bash
python3 manage.py migrate
```

**9 - Mudança na estrutura de modelos do app**
```bash
python3 manage.py makemigrations nome_do_app
```

**10 - Comando para verificar problemas no projeto**
```bash
python3 manage.py check
```

**11 - Shell do python (Django)**
```bash
python3 manage.py shell
```

**12 - Comando para criar usuário administrador**
```bash
python3 manage.py createsuperuser
```

**13 - Comando para baixar DB-Browser (No Linux Ubuntu/Debian)**
```bash
sudo apt-get update
sudo apt-get install sqlitebrowser
```

*(Obs: Dependendo de como o Python está instalado no seu Windows, os comandos que começam com `python3` ou `python3 -m` devem ser usados apenas como `python`).*
