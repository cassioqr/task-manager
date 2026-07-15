# TechFlow Task Manager

## 📖 Sobre o Projeto

*Este é um projeto feito por Cassio Queiroz de Resende para matéria de Software Engineering pela Unifecaf*

O TechFlow Task Manager é um sistema web de gerenciamento de tarefas desenvolvido como atividade prática da disciplina de Engenharia de Software.

O projeto simula uma solução para uma startup de logística que necessita acompanhar o andamento das tarefas da equipe em tempo real, permitindo organizar atividades, acompanhar seu progresso e melhorar a produtividade utilizando metodologias ágeis.

---

## 🎯 Objetivo

Desenvolver um sistema web simples para gerenciamento de tarefas aplicando conceitos de Engenharia de Software, incluindo:

- Controle de versão com Git e GitHub;
- Desenvolvimento utilizando metodologia ágil;
- Organização das atividades através de um quadro Kanban;
- Testes automatizados;
- Integração contínua utilizando GitHub Actions.

---

## 📋 Escopo Inicial

O sistema possui as seguintes funcionalidades:

- Criar tarefas;
- Listar tarefas;
- Editar tarefas;
- Excluir tarefas.

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Flask
- SQLite
- HTML5
- CSS3
- Git
- GitHub
- GitHub Actions
- Pytest

---

## 📌 Metodologia Ágil

O desenvolvimento foi baseado na metodologia Kanban.

As tarefas foram organizadas no GitHub Projects utilizando três colunas:

- To Do
- In Progress
- Done

Essa organização facilita o acompanhamento das atividades durante todo o desenvolvimento.

---

## 📂 Estrutura do Projeto

```
task-manager/
│
├── app.py
├── README.md
├── requirements.txt
├── src/
├── templates/
├── static/
├── tests/
├── docs/
└── .github/
    └── workflows/
```

---

## ▶ Como executar

Clone o repositório:

```bash
git clone https://github.com/cassioqr/task-manager.git
```

Entre na pasta:

```bash
cd task-manager
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o sistema:

```bash
python app.py
```

---

## 🔄 Mudança de Escopo

Durante o desenvolvimento foi adicionada uma nova funcionalidade para permitir que as tarefas possuam prioridade (Baixa, Média e Alta).

Essa alteração foi realizada para melhorar a organização das atividades e representar uma mudança de escopo típica de projetos ágeis.

---

## ✅ Testes

Os testes automatizados são executados utilizando Pytest.

Sempre que um novo código é enviado ao GitHub, o GitHub Actions executa automaticamente os testes para garantir que o sistema continue funcionando corretamente.

---

## 👨‍💻 Autor

Projeto desenvolvido por Cassio Queiroz de Resende para a disciplina de Software Engineering pela Unifecaf.