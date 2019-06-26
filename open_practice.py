#どちらも同じ動作
#with文の最後ではファイルを閉じる

#http://tinyurl.com/zfgczj5
st = open("st1.txt", "w")
st.write("Hi from Python!")
st.close

#http://tinyurl.com/jt9guu2
with open("st2.txt", "w",) as f:
    f.write("Hi from Python!")

#http://tinyurl.com/hmuamr7
with open("st2.txt", "r") as f:
    print("print directry: ")
    print(f.read())

#readメソッドは、ファイルを開いた後に1回だけ使える
#もう一度読み込む場合は、ファイルをいったん閉じてから開く
#読み込んだコンテンツは、変数やコンテナに入れておくとよい
#http://tinyurl.com/hkzhxdz
my_list = []
my_string = ''

with open("st2.txt", "r") as f:
    my_list.append(f.read())
with open("st2.txt", "r") as f:
    my_string = f.read()
    
print("copy to list: ")
print(my_list)
print("copy to string: ")
print(my_string)
