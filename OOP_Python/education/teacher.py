import education.pupil
class Teacher:
    def teach(self,info,*pupil):
        for i in pupil:
            i.take(info)