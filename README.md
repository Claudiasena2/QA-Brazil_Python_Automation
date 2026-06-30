# Automação de Testes Web com Python e Selenium WebDriver 🚀

Este repositório contém o projeto prático de automação de testes de ponta a ponta (E2E) para uma aplicação web, aplicando as melhores práticas de engenharia de qualidade de software.

## 🎯 Objetivos do Projeto
* Automatizar os fluxos críticos de utilizador (User Stories) e validação de regras de negócio.
* Garantir a integridade da interface gráfica (GUI), validação de campos obrigatórios e tratamento de erros.
* Implementar testes de regressão eficientes e de rápida execução.

## 🏗️ Arquitetura e Padrões de Projeto
O projeto foi estruturado utilizando o padrão **Page Object Model (POM)** para garantir a manutenibilidade, reutilização de código e separação clara entre a lógica dos testes e os elementos da interface:
* `pages.py`: Mapeamento de elementos web e interações de página.
* `data.py`: Centralização de massas de dados de teste e payloads.
* `helpers.py`: Funções utilitárias e configurações de suporte.
* `main.py`: Scripts de execução dos cenários de teste automatizados.

## 🛠️ Tecnologias e Frameworks
* **Linguagem Principal:** Python 3
* **Framework de Testes:** Pytest
* **Ferramenta de Automação:** Selenium WebDriver
* **Gestão de Dependências:** pip (através do arquivo `requirements.txt`)
* **Controle de Versão:** Git / GitHub

## 🚀 Como Executar o Projeto Localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a suíte de testes com o Pytest:
   ```bash
   pytest main.py
   ```
