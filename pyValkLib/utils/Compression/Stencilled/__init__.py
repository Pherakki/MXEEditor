from .relative import SCRelativeTemplateGenerator
from .absolute import SCAbsoluteTemplateGenerator
from .unpacked import SCTemplate, SCTemplatePack

class SCRelRep:
    @property
    def classname(self):
        raise NotImplementedError
        
    @property
    def absclass(self):
        raise NotImplementedError
        
    def __init__(self):
        self.template_generators = []
        
    def __repr__(self):
        out = ""
        for tg in self.template_generators:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        return f"<{self.classname}>{out}\n</{self.classname}>"

    def __getitem__(self, idx):
        return self.template_generators[idx]
    
    def append(self, item):
        if type(item) != SCRelativeTemplateGenerator:
            raise TypeError(f"Tried to append \'{type(item)}\', expected SCRelativeTemplateGenerator.")
        self.template_generators.append(item)
    
    def to_abs_rep(self):
        out = self.absclass()
        
        prev_offset = 0
        for tg in self.template_generators:
            atg = SCAbsoluteTemplateGenerator(tg.jump + prev_offset, tg.stride, tg.count, tg.subs)
            prev_offset += tg.jump
            out.append(atg)
        
        return out
    
class SCAbsRep:
    @property
    def classname(self):
        raise NotImplementedError
        
    @property
    def relclass(self):
        raise NotImplementedError
        
    @property
    def unpackedclass(self):
        raise NotImplementedError
        
    @property
    def utcclass(self):
        raise NotImplementedError
    
    def __init__(self):
        self.template_generators = []
        
    def __getitem__(self, idx):
        return self.template_generators[idx]
    
    def __repr__(self):
        out = ""
        for tg in self.template_generators:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        return f"<{self.classname}>{out}\n</{self.classname}>"
    
    def append(self, item):
        if type(item) != SCAbsoluteTemplateGenerator:
            raise TypeError(f"Tried to append \'{type(item)}\', expected SCAbsoluteTemplateGenerator.")
        self.template_generators.append(item)
        
    def to_rel_rep(self):
        out = self.relclass()
        
        prev_offset = 0
        for atg in self.template_generators:
            tg = SCRelativeTemplateGenerator(atg.offset - prev_offset, atg.stride, atg.count, atg.subs)
            prev_offset = atg.offset
            out.append(tg)
        
        return out
    
    def to_unpacked_rep(self):
        out = self.unpackedclass()
        
        for atg in self.template_generators:
            tpack = SCTemplatePack(atg.stride)
            
            # Generate the template
            prev_offset = 0
            utcs = []
            pack_offset = atg.offset
            for template_comp in atg.subs:
                offsets = [item + prev_offset for item in template_comp.unpack()]
                utcs.append((offsets, template_comp.type))
                prev_offset = offsets[-1] + template_comp.get_item_size()
            
            # Now copy the template
            for template_copy_idx in range(atg.count):
                ct = SCTemplate()
                
                for offsets, type_ in utcs:
                    abs_offsets = [pack_offset + item for item in offsets]
                    utc = self.utcclass(abs_offsets, type_)
                    ct.append(utc)
                    
                pack_offset += atg.stride
                
                tpack.append(ct)
            out.append(tpack)
        return out


class SCUnpackedRep:
    __slots__ = ("template_packs",)
    
    def __init__(self):
        self.template_packs = []
        
    @property
    def component_type(self):
        raise NotImplementedError
    
    @property
    def classname(self):
        raise NotImplementedError
        
    @property
    def absclass(self):
        raise NotImplementedError

    def __repr__(self):
        out = f"<{self.classname}>"
        for tg in self.template_packs:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        out += "\n" + f"</{self.classname}>"
        return out
    
    def __getitem__(self, idx):
        return self.template_packs[idx]
    
    def __setitem__(self, idx, item):
        if type(item) is not SCTemplatePack:
            raise TypeError(f"Tried to set index {idx} to type \'{type(item)}\', expected SCTemplatePack.")
        self.template_packs[idx] = item
    
    def __delitem__(self, idx):
        del self.template_packs[idx]
        
    def insert(self, idx, item):
        self.template_packs.insert(idx, item)
    
    def __len__(self):
        return len(self.template_packs)
    
    def __iter__(self):
        for elem in self.template_packs:
            yield elem
    
    def append(self, item):
        if type(item) != SCTemplatePack:
            raise TypeError(f"Tried to append \'{type(item)}\', expected SCTemplatePack.")
        self.template_packs.append(item)
    
    def flatten(self):
        return [subitem for item in self for subitem in item.flatten()]
    
    def typed_flatten(self):
        return [subitem for item in self for subitem in item.typed_flatten()]
    
    def get_first_offset(self):
        return self[0].get_first_offset()
    
    def to_abs_rep(self):
        out = self.absclass()
        
        for tpack in self:
            tpack_offset = tpack.get_first_offset()
            first_template = tpack[0]
            subs = []
            # Check that elements are contiguous?
            prev_offset = tpack_offset
            for component in first_template:
                comp_stride = component[0] - prev_offset
                subs.append(self.component_type(comp_stride, len(component), component.type))
                prev_offset = component[-1] + component.get_item_size()
            
            # Check that all subsequent templates match the first?
            
            atg = SCAbsoluteTemplateGenerator(tpack_offset, tpack.stride, len(tpack), subs)
            out.append(atg)
        return out
