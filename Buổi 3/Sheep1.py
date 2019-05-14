S = [5, 7, 300, 90, 24, 50, 75]
print("Hello my name is NDuc and these are my ship sizes",end='')
print(S)
print("Now my biggest sheep has size",max(S)," let's shear it")
S[S.index(max(S))] = 8
print("After shearing, here is my flock",end='')
print(S)
for v in range(5):
    print("MONTH",v+1)  
    for i in range(len(S)):
        S[i] = S[i] + 50
    print("1 month has passed, now here is my flock")
    print(S)  
    print("My flock has size in total:",sum(S))
    print("i would get",sum(S),"* 2$ =",sum(S)*2,"$") 
    print("Now my biggest sheep has size",max(S),"let's shear it")
    S[S.index(max(S))] = 8
    print("After shearing, here is my flock")
    print(S)
    