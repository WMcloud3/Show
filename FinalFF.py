def main():
    userFileName = "Script.csv"

    fileToReadFrom = open(userFileName, "r")

    text_file = open("FILE B", "w")

    line = fileToReadFrom.readline()

    # part 1: print name, FavoriteFridge1
    while line != "":
        fields = line.split(',')
        text_file.write(fields[0] + "," + fields[1] + '\n')
        line = fileToReadFrom.readline()

    # part 2: print item totals for customers
    namelist = "Jill,Candice,Alycia"
    names = namelist.split(',')
    index = 0
    while index < len(names):
        total = 0
        fileToReadFrom.seek(0)
        line = fileToReadFrom.readline()
        while line != "":
            fields = line.split(',')
            if names[index] == fields[0]:
                if fields[3] != "":
                    total = total + float(fields[3])
                text_file.write(fields[0] + "," + fields[2] + "," + fields[3] + '\n')
            line = fileToReadFrom.readline()
        text_file.write(str(total) + '\n')
        index = index + 1

    text_file.close ()


main()