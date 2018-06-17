import math


class Point:
    ' 代表二維空間中的坐標點 '

    def _init_(self, x=0, y=0):
        '   '  ' 點位置初始化,可以指定x與y坐標若無指定預設為原點 '  '   '
        self.move(x, y)

    def move(self, x, y):
        " 移動點到新的2D空間位置 "
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def caculate_distance(self, other_point):
        """計算這一點與當作參數傳入的第二點
      　　　的距離  此函式使用勾股定理來計
      　　　算兩點間的距離,
                  距離以浮點數回傳"""

        return math.sqrt((
        (self.x - other_point.x) ** 2 +
        (self.y - other_point.y) ** 2))


point = Point()

print(point.x,point.y)