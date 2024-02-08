# Prova de conceito de processo de CI com um script Python, Github Actions e Docker HUB

> Este script Python é um exemplo de um script que poderia ser utilizado em um processo de CI/CD.

## Pré-requisitos

- [Acesso aos recursos de git hub actions](https://docs.github.com/pt/actions)
- [Acesso aos recursos do Docker HUB](https://docs.docker.com/docker-hub/)

## Sobre

O processo aqui realizado foca em um script Python que somente se conecta a um banco de dados e imprime uma variável no console. 

O real objetivo deste repositório é demonstrar o processo de CI/CD com Github Actions e Docker HUB. Onde o script Python é utilizado como um exemplo e é executado em um container Docker, que é construído e publicado no Docker HUB por meio das actions automaticamente.