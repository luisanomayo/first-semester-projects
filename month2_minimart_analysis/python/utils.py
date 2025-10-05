# Utility functions for data conversion and filtering

from datetime import datetime

#customer, product and orders data

customers = {
    1: {"name": "Alice Johnson", "email": "alice.johnson@example.com"},
    2: {"name": "Brian Smith", "email": "brian.smith@example.com"},
    3: {"name": "Cynthia Lee", "email": "cynthia.lee@example.com"},
    4: {"name": "Daniel Perez", "email": "daniel.perez@example.com"},
    5: {"name": "Emma Brown", "email": "emma.brown@example.com"}
}

products = {
    1: {"product_name": "Wireless Mouse", "category": "Electronics", "price": 24.99},
    2: {"product_name": "Laptop Stand", "category": "Accessories", "price": 42.50},
    3: {"product_name": "Coffee Mug", "category": "Kitchen", "price": 9.99},
    4: {"product_name": "Notebook (A5)", "category": "Stationery", "price": 5.25},
    5: {"product_name": "Bluetooth Headphones", "category": "Electronics", "price": 79.00},
    6: {"product_name": "Water Bottle", "category": "Fitness", "price": 15.49},
    7: {"product_name": "Yoga Mat", "category": "Fitness", "price": 25.00},
    8: {"product_name": "Mechanical Keyboard", "category": "Electronics", "price": 99.00},
    9: {"product_name": "Portable Charger", "category": "Electronics", "price": 35.75},
    10: {"product_name": "Desk Lamp", "category": "Home Decor", "price": 28.50}
}

orders = {
    21: {"customer_id": 2, "product_id": 3, "quantity": 2, "order_date": "2025-10-01"},
    22: {"customer_id": 1, "product_id": 5, "quantity": 4, "order_date": "2025-10-01"},
    23: {"customer_id": 3, "product_id": 1, "quantity": 3, "order_date": "2025-10-02"},
    24: {"customer_id": 4, "product_id": 2, "quantity": 1, "order_date": "2025-10-02"},
    25: {"customer_id": 5, "product_id": 7, "quantity": 2, "order_date": "2025-10-03"},
    26: {"customer_id": 1, "product_id": 9, "quantity": 1, "order_date": "2025-10-03"},
    27: {"customer_id": 2, "product_id": 6, "quantity": 2, "order_date": "2025-10-04"},
    28: {"customer_id": 3, "product_id": 4, "quantity": 4, "order_date": "2025-10-04"},
    29: {"customer_id": 4, "product_id": 8, "quantity": 2, "order_date": "2025-10-05"},
    30: {"customer_id": 5, "product_id": 10, "quantity": 1, "order_date": "2025-10-05"},
    31: {"customer_id": 2, "product_id": 2, "quantity": 1, "order_date": "2025-10-06"},
    32: {"customer_id": 1, "product_id": 1, "quantity": 2, "order_date": "2025-10-06"},
    33: {"customer_id": 3, "product_id": 5, "quantity": 1, "order_date": "2025-10-07"},
    34: {"customer_id": 4, "product_id": 7, "quantity": 2, "order_date": "2025-10-07"},
    35: {"customer_id": 5, "product_id": 3, "quantity": 3, "order_date": "2025-10-08"},
    36: {"customer_id": 1, "product_id": 6, "quantity": 1, "order_date": "2025-10-08"},
    37: {"customer_id": 2, "product_id": 10, "quantity": 1, "order_date": "2025-10-09"},
    38: {"customer_id": 3, "product_id": 8, "quantity": 2, "order_date": "2025-10-09"},
    39: {"customer_id": 4, "product_id": 9, "quantity": 1, "order_date": "2025-10-10"},
    40: {"customer_id": 5, "product_id": 4, "quantity": 2, "order_date": "2025-10-10"}
}

def large_orders(orders:dict, products:dict, flag:float):
    """
    Identify orders where the total price exceeds the given threshold.
    """
    for order_id, order in orders.items():
        product_id = order["product_id"]
        quantity = order["quantity"]
        total_price = products[product_id]["price"] * quantity
        
        if total_price > flag:
            print(f"Large order placed: Order ID {order_id}, Total Price: ${total_price:.2f}")
            
            
#currency conversion and discount application

def currency_conversion_and_discount(order:dict, products:dict, exchange_rate:float, discount_rate:float, currency_symbol:str):
    """
    Convert product prices from base currency to another currency and apply a discount
    Adds 'price_new_currency' and 'final_price' to each order in the orders dictionary.
    """
    for order in orders.values():
        product_id = order["product_id"]
        quantity = order["quantity"]
        price_base_currency = products[product_id]["price"]
    
        
        # Convert to new currency
        price_new_currency = price_base_currency * exchange_rate
        # Update order with new pricing details
        order['price_new_currency'] = round(price_new_currency, 2)
    
        #introduce discount for orders on saturday
        order_date = datetime.strptime(order['order_date'], "%Y-%m-%d").date()
        order_day = order_date.strftime("%A")
        
        if order_day == "Saturday":
            final_price = round(order['price_new_currency'] * (1 - discount_rate), 2)
        else:
            final_price = round(price_new_currency, 2)

        #save final price to order
        order['final_price'] = final_price
        order['currency_symbol'] = currency_symbol