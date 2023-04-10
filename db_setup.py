import sys
import os
import psycopg2

print("Performing first-time setup...")
print("Connecting to database...")
conn = psycopg2.connect(database="server_db", user="postgres", password="postgres", host="localhost", port="5432")
cursor = conn.cursor()
conn.autocommit = True

cursor.execute("""
CREATE TABLE areas (  
  area_id serial PRIMARY KEY,  
  name VARCHAR ( 50 ) UNIQUE NOT NULL  
)  
""")

cursor.execute("""
CREATE TABLE salons (  
  salon_id serial PRIMARY KEY,  
  area_id INT,  
  name VARCHAR ( 50 ) UNIQUE NOT NULL  
)  
""")

cursor.execute("""
CREATE TABLE services (  
  service_id serial PRIMARY KEY,  
  name VARCHAR ( 50 ) UNIQUE NOT NULL,  
  price FLOAT NOT NULL
)  
""")

cursor.execute("""
CREATE TABLE positions (  
  position_id serial PRIMARY KEY,  
  name VARCHAR ( 50 ) UNIQUE NOT NULL,  
  salary FLOAT NOT NULL
)  
""")

cursor.execute("""
CREATE TABLE employees (  
  employee_id serial PRIMARY KEY,  
  firstname VARCHAR ( 50 ) NOT NULL,  
  secondname VARCHAR ( 50 ) NOT NULL,  
  thirdname VARCHAR ( 50 ) NOT NULL  
)  
""")

cursor.execute("""
CREATE TABLE clients (  
  client_id serial PRIMARY KEY,  
  firstname VARCHAR ( 50 ) NOT NULL,  
  secondname VARCHAR ( 50 ) NOT NULL,  
  thirdname VARCHAR ( 50 ) NOT NULL  
)  
""")

cursor.execute("""
CREATE TABLE orders (  
  order_id serial PRIMARY KEY,  
  salon_id INT,  
  client_id INT,  
  totalprice FLOAT  
)  
""")

cursor.execute("""
CREATE TABLE salon_service(  
  salon_id INT NOT NULL,  
  service_id INT NOT NULL,  
  PRIMARY KEY (salon_id, service_id),  
  FOREIGN KEY (salon_id)  
    REFERENCES salons (salon_id),  
  FOREIGN KEY (service_id)  
    REFERENCES services (service_id)  
)  
""")

cursor.execute("""
CREATE TABLE position_service(  
  position_id INT NOT NULL,  
  service_id INT NOT NULL,  
  PRIMARY KEY (position_id, service_id),  
  FOREIGN KEY (position_id)  
    REFERENCES positions (position_id),  
  FOREIGN KEY (service_id)  
    REFERENCES services (service_id)  
)  
""")

cursor.execute("""
CREATE TABLE order_details(  
  order_id INT NOT NULL,  
  service_id INT NOT NULL,  
  PRIMARY KEY (order_id, service_id),  
  FOREIGN KEY (order_id)  
    REFERENCES orders (order_id),  
  FOREIGN KEY (service_id)  
    REFERENCES services (service_id),  
  employee_id INT NOT NULL,  
  quantity INT NOT NULL,  
  price_per_unit FLOAT NOT NULL,  
  discount FLOAT  
)  
""")

cursor.execute("""
CREATE TABLE employee_position(  
  employee_id INT NOT NULL,  
  position_id INT NOT NULL,  
  PRIMARY KEY (employee_id, position_id),  
  FOREIGN KEY (employee_id)  
    REFERENCES employees (employee_id),  
  FOREIGN KEY (position_id)  
    REFERENCES positions (position_id)  
)  
""")





print("")

print("Closing connection...")
conn.close()
