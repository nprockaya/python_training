class ContactInGroup:
    def __init__(self, _contact_id=None, _group_id=None):
        self.contact_id = _contact_id
        self.group_id = _group_id

    def __repr__(self):
        return "%s:%s" % (self.contact_id, self.group_id)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id) and (
                self.group_id is None or other.group_id is None or self.group_id == other.group_id)
