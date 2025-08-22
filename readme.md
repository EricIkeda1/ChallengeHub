# ChallengeHub

## Objetivo do Projeto

O **ChallengeHub** é uma plataforma web desenvolvida em **Python e Django** com o objetivo de criar um ambiente interativo para praticar e melhorar habilidades de programação. O projeto permite que usuários participem de **mini desafios de código**, submetam suas soluções e acompanhem seu desempenho através de pontuação e conquistas.

### Ideia Inicial

A ideia é oferecer uma plataforma simples e divertida onde desenvolvedores, estudantes ou qualquer pessoa interessada em programação possa:  

- Criar uma conta e se autenticar.  
- Navegar por uma lista de desafios de diferentes níveis de dificuldade (fácil, médio, difícil).  
- Submeter soluções para os desafios diretamente no site.  
- Receber feedback imediato sobre o código submetido (correto/incorreto).  
- Acumular pontos, desbloquear conquistas e acompanhar seu ranking.  

O projeto tem potencial para evoluir incluindo:  
- Sistema de criação de novos desafios pelos usuários.  
- Editor de código online mais avançado, com destaque de sintaxe.  
- Salas de competição e mini torneios entre usuários.  
- Sistema de badges e conquistas visuais para engajar os participantes.  

---

## Tecnologias Utilizadas

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Banco de Dados:** SQLite (ou outro a escolha)  
- **Controle de Versão:** Git  

---

## Estrutura Inicial

```
ChallengeHub
 ┣ challenges
 ┃ ┣ migrations
 ┃ ┃ ┗ __init__.py
 ┃ ┣ admin.py
 ┃ ┣ apps.py
 ┃ ┣ models.py
 ┃ ┣ tests.py
 ┃ ┣ views.py
 ┃ ┗ __init__.py
 ┣ code_challenges
 ┃ ┣ __pycache__
 ┃ ┃ ┣ settings.cpython-312.pyc
 ┃ ┃ ┗ __init__.cpython-312.pyc
 ┃ ┣ asgi.py
 ┃ ┣ settings.py
 ┃ ┣ urls.py
 ┃ ┣ wsgi.py
 ┃ ┗ __init__.py
 ┣ .gitignore
 ┣ LICENSE
 ┣ manage.py
 ┗ readme.md

```