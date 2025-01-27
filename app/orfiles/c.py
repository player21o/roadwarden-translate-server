import os

txt = ""

for filename in os.listdir("/home/player210/websocket/roadwarden-translate-server/app/orfiles"):
    if filename.endswith(".rpy"): 
        #print(filename)
        new = filename.split('.rpy')[0]

        txt += f'export const {new}File = pgTable("{new}rpy", cardSchema)\n'

txt += 'export const files = {\n'

for filename in os.listdir("/home/player210/websocket/roadwarden-translate-server/app/orfiles"):
    if filename.endswith(".rpy"): 
        txt += f'"{filename}": {filename.split(".rpy")[0]}File,\n'

txt += '}'

print(txt)