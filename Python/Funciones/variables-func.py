def func():
    global s
    s = 5
    print(s)

s = 10
print(s)
func()
print(s)