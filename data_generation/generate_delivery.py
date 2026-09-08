import random 
import pandas as pd
from datetime import datetime, timedelta


# Read orders
orders_df = pd.read_csv(
    r'C:\Users\kalpa\OneDrive\Desktop\Codebasics\02. DATABRICKS\Ecommerce_databricks\Ecommerce\batch_data\orders.csv'
)


# No of Deliveries
deliveries =[]

no_of_deliveries = len(orders_df)

delivery_partners = ['Delhivery','Blue Dart','Ecom Express','DTDC','XpressBees']

delivery_statuses = ['Delivered','In Transit','Out for Delivery','Delayed','Failed']


for delivery_id in range(1, no_of_deliveries+1):

    order = orders_df.iloc[delivery_id-1]

    # Select delivery status
    delivery_status = random.choice(delivery_statuses)

    # Convert order_date from string to datetime
    order_date = datetime.strptime(order['order_date'],'%Y-%m-%d')


    # Estimated delivery: 2 to 7 days after order
    estimated_delivery_date = order_date + timedelta(
        days=random.randint(2, 7)
                )

    # Actual delivered date only if delivered
    if delivery_status == 'Delivered':
        # Actual delivery can be before, on, or after estimated date
        delivered_date = estimated_delivery_date + timedelta(
            days=random.randint(-1, 3)
        )
        delivered_date = delivered_date.strftime('%Y-%m-%d')

    else:
        delivered_date = None


    deliveries.append({
            'delivery_id' : f'DLV{delivery_id:05d}',
            'order_id': order['order_id'],
            'order_date' : order['order_date'],
            'estimated_delivery_date': estimated_delivery_date.strftime('%Y-%m-%d'),
            'delivered_date': delivered_date,
            'delivery_partner' : random.choice(delivery_partners),
            'delivery_status' : delivery_status
            })

# Convert to Dataframe
delivery_df = pd.DataFrame(deliveries)

# Save CSV
delivery_df.to_csv(
    r'C:\Users\kalpa\OneDrive\Desktop\Codebasics\02. DATABRICKS\Ecommerce_databricks\Ecommerce\batch_data\delivery.csv',
    index=False
            )

    
print(f"Generated {len(delivery_df)} delivery records")
print("File saved successfully!")

print("\nSample Data:")
print(delivery_df.sample(5))