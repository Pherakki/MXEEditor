class SCTemplateComponent:
    def __init__(self, stride, count, type_):
        self.type = type_
        self.count = count
        self.stride = stride
        
    def __repr__(self):
        return f"<{self.classname}> Type: {self.type} Stride: {self.stride} Count: {self.count}</{self.classname}>"

    @property
    def classname(self):
        raise NotImplementedError
        
    @property
    def get_item_size(self):
        raise NotImplementedError

    def unpack(self):
        return [self.stride + i*self.get_item_size() for i in range(self.count)]
