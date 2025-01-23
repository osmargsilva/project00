import psycopg2 as psq

conn = psq.connect(
    database="cursoPy",
    user="gomes",
    password="gomes123",
    host="147.79.111.150",
    port=5435
)


# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create produtos table
cur.execute("""CREATE TABLE IF NOT EXISTS produtos(
            id SERIAL PRIMARY KEY,
            codido VARCHAR (255) UNIQUE NOT NULL,
            produto VARCHAR (255) NOT NULL,
            quantidade INT NOT NULL,
            preco_unid REAL NOT NULL);
            """)
# Make the changes to the database persistent
conn.commit()
# Close cursor and communication with the database
cur.close()
conn.close()
print(cur)