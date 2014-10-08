import psycopg2

# Connect to an existing database
conn = psycopg2.connect("host=23.89.198.31 dbname=magikarp user=gabriel password=8963")

# Open a cursor to perform database operations
cur = conn.cursor()
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO legal (numero) VALUES (23432)")
# Make the changes to the database persistent
conn.commit()
# Close communication with the database
cur.close()
conn.close()