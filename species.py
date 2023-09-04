class Species :
    def __init__(self, name, max_length = 0.0, min_length = 0.0, max_width = 0.0, min_width = 0.0):
        self.name = name
        self.max_length = max_length
        self.min_length = min_length
        self.max_width = max_width
        self.min_width = min_width
        self.min_area = min_length * min_width
        self.max_area = max_length * max_width