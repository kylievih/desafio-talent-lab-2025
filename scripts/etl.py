import pandas as pd
import os

# Caminhos das pastas
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'Brazilian E-Commerce Public Dataset by Olist')
OUTPUT_DIR = os.path.join(BASE_DIR, 'processed')

# Garante que a pasta de saída existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Carregando os arquivos
print("📥 Lendo arquivos CSV...")
customers = pd.read_csv(os.path.join(DATA_DIR, 'olist_customers_dataset.csv'))
geolocation = pd.read_csv(os.path.join(DATA_DIR, 'olist_geolocation_dataset.csv'))
orders = pd.read_csv(os.path.join(DATA_DIR, 'olist_orders_dataset.csv'))
order_items = pd.read_csv(os.path.join(DATA_DIR, 'olist_order_items_dataset.csv'))
order_payments = pd.read_csv(os.path.join(DATA_DIR, 'olist_order_payments_dataset.csv'))
order_reviews = pd.read_csv(os.path.join(DATA_DIR, 'olist_order_reviews_dataset.csv'))
products = pd.read_csv(os.path.join(DATA_DIR, 'olist_products_dataset.csv'))
sellers = pd.read_csv(os.path.join(DATA_DIR, 'olist_sellers_dataset.csv'))
categories = pd.read_csv(os.path.join(DATA_DIR, 'product_category_name_translation.csv'))

print("✅ Dados carregados com sucesso.")

# 🔄 JUNÇÃO PRINCIPAL: pedidos + itens + produtos + categorias
print("🔗 Unindo dados...")
df = orders.merge(order_items, on='order_id', how='left') \
           .merge(products, on='product_id', how='left') \
           .merge(categories, on='product_category_name', how='left') \
           .merge(order_reviews, on='order_id', how='left') \
           .merge(order_payments, on='order_id', how='left') \
           .merge(customers, on='customer_id', how='left') \
           .merge(sellers, on='seller_id', how='left')

# 🧹 Transformações
print("🧼 Limpando e processando dados...")

# Converter colunas de data
for col in ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Tempo de entrega real
df['delivery_time_days'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

# Atraso (diferença entre a data estimada e a entrega real)
df['delivery_delay'] = (df['order_delivered_customer_date'] - df['order_estimated_delivery_date']).dt.days
df['was_late'] = df['delivery_delay'] > 0

# Margem bruta (valor - custo do item)
df['gross_margin'] = df['price'] - df['freight_value']

# Agrupar promoções por tempo pode ser feito no notebook, mas aqui preparamos a base

# 📤 Salvando dados prontos para análise
output_path = os.path.join(OUTPUT_DIR, 'ecommerce_data_processed.csv')
df.to_csv(output_path, index=False)
print(f"✅ Arquivo salvo em: {output_path}")
