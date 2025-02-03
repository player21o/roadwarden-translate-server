import os

txt = ""

for filename in os.listdir("/home/player210/websocket/roadwarden-translate-server/app/orfiles"):
    if filename.endswith(".rpy"): 
        #print(filename)
        new = filename.split('.rpy')[0]

        txt += new + ' = "' + new + '",'

print(txt)