class commands(object):
    command = ("append")
    c = command

    def __init__(self, command, content):
        self.command = command
        

    if c == 'append':
        m.append(content)
        

    elif c == 'get pw':
        if m.find(content):
            input("What do you want to set the password to?\n> ")
            
        else:
            print("Password not found.")
        
    elif c == 'erase pw':
        if m.find(content):
            print("Are you sure you want to erase the password?")

    elif c == 'change pw':
        old = input("What old password would you like to change?\n> ")
        check = m.find(old)
        if check == -1:
            print("Could not find password.")
        new = input("What password would you like to set it to?\n> ")
        repeat = input("Please Repeat new password: ")
        if new == repeat:
                m.replace(old,new)

    elif c == 'erase all pws':
        m.truncate(0)

    else:
        print("I don't know this command.")
        exit()