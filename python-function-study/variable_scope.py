#变量作用域
c='e'
def variable_scope():
     c = 'd'
     print(c) # d
variable_scope()
print(c) #e

#全局作用域
def global_variable_scope():
    global c 
    c = 'd'
    print(c)  # d
global_variable_scope() #d
print(c)  # d

def nonlocal_variable_scope():
    no_local_p = 'aa'
    def inner_fun():
        nonlocal no_local_p  
        no_local_p = 'd'
        print(no_local_p)  # d
    inner_fun()
    print(no_local_p)
nonlocal_variable_scope()  # d

