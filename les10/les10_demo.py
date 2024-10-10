import psycopg2
import db_config

connection_str  = f"host='localhost' dbname='fabriek' "
connection_str += f"user='tijmenjoppe' password='{db_config.DB_PASSWORD}'"

conn = psycopg2.connect(connection_str)
cur = conn.cursor()

invoer = 'Utrecht' # input("Geef een plaats: ")

query_select = f""" SELECT klantnr, plaats 
                    FROM klant
                    WHERE plaats = %s; """

cur.execute(query_select, [invoer])
results = cur.fetchall()

for klant in results:
    print(f" - klant #{klant[0]} woont in {klant[1]}")

query_insert = """ INSERT INTO klant (klantnr, naam, adres, plaats)
                   VALUES (%s, %s, %s, %s);"""

cur.execute(query_insert, [778, 'Tijmen', 'Constr.', 'Utrecht'])
# conn.commit()
conn.rollback()

conn.close()
