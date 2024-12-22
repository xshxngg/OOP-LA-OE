class Hero:
    def __init__(self,name):
        self.name = name

argus = Hero("argus")
print(argus.name)
del argus.name
print(argus.name)

'''class laptop:
    def __init__(self, brand, model):
        pass
    def laptop_info(self):
        pass

apple = laptop("apple","macbook")
print(laptop.laptop_info())'''