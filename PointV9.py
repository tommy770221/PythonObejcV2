class Point:
    def __init__(self,x=0,y=0):
        '''' 點位置初始化 '''
        self.move(x,y)

    def move(self,x,y):
        " 移動點到新的2D空間位置"
        self.x = x
        self.y = y

    def reset(self):
        '  將點重置回到原點: 0,0 '
        self.move(0,0)

point=Point()

print(point.x, point.y)