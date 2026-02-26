import sqlite3

conn = sqlite3.connect("data/sample.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    price REAL,
    date TEXT
)
""")

sample_data = [
    ("Laptop", "Electronics", 5, 70000, "2024-01-10"),
    ("Mobile", "Electronics", 10, 30000, "2024-01-12"),
    ("Headphones", "Accessories", 15, 2000, "2024-01-15"),
    ("Keyboard", "Accessories", 7, 1500, "2024-01-18"),
]

cursor.executemany(
    "INSERT INTO sales (product, category, quantity, price, date) VALUES (?, ?, ?, ?, ?)",
    sample_data
)

conn.commit()
conn.close()

print("Database initialized successfully")