names = []
for x in range(0,10):
    acceptedName = str (input ("Enter name: "));
    names.append(acceptedName)
print(names)

for x in range(len(names)):
    print(names.pop(0))
print(names)
