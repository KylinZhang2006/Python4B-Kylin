# Message Instruction

### Create a message_instructions.md file, containing the following info:

* Create the following classes: **Message, Email, TextMessage and Letter**
* The classes, **Email, TextMessage and Letter** should all inherit from the **Message parent class**.
* The *Message class* should have a variable called **content** that holds the contents of the message.
There should also be **read and write** methods that get and set the value of content.
* The *Message class* should also have a method called **send** that prints ***“Message sent”***.
* The *Email class* should **override** the *send method* so that it first prints ***“Sending email”*** and then
calls the send method from the parent class.
* The *TextMessage class* should override the *send method* so that it first prints ***“Sending text”*** and
then calls the send method from the parent class.
* The *Letter class* should **override** the *send method* so that it first prints ***“Mailing letter”*** and then
calls the send method from the parent class.
* A text message has a **character limit**. We will say the limit on our text messages is ***144
characters***. The *TextMessage class* should make sure that when you call the write method, your
content is not longer than ***144 characters***. If it is, the content should be **cut off** at 144 characters
and you should print a ***warning message***. (Hint: you can use the built in function len() to check
the length of a string)
* Make sure to commit your code and push it to Github!