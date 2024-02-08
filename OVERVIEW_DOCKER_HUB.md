# Prova de conceito de processo de CI com um script Python, Github Actions e Docker HUB

## Sobre

> Este script Python é um exemplo de um script que poderia ser utilizado em um processo de CI/CD.

O processo aqui realizado foca em um script Python que somente se conecta a um banco de dados e imprime uma variável no console.

O real objetivo deste repositório é demonstrar o processo de CI/CD com Github Actions e Docker HUB. Onde o script Python é utilizado como um exemplo e é executado em um container Docker, que é construído e publicado no Docker HUB por meio das actions automaticamente.

## Como usar essa imagem

### Você pode executar o container com o comando:

```bash
docker run --name python_example -e NAME=SEU_NOME -e  DATABASE_USER=USUARIO -e DATABASE_PASSWORD=SENHA -e DATABASE_HOST=HOST -e DATABASE_PORT=PORTA mugarate12/ci_python_script:latest
```

### Ou você pode utilizar o docker-compose:

```yaml
version: '3.8'

services:
  python_example:
    image: mugarate12/ci_python_script:latest
    environment:
      - NAME=SEU_NOME
      - DATABASE_USER=USUARIO
      - DATABASE_PASSWORD=SENHA
      - DATABASE_HOST=HOST
      - DATABASE_PORT=PORTA
```

### Variáveis de ambiente

- `NAME` - Nome que será impresso no console.
- `DATABASE_USER` - Usuário do banco de dados.
- `DATABASE_PASSWORD` - Senha do banco de dados.
- `DATABASE_HOST` - Host do banco de dados.
- `DATABASE_PORT` - Porta do banco de dados.

## Links úteis

- [Repositório](https://github.com/mugarate12/ci_python_script)