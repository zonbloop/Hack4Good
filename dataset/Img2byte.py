import numpy as np
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


caracteristicas = []
for i in range(1,31):
    caracteristicas.append(convertToBinaryData("User.1."+str(i)+".jpg"))
#print(c)
#print(np.array([["abc","def"]]))