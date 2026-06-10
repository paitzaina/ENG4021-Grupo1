# Mindly

## Projeto Integrado de Software — ENG4021 · PUC-Rio · 2026.1

> "Acalme sua mente a qualquer momento, da onde estiver."

[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-orange.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
![Contributors](https://img.shields.io/github/contributors/paitzaina/ENG4021-Grupo1)
![Last Commit](https://img.shields.io/github/last-commit/paitzaina/ENG4021-Grupo1)
![Repo Size](https://img.shields.io/github/repo-size/paitzaina/ENG4021-Grupo1)

![HTML](https://img.shields.io/badge/language-HTML-brown.svg)
![Python](https://img.shields.io/badge/language-Python-yellow.svg)
![CSS](https://img.shields.io/badge/language-CSS-red.svg)
![Top Language](https://img.shields.io/github/languages/top/paitzaina/ENG4021-Grupo1)
![Languages Count](https://img.shields.io/github/languages/count/paitzaina/ENG4021-Grupo1)

![Django](https://img.shields.io/badge/framework-Django-092E20?style=flat-square&logo=django&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

![Course](https://img.shields.io/badge/Course-ENG4021-blue)
![Institution](https://img.shields.io/badge/Institution-PUC--Rio-003366)
![Semester](https://img.shields.io/badge/Semester-2026.1-lightgrey)

![GitHub stars](https://img.shields.io/github/stars/paitzaina/ENG4021-Grupo1?style=social)
![GitHub forks](https://img.shields.io/github/forks/paitzaina/ENG4021-Grupo1?style=social)

---

## Integrantes

![Imagem com os contribuidores](https://contrib.rocks/image?repo=paitzaina/ENG4021-Grupo1&anon=0&columns=25&max=100&r=true)

Bruno Moreno · Gabriela Riva · Letícia Torquato · Lucas Lourenzzo · Paula Itzaina

---

## Sobre o projeto

O **Mindly** é um site de apoio à saúde mental voltado para jovens universitários.
O objetivo é oferecer suporte acessível para quem enfrenta ansiedade, estresse e depressão no dia a dia acadêmico.

O site é organizado em cinco áreas:

- **Diário** — registro emocional por data, para identificar padrões e gatilhos
- **Exercícios** — técnicas de respiração, relaxamento e meditação guiada
- **Dicas** — conteúdo por categoria: ansiedade, estresse, foco/estudos e sono
- **Notícias** — feed de artigos sobre saúde mental
- **Crise** — suporte imediato: mensagem motivadora, exercício guiado, contato do CVV (188)

- [home.html — tela inicial](Codigo/core/templates/core/home.html) _(o código ainda exibe o nome "MindApp" pois o nome não havia sido definido na época do desenvolvimento — o nome oficial do projeto é Mindly, atualização pendente)_

---

## Pesquisa e validação

- [Resumo das entrevistas com usuários](Midia/resumo%20entrevistas.txt)
- [Validação das 20 hipóteses](Documentos/Valida%C3%A7%C3%A3o%2020%20hip%C3%B3teses)
- [Melhores ideias do brainstorm](Documentos/Melhores%20ideias%20do%20brainstorm.txt)
- [Análise dos produtos similares](Documentos/An%C3%A1lise%20dos%20produtos%20similares.txt)

---

## Design e identidade visual

- [Definição da identidade visual](Documentos/Defini%C3%A7%C3%A3o%20da%20identidade%20visual)
- [Fluxograma de telas](Documentos/fluxograma)
- [Diferencial do projeto](Midia/diferencial%20do%20projeto.txt)
- [Origem e significado do nome Mindly](https://github.com/leticiatorquato24/ENG4021-Grupo1/blob/main/Midia/Mindly.txt) _(aguardando merge)_
- Telas no Figma — _a commitar_

---

## Documentação técnica

- [Escopo técnico e viabilidade](Documentos/Escopo%20Tecnico%20Viabilidade.txt)
- [Implementações diferenciais em relação aos concorrentes](Documentos/definirImplementacoes.txt)
- [Impactos sociais negativos da aplicação](Documentos/Impactos%20Sociais%20Negativos%20da%20Aplicacao)
- [Possibilidades de crescimento e ampliação](Documentos/Possibilidades%20de%20Crescimento%20e%20Ampliacao%20da%20Aplicacao)
- [Estratégia para atrair usuários](https://github.com/brunomlima9/ENG4021-Grupo1/blob/main/estrategia_atrair_usuarios) _(aguardando merge)_
- [Implementação da estratégia de atração de usuários](https://github.com/brunomlima9/ENG4021-Grupo1/blob/main/implementar_estrategia_atrair_usuarios) _(aguardando merge)_

---

## Código

### Views e rotas

- [views.py — home, diário, exercícios, dicas, notícias, crise](Codigo/core/views.py)
- [urls.py — roteamento das páginas](Codigo/core/urls.py)

### Templates HTML

- [home.html](Codigo/core/templates/core/home.html) _(exibe "MindApp" — pendente atualização para "Mindly")_
- [diario.html](Codigo/core/templates/core/diario.html)
- [exercicios.html](Codigo/core/templates/core/exercicios.html)
- [dicas.html](Codigo/core/templates/core/dicas.html)
- [noticias.html](Codigo/core/templates/core/noticias.html)
- [crise.html](Codigo/core/templates/core/crise.html)

### Estilos

- [style.css](Codigo/core/static/core/css/style.css)

### Modelos de dados

- [models — Notícia](https://github.com/gabiriva/ENG4021-Grupo1/blob/main/models%20noticia) _(aguardando merge)_
- [models — Dica](https://github.com/gabiriva/ENG4021-Grupo1/blob/main/models%20dica) _(aguardando merge)_
- [models — Exercício](https://github.com/gabiriva/ENG4021-Grupo1/blob/main/models%20exercicio) _(aguardando merge)_
- [models — Usuário](https://github.com/leticiatorquato24/ENG4021-Grupo1/blob/main/Codigo/models.py) _(aguardando merge)_
- [models — Diário](https://github.com/leticiatorquato24/ENG4021-Grupo1/blob/main/Codigo/diario.py) _(aguardando merge)_
- [models — Crise](https://github.com/leticiatorquato24/ENG4021-Grupo1/blob/main/Codigo/crise.py) _(aguardando merge)_

### Dependências e configuração

- [requirements.txt](Codigo/requirements.txt)
- [settings.py](Codigo/mindapp_project/settings.py)

---
