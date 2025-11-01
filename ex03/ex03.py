import os
from datetime import datetime

try:
    username=os.getlogin()
except OSError:
    username="Unknown"

def smart_log(*args,**kwargs)->None:
    line=""
    now=datetime.now()
    date=bool(kwargs.get("date",True))
    if date:
        line+=now.strftime("%Y.%m.%d")+" "
        line+=" "
    timestamp=bool(kwargs.get("timestamp",True))
    if timestamp:
        line+=now.strftime("%H:%M:%S")
        line+=" "
    level=str(kwargs.get("level","info"))
    line+="["+level.upper()+"] "
    for arg in args:
        line+=str(arg)+" "
    color=bool(kwargs.get("color",True))
    if color:
        if level=="info":
            color_code="\033[34m"
        elif level=="debug":
            color_code="\033[90m"
        elif level=="warning":
            color_code="\033[33m"
        elif level=="error":
            color_code="\033[31m"
        print(f"{color_code}{line}")
    else:
        base="\033[0m"
        print(f"{base}{line}")
    save_to=kwargs.get("save_to",None)
    if save_to:
        with open(save_to,"a",encoding="utf-8") as file:
            file.write(line+"\n")

if __name__=="__main__":
    smart_log("System started successfully.",level="info",timestamp=False)
    smart_log("User", username, "logged in",level="debug",timestamp=True)
    smart_log("Low disk space detected!",level="warning",date=False,save_to="ex03/log.txt")
    smart_log("Model", "training", "failed!", level="error",color=True,save_to="ex03/log.txt")
    smart_log("Process end",level="info",color=False,save_to="ex03/log.txt")