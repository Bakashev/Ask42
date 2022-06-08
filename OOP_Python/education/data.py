class Data:
    """Constructor Arguments Object and list"""
    def __init__(self,*info):
        self.info=list(info)
    def __getitem__(self, item):
        return self.info[item]