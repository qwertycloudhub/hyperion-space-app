

import os


files = os.listdir("./static/imgs/mars")

mapped= []
p = open("paste.txt", "a")
for f in files:
    p.write(f"<option value=\"{f}\">{f.replace(".png", "")}</option>\n")

