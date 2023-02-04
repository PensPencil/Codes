from pprint import pprint
class SRMIST:
    def __init__(self,school,dept1,dept2,dept3):
        self.school = school
        self.dept1 = dept1
        self.dept2 = dept2
        self.dept3 = dept3
student = SRMIST('ABC','CSE','Mech','AI')
pprint(vars(student))
setattr(student,'Specialization','Software')
pprint(vars(student))
delattr(student,'dept1')
delattr(student,'dept2')
pprint(vars(student))