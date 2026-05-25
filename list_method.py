#append
a = [10,20,30]
a.append(40)
print(a)
#insert
a.insert(1,15)
print(a)
#extend
a.extend([50,60,70])
print(a)
#remove
a.remove(20)
print(a)
#pop
a.pop()
print(a)
a.pop(0)
print(a)
#sort
b = [5,8,1,9,2]
b.sort()
print(b)
#reverse sort
b.sort(reverse=True)
print(b)
#sorted
c = [11,3,7,2]
d = sorted(c)
print(c)
print(d)
#count
x = [1,2,2,3,2,5]
print(x.count(2))
#index
print(x.index(3))
#reverse
x.reverse()
print(x)
#copy
m = [100,200,300]
n = m.copy()
n.append(400)
print(m)
print(n)
#clear
k = [1,2,3,4]
k.clear()
print(k)
#join
r = ["my","name","is","python"]
print("-".join(r))
#split
s = "i live in india"
print(s.split())
#type conversion
t = "abcdef"
t = list(t)
print(t)
