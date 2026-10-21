class Demo:
    def instance_method(self):
        print("I am an instance method,self =", self)

    @classmethod
    def class_method(cls):
        print("I am a class method, cls =", cls)
d = Demo()
d.instance_method() #called on object
Demo.class_method() #called on class