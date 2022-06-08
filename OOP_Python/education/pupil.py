import random
class Pupil:
    def __init__(self):
        self.knowelege=[]
    def take(self,info):
        self.knowelege.append(info)

    def __del__(self):
        self.randomVal=random.randrange(0,len(self.knowelege))
        self.knowelege.__delitem__(self.randomVal)
