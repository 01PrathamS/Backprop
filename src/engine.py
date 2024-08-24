class Value: 

    def __init__(self, data, _children=()): 
        self.data = data 
        self._prev = set(_children) 

    def __repr__(self): 
        return f"Value(data={self.data})"
    
    def __add__(self, other): 
        out = Value(self.data + other.data, (self, other), '+') 
        return out 
    
    def __mul__(self, other): 
        out = Value(self.data * other.data, (self, other), '*')
        return out 