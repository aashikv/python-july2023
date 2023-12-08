import requests
from bs4 import BeautifulSoup
import sqlite3

# Send a GET request to the website
url = "https://example.com"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find elements on the page using CSS selectors
elements = soup.select(".class-name")  # Replace with your desired CSS selector

# Create a connection to the SQLite database
conn = sqlite3.connect("scraped_data.db")
cursor = conn.cursor()

# Create a table in the database to store the scraped data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS scraped_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        attribute_value TEXT,
        text_content TEXT
    )
""")

# Extract data from the elements and insert into the database
for element in elements:
    attribute_value = element["attribute-name"]  # Replace with your desired attribute name
    text_content = element.get_text()  # Get the text content within the element
    
    # Insert data into the database table
    cursor.execute("""
        INSERT INTO scraped_data (attribute_value, text_content)
        VALUES (?, ?)
    """, (attribute_value, text_content))

# Commit changes and close connection to the database
conn.commit()
conn.close()
    
