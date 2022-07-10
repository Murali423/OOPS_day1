class Person :

    def __init__(self,name, surname, emailid, year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

anuj_v = Person("anuj","bandari","anujbandari@gmail.com",1995)
murali  = Person("murali","gummadidala","murlai@gmail.com",1995)
print(anuj_v.name)
print(murali.surname)
print(anuj_v.emailid)
print(type(murali))