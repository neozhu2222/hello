import random
import datetime

def handle_response(message) -> str:
    lmessage =  message.lower()
    
    if lmessage.split()[0] == "flip":
        pass
    
    if lmessage == "hello":
        return "hello"

    if lmessage == "!help":
        return "`to be filled out later`"
    
    if lmessage == "roll":
        return str(random.randint(1,10))
    
    if lmessage == "time":
        return str(datetime.datetime.now().strftime("%H:%M:%S"))
    
    return "code not working"