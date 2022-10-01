import os
import psycopg


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(emp_id, name, ubi, photo, vecdataFile, cont, age, dis, table, idp=1, number=1, email="d", parent=1):
    print("Inserting BLOB into parent table")
    try:
        connection = psycopg.connect("postgresql://jorge:uJsQkZbKwSMr9fdYM_7NsQ@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dlair-ninja-5391")
        cursor = connection.cursor()
        
        if table == "principal":
            sql_insert_blob_query = """ INSERT INTO principal (Id, Name, Location, Img, VecImg, Contact, Age, Disability) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
            empPicture = convertToBinaryData(photo)
            file = convertToBinaryData(vecdataFile)
            # Convert data into tuple format
            insert_blob_tuple = (emp_id, name, ubi, empPicture, file, cont, age, dis)
        elif table == "secondary":
            sql_insert_blob_query = """ INSERT INTO secondary (Id, IDp, Name, Location, Number, email, parent) VALUES (%s,%s,%s,%s,%s,%s,%s) """
            # Convert data into tuple format
            insert_blob_tuple = (emp_id, idp, name, ubi, number, email, parent)
        
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into principal table", result)

    except psycopg.Error as error:
        print("Failed inserting BLOB data into Crockroach table {}".format(error))

    finally:
        cursor.close()
        connection.close()
        print("Crockroach connection is closed")

insertBLOB(1, "Jorge", "Lafayette 123, Anzures, Alvaro Obregon, CDMX, Mexico",
 "/home/sara/Documents/AIHack4Good/OpenCV-Face-Recognition-master/FacialRecognition/dataset/User.2.3.jpg",
 "/home/sara/Documents/AIHack4Good/OpenCV-Face-Recognition-master/FacialRecognition/archivoProp.txt", 1, 22, 1, "principal")
#cur.execute("select * from disability")
#res = cur.fetchall()
#print(res)


