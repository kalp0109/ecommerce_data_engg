import pandas as pd
import random
from datetime import datetime , timedelta

# Read customers and products
customers_df = pd.read_csv(
    r'C:\Users\kalpa\OneDrive\Desktop\Codebasics\02. DATABRICKS\Ecommerce_databricks\Ecommerce\batch_data\customers.csv'
)

products_df = pd.read_csv(
    r'C:\Users\kalpa\OneDrive\Desktop\Codebasics\02. DATABRICKS\Ecommerce_databricks\Ecommerce\batch_data\products.csv'
)

# No of orders
no_of_orders = 10000

orders =[]

start_date = datetime(2025, 1, 1)
end_date = datetime(2025,12,31)
payment_methods = ['UPI','Credit Card','Debit Card','Net Banking','Cash on Delivery']
order_statuses = ['Delivered','Shipped','Processing','Cancelled']



for order_id in range(1, no_of_orders+1):

    # Random Customer
    customer = customers_df.sample(1).iloc[0]

    # Random Product
    product = products_df.sample(1).iloc[0]

    # Random order date
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between) 
    order_date = start_date + timedelta(days=random_days)

    orders.append({
            'order_id' : f'ORD{order_id:05d}',
            'customer_id' : customer['customer_id'],
            'product_id' : product['product_id'],
            'order_date' : order_date.strftime('%Y-%m-%d'),
            'qty' : random.randint(1, 10),
            'unit_price' : product['price'],
            'payment_method' : random.choice(payment_methods),
            'order_status' : random.choice(order_statuses)

     })



# Convert Dataframe
orders_df = pd.DataFrame(orders)

# Saving CSV 
orders_df.to_csv(r'C:\Users\kalpa\OneDrive\Desktop\Codebasics\02. DATABRICKS\Ecommerce_databricks\Ecommerce\batch_data\orders.csv', index=False)
print(f"Generated {len(orders)} orders record")
print('File saved successfully')
print('\nSample Data:')
print(products_df.sample(5))
