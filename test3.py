class person:

    def age(self,cur_year,year_of_birth):
        return  cur_year - year_of_birth

    def email_id_input(self,email_id):
        print('Take and email and print it ',email_id)

    def ask_name(self):
        name = input('Please provide your name : ')
        return name

    def ask_dob(self):
        dob = input('tell your data of birth: ')
        return dob


mu = person()
an = person()

mu.email_id_input('murali@gmal.com')
print(mu.ask_dob())
print(mu.ask_name())

#task