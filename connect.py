import os
import psycopg


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(emp_id, name, ubi, photo, vecdataFile, cont, age, dis):
    print("Inserting BLOB into parent table")
    try:
        connection = psycopg.connect("***")
        cursor = connection.cursor()
        
        sql_insert_blob_query = """ INSERT INTO principal (ID, Name, Location, Img, VecImg, Contact, Age, Disability) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
                          

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(vecdataFile)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, ubi, empPicture, file, cont, age, dis)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into principal table", result)

    except psycopg.Error as error:
        print("Failed inserting BLOB data into Crockroach table {}".format(error))

    finally:
        cursor.close()
        connection.close()
        print("Crockroach connection is closed")

insertBLOB(1, "Jorge", "Lafayette 123, Anzures, Alvaro Obregon, CDMX, Mexico", "C:\\Users\\jorge\\Documents\\Hack4ML\\Images\\Jorge.jpg", "C:\\Users\\jorge\\Documents\\Hack4ML\\Images\\Jorgevec.txt", 1, 22, 1)
#cur.execute("select * from disability")
#res = cur.fetchall()
#print(res)


