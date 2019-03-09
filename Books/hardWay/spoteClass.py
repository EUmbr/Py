class Spote():
    def __init__(self, parent):
        self.parent = parent
        self.vars = []
        
    def __str__(self):
        return self.parent, self.vars
    
    def add(self, var):
        self.vars.append(var)
        
    def get(self, var):
        if self.name == 'global' and var not in self.vars:
            print('None')
        elif var in self.vars:
            print(self.name)
        
def create(name, parent):
    s = f'{name} = Spote({parent})'
    eval(s)
    print(s)
    
create('local', 'global')