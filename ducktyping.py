class pdf:
    def send(self,name):
        print(name)
class email:
    def send(self,name):
        print(name)
class chat:
    def send(self,name):
        print(name) 
 
def notify_all(items):
    items.send("faraz")     
for dis in [pdf(),email(),chat()]:
    notify_all(dis)