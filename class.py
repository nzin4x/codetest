class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

i = Human('nz', 30)
print(i.__dict__)
i.sex = 'male'
print(i.__dict__)
i.whatthefund = "true"
print(i.__dict__)
