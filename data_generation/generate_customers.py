from faker import Faker
import random
import pandas as pd


fake = Faker('en_IN')


# No of Customers
no_of_customers = 5000

customers =[]

for customer_id in range(1,no_of_customers+1):

    customers.append({
        'customer_id' : f'CST{customer_id:04d}',
        'customer_name' : fake.name(),
        'email': fake.email(),
        'phone' : fake.phone_number(),
        'city' : fake.city(),
        'state' : fake.state(),
        'pincode' : fake.postcode(),
        'signup_date' : fake.date_between(start_date = '-3y', end_date ='today'),
        'signup_channel' : random.choice(["organic", "paid_search", "social", "referral", "email"]),
         "customer_segment": random.choice([
            "Regular",
            "Premium",
            "VIP"]),
        "is_active": random.choice([True, True, True, False])
    })

# Create Dataframe
customers_df = pd.DataFrame(customers)


# Save CSV
customers_df.to_csv(
    r'C:\Users\kalpa\OneDrive\Desktop\Codebasics\02. DATABRICKS\Ecommerce_databricks\Ecommerce\batch_data\customers.csv',
    index=False
)

print(f'Generated {len(customers_df)} customer records.')
print('File saved successfully')
print('\nSample Data:')

print(customers_df.head())

