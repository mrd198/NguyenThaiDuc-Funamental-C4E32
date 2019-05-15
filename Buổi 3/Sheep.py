s = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Duc and these are my ship sizes")
print(s)
max(s)
print("Now my biggest sheep has size",max(s),"let's shear it")
s[s.index(max(s))] = 8
print("After shearing, here is my flock")
print(s)
for v in range(3):
    print("MONTH",v+1)
    print("One month has passed, now here is my flock")
    for i in range(len(s)):
        s[i]= s[i] + 50
    print(s)
    print("My flock has size in total:",sum(s))
    print("I would get", sum(s),"* 2$ =",sum(s)*2,"$")
    print("Now my biggest sheep has size",max(s),"let's shear it")
    s[s.index(max(s))] = 8
    print("After shearing, here is my flock")
    print(s)