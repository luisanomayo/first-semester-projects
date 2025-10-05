# Entry point for the MiniMart data reporting system

from utils import customers, products, orders
from utils import large_orders, currency_conversion_and_discount
from report_generator import generate_report

def main():
    print("🛒 Welcome to the MiniMart Data Reporting System")
    
    #collect input from user
    exchange_rate = 3.64
    discount_rate = 0.10
    currency_symbol = 'AED'
    large_order_flag = 100.00
    
    # Identify large orders
    print(f"\nChecking for large orders (over ${large_order_flag})...")
    large_orders(orders, products, flag=large_order_flag)
    
    # Apply currency conversion and discounts
    print("\nApplying currency conversion and discounts...")
    currency_conversion_and_discount(orders, products, exchange_rate, discount_rate, currency_symbol)
    
    # Generate and display report
    print("\nGenerating report...")
    report = generate_report(orders, products, customers, currency_symbol)

    print("\n--- MiniMart Report ---")
    print(f"Total Products Sold: {report['total_products_sold']}")
    print(f"Most Popular Product: {report['most_popular_product']}")
    print("Revenue per Customer:")
    for customer, revenue in report['revenue_per_customer'].items():
        print(f" - {customer}: {currency_symbol}{revenue:.2f}")
    
    print("\nThank you for using the MiniMart Data Reporting System!")  

if __name__ == "__main__":
    main()