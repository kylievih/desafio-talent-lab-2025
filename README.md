# 🚀 Desafio Talent Lab 2025 — Dados que Transformam

Este repositório contém a solução desenvolvida por **Glauber Patrik** para o **Desafio "Dados que Transformam" da Talent Lab 2025**, utilizando dados públicos do e-commerce brasileiro (projeto Olist).

---

## 🧠 Objetivo

Realizar um pipeline completo de **ETL (Extração, Transformação e Carga)**, seguido de **Análise Exploratória de Dados (EDA)** com visualizações para responder a perguntas estratégicas de negócio. Todo o processo foi documentado, automatizado em Python e estruturado em um repositório limpo e modular.

---

## 🛠️ Ferramentas Utilizadas

- Python 3.13
- Pandas, NumPy
- Matplotlib, Seaborn, Plotly
- Jupyter Notebook
- Visual Studio Code
- Git e GitHub

---

## 🧱 Estrutura do Projeto

```bash
📦 desafio_talent_lab/
├── 📂 data/                      # Dados originais CSV (Olist)
├── 📂 processed/                 # Dados tratados prontos para análise
├── 📂 scripts/
│   └── etl.py                   # Script de limpeza e transformação (ETL)
├── 📂 notebooks/
│   ├── eda.ipynb                # Notebook com visualizações e análises
│   └── eda.html                 # Versão navegável do notebook
├── requirements.txt             # Bibliotecas utilizadas
└── README.md                    # Este arquivo

```

## 🔍 Questões de Análise Respondidas

De acordo com o desafio, uma questão de cada bloco temático foi selecionada e resolvida:

Tópico Questão Respondida

📦 1. Análise de Performance de Vendas:

- a. Volume de Vendas por Categoria

🚚 2. Análise de logística:

- a. Prazos de Entrega

⭐ 3. Análise de Satisfação do Cliente

- b. Impacto dos Atrasos na Satisfação do Cliente

💰 4. Análise Financeira

- a. Análise de Lucratividade por Categoria

📈 5. Análise de Marketing

- b. Eficácia de Campanhas Promocionais

## 📊 Visualizações Geradas

Gráfico de barras com as 10 categorias que mais vendem.

Histograma com a distribuição dos prazos de entrega.

Boxplot da nota dos clientes com e sem atraso na entrega.

Gráfico de lucratividade (margem bruta) por categoria.

Linha temporal da evolução de vendas mês a mês.

## ⚙️ Como Executar o Projeto

1. Clone este repositório
   git clone https://github.com/kylievih/desafio-talent-lab-2025.git
   cd desafio-talent-lab-2025
2. Crie um ambiente virtual (opcional, mas recomendado)
   python -m venv .venv
   .venv\Scripts\activate # Windows
   source .venv/bin/activate # macOS/Linux
3. Instale as dependências
   pip install -r requirements.txt
4. Execute o script de ETL
   python scripts/etl.py
5. Inicie o Jupyter Notebook
   jupyter notebook notebooks/eda.ipynb
   📄 Acesso Rápido à Análise
   📂 Veja a versão visual da análise aqui:
   👉 notebooks/eda.html

## 📌 Observações Técnicas

Os dados utilizados são públicos e vêm do dataset da Olist (via Kaggle).

A estrutura foi pensada para facilitar reuso e leitura de código.

O ETL transforma e unifica os dados em um único .csv para análise.

Todas as análises estão em Jupyter Notebook com visualizações explicativas.

## 🧑‍💻 Autor

Glauber Patrik
Estudante de Engenharia de Software — ICET/UFAM
