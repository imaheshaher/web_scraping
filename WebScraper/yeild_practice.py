def square():
    i=1
    while i<10:
        yield i*i
        i+=1

    
for i in square():
    print(i)