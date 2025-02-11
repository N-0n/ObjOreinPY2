class employee:
    def ___init__(self):
        print("employee created")
    def ___del__(self):
        print("Employee object deleted")
obj=employee()#constructor
del obj #destructor