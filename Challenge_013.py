#1
#RectangleとSquareクラスを作ろう。
#両方のクラスに、その図形の外周の長さを計算して返す
#calcurate_perimeterメソッドを定義しよう。
#そして、RectangleとSquareのオブジェクトを作って、
#それぞれのcalculate_perimeterメソッドを呼ぼう。
print("--Challenge 1--")

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calcurate_perimeter(self):
        return (self.width + self.len) * 2

class Square:
    def __init__(self, w):
        self.width = w

    def calcurate_perimeter(self):
        return (self.width) * 4

myRectangle = Rectangle(4,5)
mySquare = Square(4)
print(myRectangle.calcurate_perimeter())
print(mySquare.calcurate_perimeter())

#2
#Squareクラスにchange_sizeメソッドを定義して、
#そこに渡したすうちの分だけSquareオブジェクトの横幅を増やしたり、
#減らしたり（マイナスの値）してみよう。
print("--Challenge 2--")

class Square2:
    def __init__(self, w):
        self.width = w

    def change_size(self, cs):
        self.width += cs

mySquare = Square2(4)
print(mySquare.width)
mySquare.change_size(int(input("変更するサイズ入力: ")))
print(mySquare.width)

#3
#Shapeクラスを定義しよう。
#呼ばれたら"I am a shape"を返すメソッドwhat_am_iを定義しよう。
#前のチャレンジで定義したRectangleとSquareクラスを変更して、
#このShapeクラスを継承させよう。
#そして、RectagleとSquareのオブジェクトを生成して、
#このチャレンジで追加したメソッドwhat_am_iを読んでみよう。
print("--Challenge 3--")

class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle3(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calcurate_perimeter(self):
        return (self.width + self.len) * 2

class Square3(Shape):
    def __init__(self, w):
        self.width = w

    def calcurate_perimeter(self):
        return (self.width) * 4

myRectangle = Rectangle3(4,5)
mySquare = Square3(4)
myRectangle.what_am_i()
mySquare.what_am_i()

#4
#HorseクラスとRiderクラスを定義しよう。
#コンポジションを使って、馬（Horse）に騎手（Rider）を持たせよう。
print("--Challenge 4--")

class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

take = Rider("TakeYutaka")
deep = Horse("Deepimpact", take)

print(deep.owner.name)
