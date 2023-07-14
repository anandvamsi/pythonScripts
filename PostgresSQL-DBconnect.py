"""Install the module psyncob2
pip3 install psycopg2-binary
code for DB connecton 
>>
"""
import psycopg2
from psycopg2 import Error

DB_NAME = "CAM"
DB_USER ="lambda02access"
DB_PASSWORD = "h$n05XXXXXXXXXXXXZ6"
DB_HOST = "caXXXXXXXXXXXXmazonaws.comm"
DB_PORT= 5432
try:
    conn = psycopg2.connect(database=DB_NAME, 
                             user=DB_USER,
                             password= DB_PASSWORD,
                             host=DB_HOST,
                             port=DB_PORT)
    print("DB connection is successfull")
except Error as e:
    print(f"DB connection was not successful {e}")
