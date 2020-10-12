# file = open("firstCSV.csv","w")
# header =    "Class,Term,Grade\n"
# firstRow  = "F6520,F20, 4.0\n"
# otherRow =  ["ACCTG6510,F20, 4.0\n",
#              "FINAN6360,F20, 3.6\n",
#              "WINES1010,F20, 3.0\n"]
# file.write(header)
# file.write(firstRow)
# file.writelines(otherRow)
# file.close()


# ----------------------------------------------------------------------------------------


# file = open("testFile.csv", "r")
# rows = file.readlines()
# dict = {"Major": []}
# for row in rows[1:]:
#     row = row.strip()
#     # DO NOT DO THIS IN YOUR HOMEWORK, BUT DO THIS IN YOUR EXAM
#     columns = row.split(",")
#     colA = columns[0]
#     colB = columns[1]
#     colC = float(columns[2])
#     if "F" in colA:
#         nElements = dict["Major"]
#         # nElements.append(colC) = nElements
#         dict["Major"] = nElements + [colC]

# nElementsComplete = dict["Major"]
# average = sum(nElementsComplete) / len(nElementsComplete)
# print(dict)
# file.close()


# -----------------------------------------------------------------------------------------


file = open("testFile.csv", "r")
rows = file.readlines()
formattedList = []
dictionary = []


def filterTransactions(company):
    if():
        return true
    else:
        return false


for row in rows[1:]:
    row = row.strip()
    columns = row.split(",")
    formattedList.append(columns)

# for row in rows:
#     if rows[0] = "Utes":
#         Utes += rows[1] += -1*rws[2]
# for transaction in formattedList

# take transaction[0] and find all transactions with same value

# groupedList = filter(filterTransactions(transaction[0]), )

# reduce()

# combine all transactions from single company and append them to a new list

    print(formattedList)

file.close()

["Limited Limits LLC", "0", "8109255"]
