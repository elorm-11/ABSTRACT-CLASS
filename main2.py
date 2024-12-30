class  Range():
    def price(self):
        print("i cost From $107,400 MSRP")

    def size(self):
        print("i'm  5052 mm length and 	2209 mm wigth ")

    def type(self):
        print("i'm a  Luxury SUVs and 4x4 Vehicle.")

class bugatti():
    def price(self):
        print("i cost starts at $2,990,000 and goes up to $3,900,000 depending on the trim and options.")    

    def size(self):
          print("i'm around the length of 14'10.9” (454 cm), overall width of 6'8.2” (204 cm), and height of 3'11.7” (121 cm).")

    def type(self):
        print("i'm a sport car")

obj_ran = range() 
obj_bug = bugatti()

for country in (obj_ran, obj_bug):
    country.price()
    country.size()
    country.type()