# declaring the email class and its variables and functions
class Email:
    has_been_read = False
    email_contents = ""
    is_spam = False
    from_address = ""

    # this is the constuctor which sets the variables upon creation
    def __init__(self, from_address, email_contents):
        self.has_been_read = False
        self.from_address = from_address
        self.is_spam = False
        self.email_contents = email_contents

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True


# declare the inbox as a list
inbox = []

def add_email(senders_address, email_contents):
    inbox.append(Email(senders_address, email_contents))

def get_count():
    return len(inbox)

def get_email(index):
    # try to get the email at the given index and return its contents, if it can't then it will print an error
    try:
        inbox[index].mark_as_read()
        return inbox[index].email_contents
    except:
        print(f"Unable to find email at index {index}, please try again with a different index")


def get_unread_emails():
    unread_emails = []
    for email in inbox:
        if email.has_been_read is not True:
            unread_emails.append(email)

    return unread_emails


def get_spam_emails():
    spam_emails = []

    for email in inbox:
        if email.is_spam is True:
            spam_emails.append(email)

    return spam_emails


def delete(index):
    del inbox[index]


#An Email Simulation

user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":
        # gets the email at the given index and prints out the contents and sets the email to read
        index = int(input("Please enter the index of the email you would like to read "))
        print(get_email(index))
    elif user_choice == "mark spam":
        # marks the requested email at the index provided as spam
        index = int(input("Please enter the index of the email you would like to mark as spam "))
        inbox[index].mark_as_spam()
    elif user_choice == "send":
        # asks the user to input an email address and the contents and adds it to the inbox
        sender_address = input("Please enter the senders address ")
        email_contents = input("Please enter the contents of the email")
        add_email(sender_address, email_contents)
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
