

import os


files = os.listdir("./static/imgs/lunar")

mapped= []
p = open("paste.txt", "a")
for f in files:

    p.write(f"<option value=\"{f}\">{f[14:24]}</option>\n")
    #print(f[14:24])