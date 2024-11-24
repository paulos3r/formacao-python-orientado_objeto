# Formação python orientado a objeto Alura

Este repositório contém dois ambientes distintos para a execução dos serviços com `Docker Compose`. A estrutura é organizada em duas pastas:

## Estrutura do Projeto

```bash
.
├── sabor-express/
│   └── docker-compose.yaml
└── README.md
```

## Como subir os ambientes

### Ambiente da Aula

Para iniciar o ambiente, siga os passos abaixo:

1. Navegue até a pasta sabor-express:

```bash
cd sabor-express
```

2. Execute o comando para subir os containers:

```bash
docker-compose up -d
```

3. Após o término da aula, para parar e remover os containers, execute:

```bash
docker-compose down
```

### Rodando os testes

1. Execute o comando no terminal do container:

```bash
pytest
```

### Observações

- Certifique-se de ter o Docker instalado na sua máquina antes de rodar os comandos.
- Para mais informações sobre o Docker, consulte os tutoriais.
- Sinta-se à vontade para consultar o ambiente referencial.
