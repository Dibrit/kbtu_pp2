class StringProcessor:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input()

    def printString(self):
        print(self.text.upper())

a = StringProcessor()
a.getString()
a.printString()
