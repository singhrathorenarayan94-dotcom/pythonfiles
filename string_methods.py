#case methods
s = "python Programming"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
#space methods
a = "      hello world      "
print(a.strip())
print(a.lstrip())
print(a.rstrip())
#search methods
n = "i live in india and india is great"
print(n.find("india"))
print(n.count("india"))
print(n.startswith("i"))
print(n.endswith("great"))
#replace
x = "python is easy"
x = x.replace("easy","powerful")
print(x)
#split
m = "my name is python"
print(m.split())
#join
r = ["2025","07","15"]
print("/".join(r))
#validation methods
k = "HELLO"
print(k.isupper())
k1 = "hello"
print(k1.islower())
num = "123456"
print(num.isnumeric())
t = "python123"
print(t.isalnum())
