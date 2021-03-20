class TaskManager:
    def __init__(self):
        self.tasks = []

    def parseadd(self, command):
        return Action("add", command[2:])

    def parsedel(self, numero):
        return Action2("del", numero)



class Action:
    def __init__(self, name, description, numero):
        self.name = name
        self.description = description
        self.numero = numero
        
class Action2:
    def __init__(self):
        pass


#    def __del__(self):
#        print('Destructor called') 
#objet1 = Action2()
#del objet1