import array

class SCUnpackedTemplateComponents:
    __slots__ = ("values", "type")
    
    def __init__(self, values, type_):
        self.values = array.array('I', values)
        self.type = type_
        self.__validate()
                   
    def __getitem__(self, idx):
        return self.values[idx]
    
    def __len__(self):
        return len(self.values)
    
    def __iter__(self):
        for elem in self.values:
            yield elem
     
    def __repr__(self):
        return f"<{self.classname} UTC>{{{self.type}}} {list(self.values)}</{self.classname} UTC>"

    def get_item_size(self):
        return self.get_type_sizes()[self.type]
    
    @property
    def classname(self):
        raise NotImplementedError
    
    def get_type_sizes(self):
        raise NotImplementedError
        
    def __validate(self):
        sz = self.get_type_sizes()[self.type]
        for v1, v2 in zip(self.values, self.values[1:]):
            if v1 + sz != v2:
                raise ValueError(f"{self.classname} initialisation was attempted with non-contiguous data.")
        
class SCTemplate:
    __slots__ = ("components",)
    
    def __init__(self):
        self.components = []
        
    def __getitem__(self, idx):
        return self.components[idx]
            
    def __len__(self):
        return len(self.components)
    
    def __iter__(self):
        for elem in self.components:
            yield elem
    
    def __repr__(self):
        out = "<SC UT>" 
        for tg in self.components:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        out += "\n</SC UT>"
        return out
    
    def get_first_offset(self):
        return self[0][0]
    
    def append(self, item):
        if not issubclass(type(item), SCUnpackedTemplateComponents):
            raise TypeError(f"Tried to append \'{type(item)}\', expected subclass of SCUnpackedTemplateComponents.")
        self.components.append(item)
        
    def flatten(self):
        return [subitem for item in self for subitem in item]
    
    def typed_flatten(self):
        return [(subitem, item.type) for item in self for subitem in item]

class SCTemplatePack:
    __slots__ = ("templates", "stride")
    
    def __init__(self, stride):
        self.templates = []
        self.stride = stride
        
    def __getitem__(self, idx):
        return self.templates[idx]
        
    def __len__(self):
        return len(self.templates)
    
    def __iter__(self):
        for elem in self.templates:
            yield elem
    
    def __repr__(self):
        out = f"<SC UTP> Stride: {self.stride}"
        for tg in self.templates:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        out += "\n</SC UTP>"
        return out
    
    def get_first_offset(self):
        return self[0][0][0]
    
    def append(self, item):
        if type(item) != SCTemplate:
            raise TypeError(f"Tried to append \'{type(item)}\', expected SCTemplate.")
        if len(self.templates):
            self.__validate(item)
        self.templates.append(item)
        
    def flatten(self):
        return [subitem for item in self for subitem in item.flatten()]
    
    def typed_flatten(self):
        return [subitem for item in self for subitem in item.typed_flatten()]

    def __validate(self, new_data):
        for new_elems, first_elems in zip(new_data, self.templates[0]):
            new_subelems = [ne - new_elems[0] for ne in new_elems]
            first_subelems = [fe - first_elems[0] for fe in first_elems]
            if new_subelems != first_subelems:
                raise TypeError("Attempted to append a Template Instance that did not match the Template.")