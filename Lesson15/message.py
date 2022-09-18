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


class TextMessage(Message):
    def __init__(self):
        self.max_character = 144
        super().__init__()

    def send(self):
        print("Sending text.")
        super().send()

    def write(self, content):
        if len(content) > self.max_character:
            warning_message = "The number of characters in your message exceeded {}. Please keep it concise.".format(self.max_character)
            print(warning_message)
            super().write(content[:144])
        else:
            super().write(content)


class Letter(Message):
    def __init_(self):
        super().__init__()

    def send(self):
        print("Mailing letter.")
        super().send()


"""Main methods"""
email = Email()
email_content = "Hello! How are you today?"
email.write(email_content)
email.send()

text_message = TextMessage()
text_message_content = "Lorem ipsum dolor sit amet, " \
                       "consectetuer adipiscing elit. Aenean commodo " \
                       "ligula eget dolor. Aenean massa. Cum sociis natoque penatibus " \
                       "et magnis dis p"
text_message.write(text_message_content)
text_message.send()

print(len(text_message.read()))

letter = Letter()
letter_content = "Dear someone, it was very pleasant to meet you yeterday."
letter.write(letter_content)
print(letter.read())
letter.send()









