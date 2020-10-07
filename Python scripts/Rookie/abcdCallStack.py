globo='I am in global'

print(globo)
def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    global globo
    globo='I was modified within d() local scope'
    print('d() returns')

a()
print(globo)
