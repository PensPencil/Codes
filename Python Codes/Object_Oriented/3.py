class dept:
    def __init__(self,name = 'SCO'):
        self.name = name
student1 = dept('ABc')
student2 = dept()
print(student1.name)
print(student2.name)