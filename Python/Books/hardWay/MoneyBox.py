class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.val = 0

    def can_add(self, val):
        if self.val + val <= self.capacity:
            return True
        else:
            return False

    def add(self, val):
        if self.can_add(val):
            self.val += val


box = MoneyBox(20)
box.can_add(13)
box.add(13)
box.can_add(7)
box.add(8)
box.can_add(7)
