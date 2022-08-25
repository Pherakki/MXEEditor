class SCAbsoluteTemplateGenerator:
    def __init__(self, offset, stride, count, subs):
        self.offset = offset
        self.stride = stride
        self.count = count
        self.subs = subs
        
    def __getitem__(self, idx):
        return self.subs[idx]
        
    def __repr__(self):
        out = ""
        for sub in self.subs:
            out += f"\n\t{sub}"
        return f"<SCAbsGen> Offset: {self.offset} Stride: {self.stride} Count: {self.count}{out}\n</SCAbsGen>"
