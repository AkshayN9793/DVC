

with open("artifact.txt","r")as f:
    text=f.read()
with open("artifact.txt","w") as f:
    text=f.write(text+"i added one line")
    
print(text)
print("end of stage 3")