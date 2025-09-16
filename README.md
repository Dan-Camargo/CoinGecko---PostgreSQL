# Ingestão de Dados da CoinGecko para PostgreSQL

Este projeto é um script em Python que busca taxas de câmbio de criptomoedas da [CoinGecko API](https://www.coingecko.com/pt/api) e insere os dados em um banco de dados PostgreSQL.
O projeto está em desenvolvimento, com o objetivo de criar um banco de dados robusto que poderá ser analisado futuramente usando **Pandas**, **Power BI** ou outras ferramentas de visualização de dados.

---

## Conteúdo

- [Funcionalidades](#funcionalidades)
- [Capturas de Tela](#capturas-de-tela) (A adicionar)
- [Requisitos](#requisitos)
- [Configuração](#configuração)
- [Uso](#uso)
- [Próximos Passos](#próximos-passos)
  
---

## Funcionalidades

- Busca taxas de câmbio de criptomoedas em tempo real na CoinGecko.
- Insere os dados na tabela PostgreSQL chamada `projeto`.
- Cria automaticamente a tabela caso ela não exista.
- Armazena dados com timestamp para análise histórica.
- Projetado para ser expansível para outras fontes de dados.
- Suporta uso de `.env` para gerenciar de forma segura credenciais e chaves de API.
  
---

## Requisitos

- Python 3.9+
- PostgreSQL 12+ (ou compatível)
- Bibliotecas Python:
  - `requests`
  - `pandas`
  - `sqlalchemy`
  - `psycopg2-binary`
  - `python-dotenv`

Instale as dependências com:

```bash
pip install -r requirements.txt
