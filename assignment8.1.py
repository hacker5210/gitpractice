fname = input("Enter the file name: ")
fhandle = open(fname,'r')
x = list()
for line in fhandle:
    line=line.strip()
    words=line.split()
    for word in words:
        if word in x:
            continue
        else:
            x.append(word)
x.sort()
print(x)
