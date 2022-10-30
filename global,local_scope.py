#Global & Local Variables

x=100 #Global Variabe
def fun1():
def fun2():
        x=10 #Local Variable
        print("Local Varable Value",x)
    global x
    print("Global Variable Value",x)

fun2()
fun1()