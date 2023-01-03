
class Creative:
    def __init__(self, name, typeC):
        self.name = name
        self.typeC = typeC

    def printInfo(self):
        info = '\nName: {}\nType: {}'.format(self.name,self.typeC)
        return info
class Author(Creative):
    def __init__(self, genre):
        self.genre = genre


if __name__ == "__main__":
    C1 = Creative('Elyse Norman', 'Painter')
    print(C1.printInfo())
