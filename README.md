# Pandas 2025

Este repositório contém códigos e exemplos práticos de uso da biblioteca **pandas** para análise de dados em Python. O material está organizado por dias de estudo e aborda desde operações básicas com **Series** até manipulação de **DataFrames** e leitura de arquivos externos.

## Estrutura do projeto

- **dia01/**: introdução ao pandas, criação de `Series`, manipulação de índices e primeiros passos com `DataFrame`.
- **dia02/**: leitura de arquivos CSV e Excel, uso de dados copiados da área de transferência, extração de tabelas da web e inspeção de colunas.
- **data/**: pasta reservada para conjuntos de dados utilizados nos exemplos.

Cada arquivo Python possui células indicadas por `# %%`, permitindo execução interativa em editores compatíveis com o padrão de *notebooks*.

## Pré‑requisitos

- Python 3.10 ou superior
- Biblioteca `pandas`

Para instalar as dependências principais, utilize:

```bash
pip install pandas
```

## Executando os exemplos

A forma mais simples é abrir os arquivos `.py` em um editor que suporte blocos interativos, como VS Code ou Jupyter. Também é possível executá‑los diretamente pelo terminal:

```bash
python dia01/02_series.py
```

Os scripts dentro de `dia02/` geram arquivos como `customers.xlsx` e `unidades_federativas.csv`. Eles servem como exemplos de como exportar e importar dados em diferentes formatos.

## Licença

Este projeto é distribuído sob a licença MIT.

