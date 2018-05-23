def acronym(inputString):
    listStrings = inputString.split()
    acronym = ''

    for item in listStrings:
        acronym = acronym + (item[0].upper())

    return acronym