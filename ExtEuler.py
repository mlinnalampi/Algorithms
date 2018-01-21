r=[]
q=[]
t=[]
s=[]
r.append(int(input("Give r0\n")))
r.append(int(input("Give r1\n")))
s.append(1)
s.append(0)
t.append(0)
t.append(1)
q.append("")
i=0
while r[-1]!=0:
    print("i:", i, "\tr:", r[i], "\ts:", s[i], "\tt:", t[i], "q:",q[i])
    q.append(int(r[-2])//int(r[-1]))
    r.append(r[-2]%r[-1])
    s.append(s[-2]-q[-1]*s[-1])
    t.append(t[-2]-q[-1]*t[-1])
    i+=1
print("i:", i, "\tr:", r[i], "\ts:", s[i], "\tt:", t[i], "q:",q[i]);i+=1;
print("i:", i, "\tr:", r[i], "\ts:", s[i], "\tt:", t[i])


print(s[-2],"*",r[0],"+",t[-2],"*",r[1],"=",s[-2]*r[0]+t[-2]*r[1])
