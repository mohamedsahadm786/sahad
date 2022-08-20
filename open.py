g = open("sahad.py","w")
g.write("a='mohamed '\nb='sahad '\nc='madathodiyil'\nprint(a+b+c)")
g.close()
print("----------------------------------------------------------------------------------")

with open("sahad.py","r") as f:
    x=f.read()

    print(x)