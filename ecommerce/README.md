# Ecommerce Store

Este é um projeto de e-commerce de roupas desenvolvido com o framework Django. Ele foi criado com o propósito de aprimorar habilidades em Django, Python, lógica de programação e programação orientada a objetos.

---

## Propósito
O principal objetivo deste projeto é desenvolver e consolidar habilidades práticas em:
- **Django**: Framework Python para desenvolvimento web.
- **Python**: Construção de sistemas robustos e escaláveis.
- **Lógica de Programação**: Resolução de problemas e organização de código.
- **Programação Orientada a Objetos (POO)**: Estruturar o sistema de maneira modular e reutilizável.

---

## Problema Resolvido
Este projeto resolve o problema de criar uma aplicação funcional de e-commerce para gerenciar produtos, categorias, variações, usuários e pedidos. Com ele, é possível criar lojas virtuais completas e personalizáveis.

---

## Funcionalidades
- **Gestão de Produtos:** Cadastro, edição e exclusão de produtos.
- **Categorias e Tipos:** Organização dos produtos em categorias e tipos.
- **Carrinho de Compras:** Sistema de adição, remoção e cálculo de preços.
- **Sistema de Usuários:** Registro, login e gerenciamento de contas de cliente.
- **Gerenciamento de Pedidos:** Finalização e histórico de pedidos.
- **Interface Administrativa:** Controle completo pelo Django Admin.

---

## Como Usar
1. Clone este repositório:
   ```bash
   git clone https://github.com/brenpaiva/ecommerce-store.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd ecommerce-store
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor local:
   ```bash
   python manage.py runserver
   ```
6. Acesse o site em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Django**: Framework web para criação da aplicação.
- **SQLite**: Banco de dados utilizado.
- **HTML/CSS/JavaScript**: Frontend para a interface de usuário.

---

## Estrutura do Projeto
```
├── ecommerce
│   ├── loja
│   │   ├── migrations
│   │   ├── templates
│   │   │   ├── interno
│   │   │   └── usuario
│   │   ├── static
│   │   │   ├── css
│   │   │   ├── js
│   │   │   └── images
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   └── settings.py
│   └── urls.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3
```

---

## Links Úteis
- [Documentação do Django](https://docs.djangoproject.com/)
- [Tutorial de Django](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
- [Python](https://www.python.org/)

---

## Como Iniciar o Site
Use o seguinte comando para iniciar o servidor:
```bash
python manage.py runserver
```
Acesse o site localmente em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

Este projeto é uma iniciativa de aprendizado e está em constante evolução. Feedbacks e contribuições são bem-vindos!