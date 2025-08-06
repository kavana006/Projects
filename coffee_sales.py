import csv
from datetime import datetime
from collections import defaultdict

def load_data(file_path):
    data = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # Parse date and datatime 
                date = datetime.strptime(row['date'], '%Y-%m-%d').date()
                dt = datetime.strptime(row['datetime'], '%Y-%m-%d %H:%M:%S')
                money = float(row['money'])
                coffee = row['coffee_name']
                cash_type = row['cash_type']
                data.append((date, dt.hour, coffee, money, cash_type))
            except Exception as e:
                print("Skipping row due to error:", e)
    return data

def summarize_sales(data):
    coffee_totals = defaultdict(float)
    hourly_sales = defaultdict(int)
    payment_methods = defaultdict(int)
    total_sales = 0

    for (date, hour, coffee, money, cash_type) in data:
        coffee_totals[coffee] += money
        hourly_sales[hour] += 1
        payment_methods[cash_type] += 1
        total_sales += money

    return coffee_totals, hourly_sales, payment_methods, total_sales

def print_report(coffee_totals, hourly_sales, payment_methods, total_sales):
    print("\n=== Coffee Sales Summary ===")
    print(f"Total Revenue: ₹{total_sales:.2f}\n")

    print("Sales by Coffee Type:")
    for coffee, amount in sorted(coffee_totals.items(), key=lambda x: -x[1]):
        print(f"  {coffee:20s} ₹{amount:.2f}")

    print("\nSales by Hour of Day:")
    for hour in range(24):
        count = hourly_sales.get(hour, 0)
        print(f"  Hour {hour:02d}: {count} sales")

    print("\nPayment Method Breakdown:")
    for method, count in payment_methods.items():
        print(f"  {method.title():6s}: {count} transactions")

# Main 
if __name__ == "__main__":
    file_path = "coffee_sales.csv"
    data = load_data(file_path)
    coffee_totals, hourly_sales, payment_methods, total_sales = summarize_sales(data)
    print_report(coffee_totals, hourly_sales, payment_methods, total_sales)
