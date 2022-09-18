class Message:
    def __init__(self):
        self.content = ""

    def send(self):
        print("Message sent.")

    def read(self):
        return self.content

    def write(self, content):
        self.content = content


class Email(Message):
    def __init__(self):
        super().__init__()

    def send(self):
        print("Sending email.")
        super().send()








