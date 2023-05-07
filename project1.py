# connection.py

import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='Manjula2711@')
print(mydb.connection_id)

-- ----------------------------------------------------------------------------------------------------------------------------------------------
# createdb.py

import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='Manjula2711@')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute("create database Inventory_Management")

-- ------------------------------------------------------------------------------------------------------------------------------------------------
# creating_tables.py

import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='Manjula2711@',database='Inventory_Management')
cur=mydb.cursor()
t1='create table manufacture_table(manufacture_id integer(5) primary key,productName varchar(30),color varchar(20),no_of_items integer(5),defective_items integer(5),manufacture_date date,store varchar(30))'
t2='create table goods_table(companyName varchar(30),productName varchar(30),goods_id integer(5) primary key,cost_of_goods integer(5),manufacture_date date)'
t3='create table purchase_table(purchase_id integer(5) primary key,productName varchar(30),color varchar(20),no_of_items integer(5),store varchar(30),purchase_amount integer(5))'
t4='create table sale_table(manufacture_id integer(5) primary key,productName varchar(30),store varchar(30),sale_date date,profit_margin integer(2))'
cur.execute(t1)
cur.execute(t2)
cur.execute(t3)
cur.execute(t4)

-- -----------------------------------------------------------------------------------------------------------------------------------------------

# inserting_tables.py

import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='Manjula2711@',database='Inventory_Management')
cur=mydb.cursor()
i1='insert into manufacture_table(manufacture_id,productName,color,no_of_items,defective_items,manufacture_date,store)values(%s,%s,%s,%s,%s,%s,%s)'
a=[(101,"shirt","black",200,1,"23-04-01","ORay"),(102,"shirt","blue",200,0,"23-03-02","ORay"),(103,"toys","blue",100,0,"23-04-03","MyKids"),(104,"toys","red",100,0,"23-05-05","MyKids"),(105,"wooden chairs","brown",90,0,"23-05-01","MyCare"),(106,"wooden chairs","black",90,0,"23-04-18","MyCare"),(107,"wooden table","brown",100,0,"23-04-01","MyCare")]
i2='insert into goods_table(companyName,productName,goods_id,cost_of_goods,manufacture_date)values(%s,%s,%s,%s,%s)'
b=[("SS Export","shirt",101,20000,"23-04-01"),("X Export","shirt",102,10000,"23-03-02"),("Y Export","toys",103,23000,"23-04-03"),("Z Export","toys",104,10000,"23-04-03"),("X Export","wooden chairs",105,10000,"23-05-01"),("Y Export","wooden chairs",106,15000,"23-04-18"),("Z Export","wooden table",107,15000,"23-04-01")]
i3='insert into purchase_table(purchase_id,productName,color,no_of_items,store,purchase_amount)values(%s,%s,%s,%s,%s,%s)'
c=[(101,"shirt","black",200,"ORay",2000),(102,"shirt","blue",200,"ORay",3000),(103,"toys","blue",100,"MyKids",2000),(104,"toys","red",100,"MyKids",1000),(105,"wooden chairs","brown",90,"MyCare",10000),(106,"wooden chairs",'black',90,"MyCare",15000),(107,"wooden table","brown",100,"MyCare",20000)]
i4='insert into sale_table(manufacture_id,productName,store,sale_date,profit_margin)values(%s,%s,%s,%s,%s)'
d=[(101,"shirt","ORay","23-06-01",2000),(102,"shirt","ORay","23-07-27",3000),(103,"toys","MyKids","23-11-27",4000),(104,"toys","MyKids","23-08-27",2000),(105,"wooden chairs","MyCare","23-12-12",5000),(106,"wooden chairs","MyCare","23-09-23",5000),(107,"wooden table","MyCare","23-08-08",5000)]

cur.executemany(i1,a)
cur.executemany(i2,b)
cur.executemany(i3,c)
cur.executemany(i4,d)

mydb.commit()
print("inserted successfully")

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

# queries.py

import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', password='Manjula2711@',database='Inventory_Management')
cur=mydb.cursor()

# Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’.

a='delete from manufacture_table where store = "ORay" and manufacture_date = "23-04-01" and defective_items = 1'
cur.execute(a)
mydb.commit()
print("deleted successfully")

# Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store

b= 'update manufacture_table set manufacture_id=108,productName ="Toys",color="black",no_of_items=105,defective_items=0,manufacture_date="23-02-02",store="KStore" where productName="Toys" and color="red" '
cur.execute(b)
mydb.commit()
print("updated successfully")

#Display all the “wooden chair” items that were manufactured before the 1st May 2023.

c= 'select * from manufacture_table where productName="wooden chairs" and manufacture_date < "23-05-01" '
cur.execute(c)
display=cur.fetchall()
for x in display:
    print(x)
print("displayed")

# Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company

d= 'select profit_margin from sale_table inner join goods_table on sale_table.manufacture_id=goods_table.goods_id where sale_table.productName="wooden table" and sale_table.store="MyCare" and goods_table.companyName = "SS Export" ' 
cur.execute(d)
display=cur.fetchall()
for x in display:
     print(x)
print("displayed")

