class Buffer():
    def __init__(self):
        self.list = []

    def add(self, *part):
        for elem in part:
            self.list.append(elem)
            if len(self.list) == 5:
                s = 0
                for i in range(5):
                    s += self.list.pop(0)
                print(s)

    def get_current_part(self):
        return self.list
