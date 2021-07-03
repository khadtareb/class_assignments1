# #. Python | Remove empty tuples from a list
l=[3,2,6,(),4,7,()]
for i in l:
    if i==():
        l.remove(())
print(l)



