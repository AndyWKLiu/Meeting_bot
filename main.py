#Modules needed 
import webbrowser
from datetime import datetime

#Only input you'll need - the time you need to open the meeting by
timer = str(input('Please enter a time: '))

url = '' #Insert url between the quotes
current_time = datetime.now().strftime("%H:%M")
print(current_time)


while True:
    if current_time != timer:
        current_time = datetime.now().strftime("%H:%M")
        pass
    else: 
        webbrowser.open(url)
        break
