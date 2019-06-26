import csv

#http://tinyurl,com/go9wepf
with open("stCsv.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

#http://tinyurl.com/gvcdgxf
#正しくはこう？
with open("stCsv.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in f:
        print(row)
#教科書の内容
with open("stCsv.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in f:
        print(",".join(row))
