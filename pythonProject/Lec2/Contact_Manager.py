class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class MailSender:
    def __init__(self, email):
        self.email = email

    def send_mail(self):
        return f"your mail send {self.email} "


class Friend(Contact, MailSender):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        MailSender.__init__(self, email)


class Family(Contact, MailSender):
    def __init__(self, name, phone, email, birth_data):
        super().__init__(name, phone)
        MailSender.__init__(self, email)
        self.birth_data = birth_data


c = Contact("eka", "555 555 555")

fr1 = Friend("ekaterine",  "555 555 555", "ekaterine.gurgenidze.1@btu.edu.ge")
print(fr1.send_mail())

fe1 = Family("kato", "571 555 555", "kato.gurgenidze.1@btu.edu.ge", "09/12/2002")
print(fe1.send_mail())
