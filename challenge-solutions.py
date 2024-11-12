class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
        return(a + b + c)


obj1 = Point(4, 5, 6)
print(obj1.sqSum())

###### challenge 2 #######
class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return(self.phy + self.chem + self.bio)

    def percentage(self):
        return((self.totalObtained() / 300) * 100)
