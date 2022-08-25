from pyValkLib.serialisation.Serializable import Serializable


class PointerIndexableArray(Serializable):
    def __init__(self, context):
        super().__init__(context)
        #self.context.anchor_pos = context.anchor_pos
        #self.context.endianness = context.endianness
        
        self.data = []
        self.ptr_to_idx = {}
        self.idx_to_ptr = {}
        
    def at_ptr(self, ptr):
        return self.data[self.ptr_to_idx[ptr]]
    
    def at_idx(self, idx):
        return self.data[idx]

    def __getitem__(self, idx):
        return self.data[idx]

    def __iter__(self):
        for elem in self.data:
            yield elem
    
    def read_write(self, rw):
        rw.mark_new_contents_array()
        for i, elem in enumerate(self.data):
            rw.mark_new_contents_array_member()
            if i in self.idx_to_ptr:
                rw.assert_local_file_pointer_now_at("Start of Array Entry", self.idx_to_ptr[i])
            curpos = rw.local_tell()
            self.ptr_to_idx[curpos] = i
            self.idx_to_ptr[i] = curpos

            self.rw_element(rw, i)
            

    def rw_element(self, rw, idx):
        rw.rw_obj(self.data[idx])
        
    def rw_element_method(self, rw, func, idx):
        rw.rw_obj_method(self.data[idx], getattr(self.data[idx], func.__name__))
        
    def __len__(self):
        return len(self.data)
    
class PointerIndexableArrayInt8(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_int8(self.data[idx])
    
class PointerIndexableArrayUint8(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_uint8(self.data[idx])
    
class PointerIndexableArrayInt16(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_int16(self.data[idx])
    
class PointerIndexableArrayUint16(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_uint16(self.data[idx])
    
class PointerIndexableArrayInt32(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_int32(self.data[idx])
    
class PointerIndexableArrayUint32(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_uint32(self.data[idx])
    
class PointerIndexableArrayInt64(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_int64(self.data[idx])
    
class PointerIndexableArrayUint64(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_uint64(self.data[idx])
    
class PointerIndexableArrayFloat16(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_float16(self.data[idx])
    
class PointerIndexableArrayFloat32(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_float64(self.data[idx])
    
class PointerIndexableArrayFloat64(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_float64(self.data[idx])
    
class PointerIndexableArrayCStr(PointerIndexableArray):
    def __init__(self, context, encoding='ascii'):
        super().__init__(context)
        self.encoding = encoding
        
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_cstr(self.data[idx], encoding=self.encoding)
