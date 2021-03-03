class Group:
    def __init__(self, _name=None, _header=None, _footer=None, _id=None):
        self.name = _name
        self.header = _header
        self.footer = _footer
        self.id = _id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name