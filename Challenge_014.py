#1
#Squareクラスにsquare_listクラス変数を追加しよう。
#そして、新しくSquareクラスのオブジェクトが作られるたび、
#そのオブジェクトをこのリストに追加しよう。
print("--Challenge 1--")

class Square:
    square_list = []
    
    def __init__(self, w):
        self.width = w
        self.square_list.append(self.width)

#2
#Squareクラスのオブジェクトをprint関数に渡したら、
#4辺それぞれの長さを出力しよう。
#例えば、Square(29)のようにオブジェクトを作ったら、
#print関数では 29by29by29by29 と出力しよう。
print("--Challenge 2--")

class Square2:
    square_list = []
    
    def __init__(self, w):
        self.width = w
        self.square_list.append(self.width)

    def __repr__(self):
        return "{}by{}by{}by{}".format(self.width,self.width,self.width,self.width)

mySquare = Square2(5)
print(mySquare)

#3
#2つのパラメータを受け取る関数を書こう。
#この関数は同じオブジェクトを渡されたらTrueを返し、
#そうじゃなかったらFalseを返そう。
print("--Challenge 3--")

def compare(x, y):
    return x is y

graph1 = Square(5)
graph2 = Square(7)
graph3 = graph1

print(compare(graph1, graph2))
print(compare(graph1, graph3))
