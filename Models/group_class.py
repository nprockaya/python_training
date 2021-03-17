from sys import maxsize


class Group:
    def __init__(self, _name=None, _header=None, _footer=None, _id=None):
        self.name = _name
        self.header = _header
        self.footer = _footer
        self.group_id = _id

    def __repr__(self):
        return "%s:%s" % (self.group_id, self.name)

    def __eq__(self, other):
        return (self.group_id is None or other.group_id is None or self.group_id == other.group_id) and self.name == other.name

    def id_or_max(self):
        if self.group_id:
            return int(self.group_id)
        else:
            return maxsize
