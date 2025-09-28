# Ingestão de Dados da CoinGecko para PostgreSQL

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)

Este projeto se consiste em scripts Python que buscam taxas de câmbio de criptomoedas da [CoinGecko API](https://www.coingecko.com/pt/api) e inserem os dados em um banco de dados PostgreSQL.
O objetivo é construir um banco de dados histórico que será posteriormente analisado usando **Pandas**, **Power BI** e outras ferramentas de visualização (Atualmente **METABASE** foi escolhido por ser open-source).

---

## Conteúdo

* [Funcionalidades](#funcionalidades)
* [Capturas de Tela](#capturas-de-tela)
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

## Capturas de Tela

Captura para demonstrar a quantidade de ingestões feitas:

![Count Rows](https://i.imgur.com/T0gYf5j.png)


VSCode durante desenvolvimento:

![VS-Code](https://i.imgur.com/cQnE7wM.png)


Execução de um Join para demonstrar a modelagem de dados

![Join](https://i.imgur.com/uDpfKce.png)

Metabase Hosteado localmente utilizando Docker + VSCode:

![Metabase+VSCode](https://i.imgur.com/aBCy28p.png)

Dashboard Metabase:

![Dashboard](https://i.imgur.com/228pl7z.png)

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

Execute o script de ingestão:

```bash
python ingest.py
```

* O script fará 10 requisições à API da CoinGecko, com intervalo de 10 segundos entre cada.
* Os dados serão inseridos na tabela `projeto`.
* Opcional: descomente `df.to_csv()` para salvar os dados localmente em CSV.

---

Execute o script de modelagem de banco:

```bash
python database_model.py
```


* Insere os dados do CSV na tabela `currency_metadata`.  
* Define `unit` como chave primária em currency_metadata.  
* Cria chave estrangeira `unit` em `projeto` referenciando `currency_metadata(unit)`.

---

## Próximos Passos / Roadmap

* Expandir o banco de dados com mais fontes de dados de criptomoedas e financeiras. - EM PROGRESSO
* Realizar análise exploratória usando **Pandas** e gerar gráficos informativos.
* Integrar com **Power BI** ou **Metabase** (preferencial por ser open-source) para dashboards e observabilidade avançada dos dados.
* Possível automação futura com agendamento de pipelines para atualização contínua.
