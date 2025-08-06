import csv
from datetime import datetime
from statistics import mean

# Step 1: Load a csv file
def load_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                date = datetime.strptime(row['Date'], '%Y-%m-%d')
                close = float(row['Close'])
                data.append((date, close))
            except ValueError:
                continue 
    return data

# Step 2: Compute Simple Moving Average (SMA)
def compute_sma(data, window):
    sma = []
    for i in range(len(data)):
        if i >= window - 1:
            window_prices = [price for (_, price) in data[i-window+1:i+1]]
            avg = mean(window_prices)
            sma.append((data[i][0], avg))
        else:
            sma.append((data[i][0], None))  # Not enough data
    return sma

# Step 3: Displays the results
def display_summary(data, sma20, sma50, last_n=10):
    print(f"{'Date':<12} {'Close':>10} {'SMA20':>10} {'SMA50':>10}")
    print("-" * 44)
    start = max(0, len(data) - last_n)
    for i in range(start, len(data)):
        date_str = data[i][0].strftime('%Y-%m-%d')
        close = f"{data[i][1]:.2f}"
        s20 = f"{sma20[i][1]:.2f}" if sma20[i][1] is not None else "N/A"
        s50 = f"{sma50[i][1]:.2f}" if sma50[i][1] is not None else "N/A"
        print(f"{date_str:<12} {close:>10} {s20:>10} {s50:>10}")

# Main Program
if __name__ == "__main__":
    file_path = "coca_cola.csv"  # Make sure this file is in same folder
    stock_data = load_data(file_path)

    # Optional: print how many rows were loaded
    print(f"Loaded {len(stock_data)} rows from CSV.\n")

    sma_20 = compute_sma(stock_data, 20)
    sma_50 = compute_sma(stock_data, 50)
    
    display_summary(stock_data, sma_20, sma_50, last_n=15)
