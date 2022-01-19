class roman_numeral:
    def __init__(self, integer):
        self.integer = integer

    def thousands(self):
        thousands = self.integer / 1000
        self.remainder1 = self.integer % 1000
        while thousands > 0:
            print "M"
            thousands = thousands - 1

    def five_hundred(self):
        five_hundred = self.remainder1 / 500
        self.remainder2 = self.remainder1 % 500
        if (self.remainder1 / 100) == 9:
            print "C"
            print "M"
        else:
            while five_hundred > 0:
                print "D"
                five_hundred = five_hundred - 1

    def hundreds(self):
        hundreds = self.remainder2 / 100
        self.remainder3 = self.remainder2 % 100
        if (self.remainder1 / 100) < 9:
            while hundreds > 0:
                print "C"
                hundreds = hundreds - 1

    def fifty(self):
        fifty = self.remainder3 / 50
        self.remainder4 = self.remainder3 % 50
        if (self.remainder3 / 10) == 9:
            print "X"
            print "C"
        else:
            while fifty > 0:
                print "L"
                fifty = fifty - 1

    def tens(self):
        tens = self.remainder4 / 10
        self.remainder5 = self.remainder4 % 10
        if (self.remainder3 / 10) < 9:
            while tens > 0:
                print "X"
                tens = tens - 1

    def five(self):
        five = self.remainder5 / 5
        self.remainder6 = self.remainder5 % 5
        if (self.remainder5 / 1) == 9:
            print "I"
            print "X"
        else:
            while five > 0:
                print "V"
                five = five - 1

    def ones(self):
        ones = self.remainder6 / 1
        self.remainder7 = self.remainder6 % 1
        if (self.remainder5 / 1) < 9:
            while ones > 0:
                print "I"
                ones = ones - 1
    

integer = int(input("Enter an integer"))

number = roman_numeral(integer)

number.thousands()
number.five_hundred()
number.hundreds()
number.fifty()
number.tens()
number.five()
number.ones()
