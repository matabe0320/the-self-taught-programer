#1 文字列「カミュ」に含まれているすべての文字を1文字ずつ出力
print("----Challenge 1----")

string1 ="カミュ"
print(string1[0])
print(string1[1])
print(string1[2])

#2 2つの文字列を入力させるプログラムを書こう。その文字列をそれぞれ、
#  別の文字列の箇所に穴埋めした新しい文字列を作ろう
#　「私は昨日[入力1]を描いて、[入力2]に送った！」
#  そして、それを出力しよう
#print("----Challenge 2----")
#data1 = input("描いたもの：")
#data2 = input("送り先：")
#print("私は昨日{}を描いて、{}に送った！".format(data1, data2))

#3 文法的には正しい文章を書いた文字列「aldous Huxley was born in
#  1894.」の先頭をメソッドを使って大文字にしよう
print("----Challenge 3----")
print("aldous Huxley was born in 1894.".capitalize())

#4 文字列「どこで？　だれが？　いつ？」をメソッドで分割して「どこで？」
#  「だれが？」「いつ？」のようなリストにしよう
print("----Challenge 4----")
print("どこで？　だれが？　いつ？".split("　"))

#5 リスト「The」「fox」「jumped」「over」「the」「face」「.」の文字列
#  を正しい英文になるように連結しよう。単語と単語の間は空白が必要で
#  すが、最後のピリオドの前には空白は不要です。文字列を要素に持つリストを
#  1つに連結するメソッドがあることを忘れずに！
print("----Challenge 5----")
words = "The","fox","jumped","over","the","face"
print(" ".join(words)+".")

#6 文字列「A screaming comes across the sky.」に含まれるすべての「s」を
#  ドル記号に置き換えた文字列を作ろう
print("----Challenge 6----")
print("A screaming comes across the sky.".replace("s","$"))

#7 メソッドを使って、「Hemingway」の中で最初に「m」が出現するインデックスを
#  調べよう
print("----Challenge 7----")
try:
    print("Hemingway".index("m"))
except:
    print("'m' does not found.")

#8 好きな本のセリフを探して、Pythonの文字列にしよう。ただし、クウォート文字が
#  含まれているセリフを選ぶこと
print("----Challenge 8----")
print("Everything has a \"begining\"")
print("Nothing has no 'end'")

#9 文字列を「＋」で連結して、「three three three」という文字列を作ろう
#  また「*」を使って同じ文字列を作ってみよう
print("----Challenge 9----")
print("three " + "three " + "three")
print(("three " * 3).strip())

#10 文字列「四月の晴れた寒い空で、時計がどれも十三時を打っていた。」を
#   スライスして、「、」の前までの部分文字列を作ろう。
print("----Challenge 10----")
words = "四月の晴れた寒い空で、時計がどれも十三時を打っていた。"
position = words.index("、") 
print(words[:position])
