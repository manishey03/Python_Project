def read_data():
    data = []
    column = ['SN', 'Name', ' Brand', ' Price', ' Quantity', ' Processor', ' Graphic card']
    data.append(column)
    file = open('data.txt', 'r')
    sn = 1
    for line in file.readlines():
        data.append([str(sn),*line.rstrip().split(',')])
        sn += 1
    file.close()
    return data



