﻿# trabalho_linguagem_natural_Bimestre1


PRÉ-REQUISITOS
Python 3.8 ou 3.9 (Rasa ainda não é totalmente compatível com versões acima de 3.10)

VS Code instalado

Terminal com pip funcionando

Rasa SDK instalado


INSTALAR RASA E DEPENDÊNCIAS

pip install "rasa==3.1.0
pip install rasa-sdk

INICIAR O SERVIDOR DE AÇÕES
Dentro da pasta do projeto pelo terminal do vscode

entrar na pasta actions
executar o comando: .\venv\Scripts\Activate.ps1
e depois o comando: rasa run actions

TREINAR O MODELO
abra outro terminal no vscode mesmo, na pasta raiz do projeto

Treinar primeiro:
executar o comando: .\venv\Scripts\Activate.ps1
depois o comando: rasa train

Executar os testes:
rasa shell
