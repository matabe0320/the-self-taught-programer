import math

#1
#リンゴと言われて思い浮かぶ、4つの属性を考えよう。
#4つの属性をインスタンス変数に持つ、Apppleクラスを定義しよう
print("--challenge 1--")

class Apple:
    def __init__(self, color, size, weight, sweet):
        self.color = color
        self.size = size
        self.weight = weight
        self.sweet = sweet

#2
#円を表すCircleクラスを定義しよう。
#そのクラスに、面積を計算して返すメソッドareaをもたせよう。
#面積の計算には、Pythonの組み込みモジュールmathのpi定数が使えます。
#次にCircleオブジェクトを作って、areaメソッドを呼び出し、結果を出力しよう。
print("--challenge 2--")

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius * self.radius * math.pi

myCircle = Circle(10)
print(myCircle.area())

#3
#三角形を表すTriangleクラスを定義して、面積を返すareaメソッドを持たせよう。
#そしてTriangleオブジェクトをつくって、areaメソッドを呼び出して、結果を出力しよう。
print("--challenge 3--")

class Triangle:
    def __init__(self, b, h):
        self.bottom = b
        self.height = h

    def area(self):
        return self.bottom * self.height / 2

myTriangle = Triangle(5, 8)
print(myTriangle.area())

#4
#六角形を表すHexagonクラスを定義しよう。
#そのクラスには、外周の長さを計算して返すメソッドcaluculate_perimeterを定義しよう。
#そして、Hexagonオブジェクトを作ってcaluculate_perimeterメソッドを呼び出し、結果を出力しよう。
print("--challenge 4--")

class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

a_hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(a_hexagon.calculate_perimeter())
