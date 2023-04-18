class Project:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def sort_by_name(self):
        return self.name

    def __repr__(self):
        return "%s_%s" % (self.name, self.description)

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description
