import csv

#3
#リストのリストに含まれている要素をCSVに書き出そう。
#データは次の通り
#[["Top Gun", "Ricky Business", "Minority Report"],
#["Titanic", "The Revenant", "Inception"],
#["Training Day", "Man on Fire", "Flight"]]
#データの各要素はCSVの一行となり、その一行に含まれる各要素が
#カンマで区切られるように書き出そう
movie_list = [["Top Gun", "Ricky Business", "Minority Report"],
 ["Titanic", "The Revenant", "Inception"],
 ["Training Day", "Man on Fire", "Flight"]]
with open("challenge.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for row in movie_list:
        w.writerow(row)


#4 上記を日本語でもやってみよう
movie_list = [["トップガン", "リッキー", "マイノリティーリポート"],
 ["タイタニック", "レベナント", "インスペクション"],
 ["トレーニングデイ", "マンオンファイア", "フライト"]]
with open("challenge2.csv", "w", newline='', encoding="cp932") as f:
    w = csv.writer(f, delimiter=",")
    for row in movie_list:
        w.writerow(row)
