class Person :

    def __init__(sudh,name, surname, emailid, year_of_birth):
        sudh.name = name
        sudh.surname = surname
        sudh.emailid = emailid
        sudh.year_of_birth = year_of_birth

    def age(sudh, current_year):
        return current_year - sudh.year_of_birth

anuj_v = Person("anuj","bandari","anujbandari@gmail.com",1995)
murali  = Person("murali","gummadidala","murlai@gmail.com",1993)
print(anuj_v.name)
print(murali.surname)
print(anuj_v.emailid)
print(type(murali))
print(murali.age(2022))