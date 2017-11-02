import sqlite3
conn = sqlite3.connect('test.db')
# print("opened database successfully")

# c.execute('''
#         create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real

#         );
#         ''')

# print("Table creat successfully")
# conn.commit()
# conn.close()

# c.execute("insert into company (id , name , age , address , salary) \
#         values (1 , 'paul' , 32 , 'california' , 20000.00)")

# conn.commit()
# print("Records created successfully")
# conn.close()

# cursor = c.execute("select * from company")
# for row in cursor:
#     print ("id = " , row[0])
#     print ("name = " , row[1])
#     print ("age = " ,row[2])
#     print ("address = " , row[3])
#     print("salary = " , row[4])

# print("Operation done successfully")
# conn.close()
c = conn.cursor()

c.execute("update company set salary = 25000 where id = 1 " )

conn.commit()
print("total number of rows updated : " , conn.total_changes)

cursor = conn.execute("select id , name , address , salary from company")
for row in cursor:
    print ("id = " , row[0])
    print ("name = " , row[1])
    print ("age = " ,row[2])
    print ("address = " , row[3])
    print("salary = " , row[4])

print("successfully")
conn.close()