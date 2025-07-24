# 🚀 Desafio Talent Lab 2025 — Dados que Transformam

Este repositório contém a solução desenvolvida por [Seu Nome Aqui] para o **Desafio "Dados que Transformam" da Talent Lab 2025**, utilizando dados públicos do e-commerce brasileiro (Olist).

---

## 🧠 Objetivo

Realizar um pipeline completo de **ETL (Extração, Transformação e Carga)**, seguido de **Análise Exploratória de Dados (EDA)** para responder perguntas de negócio a partir de dados reais do e-commerce nacional.

---

## 🛠️ Ferramentas Utilizadas

- Python 3.13
- Pandas, Numpy
- Matplotlib, Seaborn, Plotly
- Jupyter Notebook
- VSCode / PyCharm
- Git e GitHub

---

## 🧱 Estrutura do Projeto

📦 desafio_talent_lab/
├── 📂 data/ # Dados originais CSV (Olist)
├── 📂 processed/ # Dados tratados prontos para análise
├── 📂 scripts/
│ └── etl.py # Script de limpeza e transformação
├── 📂 notebooks/
│ └── eda.ipynb # Análises exploratórias por bloco
├── README.md # Este arquivo
├── requirements.txt # Bibliotecas necessárias

---

## 🔍 Questões de Análise Respondidas

Conforme solicitado no desafio, foi escolhida **uma pergunta por bloco temático**, totalizando 5 análises:

| Tópico                   | Questão                                                |
| ------------------------ | ------------------------------------------------------ |
| 📦 Performance de Vendas | Volume de vendas por categoria                         |
| 🚚 Logística             | Prazos médios de entrega e fatores que causam atrasos  |
| ⭐ Satisfação do Cliente | Relação entre atrasos e avaliações negativas           |
| 💰 Financeiro            | Lucratividade por categoria de produto                 |
| 📈 Marketing             | Eficácia de campanhas promocionais no volume de vendas |

---

## ⚙️ Como Executar o Projeto

### 1. Clone este repositório

```bash
git clone https://github.com/seu-usuario/desafio-talent-lab-2025.git
cd desafio-talent-lab-2025
```

2. Crie um ambiente virtual (opcional, mas recomendado)
   python -m venv venv
   venv\Scripts\activate # Windows
   source venv/bin/activate # macOS/Linux
3. Instale as dependências
   pip install -r requirements.txt
4. Execute o ETL
   python scripts/etl.py
5. Execute a análise
   Abra o notebook:
   jupyter notebook notebooks/eda.ipynb

## 📌 Observações Técnicas

1. Todos os dados utilizados são públicos (Olist, disponíveis no Kaggle).
2. Os dados foram limpos, integrados e transformados no arquivo etl.py.
3. As visualizações estão concentradas em eda.ipynb.
4. O projeto preza pela legibilidade do código e pela clareza das análises.

## 🧑‍💻 Autor

Glauber Patrik
Estudante de Engenharia de Software | UFAM
