class Ghana():
    def capital(self):
        print("Greater Accra is the capital of Ghana.")

    def language(self):
        print("English is the most widely spoken language of Ghana.")

    def type(self):
        print("Ghana is a developing country.")

class USA():
    def capital(self):
        print("washington, D.C, is the capital of USA.")    

    def language(self):
          print("English is the primary language of USA.")

    def type(self):
        print("USA is a developing country.")

obj_gha = Ghana() 
obj_usa = USA()

for country in (obj_gha, obj_usa):
    country.capital()
    country.language()
    country.type()