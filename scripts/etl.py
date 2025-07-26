import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'Brazilian E-Commerce Public Dataset by Olist')
OUTPUT_DIR = os.path.join(BASE_DIR, 'processed')

os.makedirs(OUTPUT_DIR, exist_ok=True)

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

print("🔗 Unindo dados...")
df = orders.merge(order_items, on='order_id', how='left') \
           .merge(products, on='product_id', how='left') \
           .merge(categories, on='product_category_name', how='left') \
           .merge(order_reviews, on='order_id', how='left') \
           .merge(order_payments, on='order_id', how='left') \
           .merge(customers, on='customer_id', how='left') \
           .merge(sellers, on='seller_id', how='left')

print("🧼 Limpando e processando dados...")

for col in ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']:
    df[col] = pd.to_datetime(df[col], errors='coerce')

df['delivery_time_days'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days

df['delivery_delay'] = (df['order_delivered_customer_date'] - df['order_estimated_delivery_date']).dt.days
df['was_late'] = df['delivery_delay'] > 0

df['gross_margin'] = df['price'] - df['freight_value']

output_path = os.path.join(OUTPUT_DIR, 'ecommerce_data_processed.csv')
df.to_csv(output_path, index=False)
print(f"✅ Arquivo salvo em: {output_path}")
