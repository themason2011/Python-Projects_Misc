def getFields(filename):
    ''' Input is a filename
    return a list [[motnhs],[days],[names]]
    '''

    f = open(filename)
    line = f.readline() #Skips past first two lines of the file
    line = f.readline()
    months = []
    days = []
    names = []

    while line.startswith('#'): #Skip past comments
        line = f.readline()

    while line:
        lst = line.strip().split(',') #Split each line into a list
        month = lst[0]
        day = lst[1]
        name = lst[2]
        months.append(month) #Add each element of the list into month, day, and name
        days.append(day)
        names.append(name)
        print(month, day, name) #Print each month, day, and name
        line = f.readline()

    f.close()
    return [months, days, names]

result = getFields('songs.txt')
