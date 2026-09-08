import random
import pandas as pd
from faker import Faker 


fake = Faker('en-IN')

num_of_products = 1000

products=[]

categories = { "Electronics": ["Laptops","Smartphones","Tablets","Headphones","Cameras","Smartwatches","Televisions","Gaming Consoles"],
            "Clothing": ["T-Shirts","Shirts","Jeans","Trousers","Jackets","Dresses","Sarees","Shoes"],
            "Home & Kitchen": ["Furniture","Cookware","Kitchen Appliances","Bedding","Home Decor","Storage","Lighting"],
            "Beauty & Personal Care": ["Skincare","Makeup","Hair Care","Fragrances","Bath & Body","Grooming"],
            "Sports & Fitness": ["Running","Cricket","Football","Gym Equipment","Yoga","Cycling","Outdoor Recreation"],
            "Books": ["Fiction","Non-Fiction","Science","History","Biography","Self-Help","Children's Books"],
            "Grocery": ["Fruits & Vegetables","Snacks","Beverages","Dairy","Bakery","Staples","Frozen Foods"],
            "Toys & Games": ["Action Figures","Board Games","Puzzles","Educational Toys","Dolls","Remote Control Toys"]
}

for product_id in range(1, num_of_products+1):

    category = random.choice(list(categories.keys()))
    sub_category = random.choice(categories[category])
    products.append({
            'product_id': f'PRD{product_id:04d}',
            'brand' : fake.company(),
            'category' : category,
            'sub_category' : sub_category,
            'price' : round(random.uniform(100, 500000),2),
            'rating' : round(random.uniform(1, 5), 1),
            'review_count' : random.randint(0,5000)
})


products_df = pd.DataFrame(products)

# Save CSV
products_df.to_csv(r'C:\Users\kalpa\OneDrive\Desktop\Codebasics\02. DATABRICKS\Ecommerce_databricks\Ecommerce\batch_data\products.csv', index=False)

print(f"Generated {len(products)} products record")
print('File saved successfully')
print('\nSample Data:')

print(products_df.head())


