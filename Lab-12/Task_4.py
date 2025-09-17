import random
import time
import heapq

class Stock:
    """Represents a stock with its daily price data and percentage change."""
    def __init__(self, symbol, open_price, close_price):
        self.symbol = symbol
        self.open_price = open_price
        self.close_price = close_price
        self.change = self.calculate_percentage_change()

    def calculate_percentage_change(self):
        """Calculates the percentage change from open to close price."""
        if self.open_price == 0:
            return float('inf') if self.close_price > 0 else float('-inf')
        return ((self.close_price - self.open_price) / self.open_price) * 100

    def __repr__(self):
        return f"Stock(Symbol='{self.symbol}', Change={self.change:.2f}%)"

def generate_stock_data(num_stocks):
    """Simulates a list of stock data for a given number of stocks."""
    stocks = []
    for i in range(num_stocks):
        symbol = f"SYM{i:04d}"
        open_price = round(random.uniform(10, 500), 2)
        change_factor = random.uniform(0.95, 1.05)
        close_price = round(open_price * change_factor, 2)
        stocks.append(Stock(symbol, open_price, close_price))
    return stocks

# --- 1. Heap Sort Implementation ---
def heap_sort(stocks):
    """Sorts a list of stocks by percentage change using Heap Sort (max-heap)."""
    n = len(stocks)

    # Build a max-heap (rearranging the list)
    # The heap is built on the 'change' attribute
    for i in range(n // 2 - 1, -1, -1):
        heapify(stocks, n, i)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        stocks[i], stocks[0] = stocks[0], stocks[i]  # Move current root to end
        heapify(stocks, i, 0) # Call max heapify on the reduced heap
    
    # The list is now sorted in ascending order. Reverse it for descending.
    return stocks[::-1]

def heapify(arr, n, i):
    """Helper function for Heap Sort to maintain the heap property."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left].change > arr[largest].change:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right].change > arr[largest].change:
        largest = right

    # If the largest element is not the root, swap and heapify the sub-tree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# --- 2. Hash Map Implementation ---
def build_stock_hash_map(stocks):
    """Creates a hash map for O(1) lookups by stock symbol."""
    stock_map = {}
    for stock in stocks:
        stock_map[stock.symbol] = stock
    return stock_map

def search_stock_by_symbol(stock_map, symbol):
    """Retrieves a stock object from the hash map."""
    return stock_map.get(symbol)

# --- Main Program Execution and Comparison ---
if __name__ == "__main__":
    NUM_STOCKS = 50000
    
    # Simulate stock data
    print(f"Generating data for {NUM_STOCKS} stocks...")
    stock_data = generate_stock_data(NUM_STOCKS)

    # --- Sorting Performance Comparison ---
    print("\n--- Sorting Performance ---")
    
    # Custom Heap Sort
    heap_sort_data = list(stock_data)
    start_time_heap = time.perf_counter()
    heap_sorted_stocks = heap_sort(heap_sort_data)
    end_time_heap = time.perf_counter()
    print(f"Heap Sort took: {end_time_heap - start_time_heap:.6f} seconds")

    # Standard Library Sort (Timsort)
    start_time_lib = time.perf_counter()
    lib_sorted_stocks = sorted(stock_data, key=lambda s: s.change, reverse=True)
    end_time_lib = time.perf_counter()
    print(f"Python's sorted() took: {end_time_lib - start_time_lib:.6f} seconds")

    print("\n--- Top 10 Stocks by Performance (using sorted list) ---")
    for i, stock in enumerate(lib_sorted_stocks[:10]):
        print(f"{i+1}. {stock}")

    # --- Searching Performance Comparison ---
    print("\n--- Searching Performance ---")
    
    # Build the hash map
    start_time_build = time.perf_counter()
    stock_map = build_stock_hash_map(stock_data)
    end_time_build = time.perf_counter()
    print(f"Hash Map build time: {end_time_build - start_time_build:.6f} seconds")

    # Test lookup for a specific symbol
    search_symbol = stock_data[random.randint(0, NUM_STOCKS - 1)].symbol
    start_time_search = time.perf_counter()
    found_stock = search_stock_by_symbol(stock_map, search_symbol)
    end_time_search = time.perf_counter()
    print(f"Hash Map lookup for '{search_symbol}' took: {end_time_search - start_time_search:.9f} seconds")
    if found_stock:
        print(f"  Found Stock: {found_stock}")
    
    # Standard dictionary lookup for comparison
    start_time_dict = time.perf_counter()
    dict_found = stock_map.get(search_symbol)
    end_time_dict = time.perf_counter()
    print(f"Standard dict lookup took: {end_time_dict - start_time_dict:.9f} seconds")
    
    # --- Analysis ---
    print("\n--- Analysis of Trade-offs ---")
    print("Sorting:")
    print("  Timsort (Python's built-in sorted()) is highly optimized and often outperforms a pure Heap Sort for typical datasets.")
    print("  Heap Sort has a guaranteed O(n log n) worst-case time complexity, making it a reliable choice for any data distribution.")
    print("Searching:")
    print("  Hash Maps (dictionaries) provide constant time (O(1)) average-case lookups, which is crucial for real-time systems where speed is critical.")
    print("  The trade-off is the initial time and memory required to build the hash map, but this cost is quickly recouped by the speed of subsequent searches.")














    