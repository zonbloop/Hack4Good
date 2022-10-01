import os
import psycopg
conn = psycopg.connect("**")
with conn.cursor() as cur:
#    conn.execute("CREATE TABLE secondary( ID int not null, IDp int not null, Name varchar(255), Location varchar(255), Number int not null, Email varchar(100), Parent varchar(50), PRIMARY KEY (ID) )")
    conn.execute("CREATE TABLE disability( ID int not null, Disability varchar(255), PRIMARY KEY (ID) )")
    #conn.execute("select * from public.principal")
    #res = cur.fetchall()
    conn.commit()
    #print(res)
