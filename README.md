# Ingestão de Dados da CoinGecko para PostgreSQL

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)

Este projeto é um script Python que busca taxas de câmbio de criptomoedas da [CoinGecko API](https://www.coingecko.com/pt/api) e insere os dados em um banco de dados PostgreSQL.
O objetivo é construir um banco de dados histórico que será posteriormente analisado usando **Pandas**, **Power BI** e outras ferramentas de visualização.

---

## Conteúdo

* [Funcionalidades](#funcionalidades)
* [Capturas de Tela](#capturas-de-tela) (A adicionar)
* [Requisitos](#requisitos)
* [Configuração](#configuração)
* [Uso](#uso)
* [Próximos Passos](#próximos-passos)

---

## Funcionalidades

* Busca taxas de câmbio de criptomoedas em tempo real na CoinGecko.
* Insere dados na tabela PostgreSQL `projeto`.
* Cria automaticamente a tabela caso não exista.
* Armazena dados com timestamp para análises históricas.
* Suporta múltiplas fontes futuras de dados.
* Usa `.env` para gerenciamento seguro de credenciais e API keys.

---

## Requisitos

* Python 3.9+
* PostgreSQL 12+ (ou compatível)
* Bibliotecas Python:

  * `requests`
  * `pandas`
  * `sqlalchemy`
  * `psycopg2-binary`
  * `python-dotenv`

Instale todas as dependências com:

```bash
pip install -r requirements.txt
```

---

## Configuração

1. Clone o repositório:

```bash
git clone <URL-do-seu-repositorio>
cd CoinGecko-PostgreSQL
```

2. Crie um arquivo `.env` na raiz do projeto:

```env
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=host_do_banco
DB_PORT=5432
DB_NAME=postgres
COINGECKO_KEY=sua_chave_api
```

---

## Uso

Execute o script Python:

```bash
python ingest.py
```

* O script fará 10 requisições à API da CoinGecko, com intervalo de 10 segundos entre cada.
* Os dados serão inseridos na tabela `projeto`.
* Opcional: descomente `df.to_csv()` para salvar os dados localmente em CSV.

---

## Próximos Passos / Roadmap

* Expandir o banco de dados com mais fontes de dados de criptomoedas e financeiras.
* Criar tabelas com métricas derivadas e rastreamento histórico detalhado.
* Realizar análise exploratória usando **Pandas** e gerar gráficos informativos.
* Integrar com **Power BI** para dashboards e observabilidade avançada dos dados.
* Otimizar ETL para grandes volumes de dados, garantindo performance e consistência.
* Possível automação futura com agendamento de pipelines para atualização contínua.
