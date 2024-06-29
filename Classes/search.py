import sqlite3

#sqlite for temporary purposes
#find out how django works with sqlite
#   no me gusta leer documentación  <-- hilarious, dave :) -Tracie

def search_customers(search_term: str) -> list:
    conn: sqlite3.Connection = sqlite3.connect('customer_management.db')
