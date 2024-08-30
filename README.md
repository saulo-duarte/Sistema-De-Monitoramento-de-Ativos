# Sistema de Monitoramento de Ativos Financeiros

## Objetivo

O objetivo deste projeto é criar um sistema de monitoramento de ativos financeiros, que permita a visualização de informações de ativos financeiros em tempo real. O sistema é capaz de consumir informações de ativos financeiros de uma API da yahoo finance, carregar essas informações no snowflake, criar um data lake com uma arquitetura medalion e disponibilizar essas informações em uma aplicação web.

## Indice

## Estrutura do Projeto

```
├── src
│   ├── app
│   ├── configs
│   │   ├── rules
│   │   │   └── rules.py
│   │   └── tools
│   │       └── snowflake.py
│   └── data_acquisition
│       └── data_collection.py
│       └── data_validation.py
│       └── data_ingestion.py
└── pyproject.toml
```
## Arquitetura

![Arquitetura](media/financial_arch.svg)