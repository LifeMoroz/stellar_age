class PriorityList(list):
    def __contains__(self, item):
        return isinstance(item, tuple(self))
