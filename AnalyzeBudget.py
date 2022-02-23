import os
import sys
import csv

grocerylist = [
"DIERBERG",
"SCHNUCKS",
"WALGREENS",
"TARGET"
]

billlist = [
"GEICO",
"FUNIMATION",
"SPOTIFY",
"CLUB FITNESS",
"CHARTER",
"AMEREN",
"DISNEYPLUS",
"AMAZON PRIME",
"HULU"
]

gaslist = [
"CIRCLE K",
"SHELL SERVICE",
"PILOT"
]

entertainmentlist = [
"GOLF",
"FOREST PARK GC",
"SCAREFEST"
]

debtdownlist = [
"HONDA PMT",
"STUDNTLOAN",
"BANKING TRANSFER"
]

badlist = [
"MCDONALD",
"TACO",
"PANDA",
"BURGER",
"DOMINO",
"CHICK",
"CANE",
"SONIC",
"5GUYS",
"WENDY",
"HARDEES",
"SHACK",
"IMOS",
"KRISPY",
"FUZZY",
"WAVE",
"TIN ROOF",
"IHOP",
"COOK OUT",
"SUBWAY",
"MCGURKS",
"KFC",
"OLIVE GARDEN",
"RED ROBIN",
"MOES",
"PEI WEI",
"BRICKHOUSE",
"BAILEYS RANGE",
"KINGPIN",
"PUEBLO NUEVO",
"THE POST BAR",
"WILD WINGS",
"CREVE COEUR LAKEHOUSE",
"AMIGO JOE",
"ROSALITA",
"DUKES",
"PINK GALLEON",
"GIBSONS",
"JASON",
"PELANCHOS",
"LITERBOARD",
"COOL BEANS",
"ZAXBYS",
"MOLLY",
"DAIRY QUEEN",
"OISHI",
"RAMEN",
"OLIVE",
"FIRST",
"NUDO",
"DUNKIN",
"DEWEY",
"QUIZNO",
"SYBERGS",
"ARAMARK BOEING",
"LOUIES",
"HOKKAIDO"
]

CashFlowList = [
"TWITCH",
"BOEING"
]

CategoriesDict = {}
CategoriesDict['rent'] = {}
CategoriesDict['bills'] = {}
CategoriesDict['groceries'] = {}
CategoriesDict['gas'] = {}
CategoriesDict['debt'] = {}
CategoriesDict['bad'] = {}
CategoriesDict['other'] = {}
CategoriesDict['in'] = {}
CategoriesDict['in']['boeing'] = []
CategoriesDict['in']['twitch'] = []


def isRent(row):
    if "WESTCHASE" in row[2]:
        return 1
    elif "CHECK" in row[2] and row[4] == "0":
        return 1
    else:
        return 0

def insertIntoCategory(dict, name, row):
    if name not in dict:
        dict[name] = []
    dict[name].append(row[3])

def sortCashIn(row):
    if "BOEING" in row[2]:
        CategoriesDict['in']['boeing'].append(row[4])
        return 1
    elif "TWITCH" in row[2]:
        CategoriesDict['in']['twitch'].append(row[4])
        return 1
    else:
        return 0

def categorize(row):
    other = False
    if row[3] == "0":
        other = other or sortCashIn(row)
    if isRent(row):
        other = True
        insertIntoCategory(CategoriesDict['rent'], "westchase", row)
    other = other or checkList(billlist, row, CategoriesDict['bills'])
    other = other or checkList(grocerylist, row, CategoriesDict['groceries'])
    other = other or checkList(gaslist, row, CategoriesDict['gas'])
    other = other or checkList(debtdownlist, row, CategoriesDict['debt'])
    other = other or checkList(badlist, row, CategoriesDict['bad'])
    if not other:
        if 'Date' not in row[0] and 'Transactions' not in row[0] and not row[0] == '':
            name = row[2]
            insertIntoCategory(CategoriesDict['other'], row[2], row)


def checkList(l, row, dict):
    if row[4] == "0":
        cashflow = row[3]
    if row[3] == "0":
        cashflow = row[4]
    other = 0
    for x in l:
        if x in row[2]:
            insertIntoCategory(dict, x, row)
            other = 1
    return other


def sortSecond(val):
    return val[1]

def recursiveSum(dic):
    if isinstance(dic, list):
        print("NOT OF DICTIONARY TYPE")
    elif isinstance(dic, dict):
        dictSummary = {}
        for key, val in dic.items():
            if isinstance(val, dict):
                dictSummary[key] = recursiveSum(val)
            elif isinstance(val, list):
                total = 0.0
                for j in val:
                    total = total + float(j)
                dictSummary[key] = total
        return dictSummary

def recursiveSumEx(dic, exclude):
    if isinstance(dic, list):
        print("NOT OF DICTIONARY TYPE")
    elif isinstance(dic, dict):
        dictSummary = {}
        for key, val in dic.items():
            if key in exclude:
                continue
            if isinstance(val, dict):
                dictSummary[key] = recursiveSum(val)
            elif isinstance(val, list):
                total = 0.0
                for j in val:
                    total = total + float(j)
                dictSummary[key] = total
        return dictSummary

def printDict(dict):
    for key, value in dict.items():
        print (key)
        print ("   " + value)


def summarizeDataDict(dict):
    totalCashInDic = recursiveSum(dict)
    totalIn = 0.0
    print(totalCashInDic)
    for key, val in totalCashInDic.items():
         totalIn = totalIn + val
    print("Total Cash In : " + str(totalIn))

def dictSum(dictionary):
    total = 0.0
    for key, value in dictionary:
        for amount in value:
            total = total + float (value)

def findAmount(d, exclude):
    if isinstance(d, list):
        print("NOT OF DICTIONARY TYPE")
    elif isinstance(d, dict):
        amount = 0.0
        for key, val in d.items():
            if key in exclude:
                continue
            if isinstance(val, dict):
                amount = amount + findAmount(val, [])
            elif isinstance(val, list):
                total = 0.0
                for j in val:
                    total = total + float(j)
                amount = amount + total
        return amount

def getCashIn():
    return findAmount(CategoriesDict['in'], [])

def getCashOut():
    return findAmount(CategoriesDict, ['in'])

def summarizeData():
    print("DATA SUMMARY\n")
    inn = getCashIn()
    out = getCashOut()
    print("Cash In  = " + str(inn))
    print("Cash Out = " + str(out))
    print("Net Flow = " + str(inn-out))
    print("\n")
    for key in CategoriesDict:
        print(key + " : " + str(findAmount(CategoriesDict[key], [])))


os.chdir("../../Finances/Budget/2020")

badtotal = 0.0
goodtotal = 0.0
x = 0
y = 0
for filename in os.listdir("."):
    if "Suntrust" in filename:
        with open(filename,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                categorize(row)


summarizeDataDict(CategoriesDict['gas'])
summarizeData()
#print(findAmount(CategoriesDict['debt'], []))
#summarizeData()
#print(CategoriesDict)

##
