class Order():

    def __init__(self, id, style_id, metal_id, size_id):
        self.id = id
        self.style_id = style_id
        self.metal_id = metal_id
        self.size_id = size_id
        self.style = None
        self.metal = None
        self.size = None