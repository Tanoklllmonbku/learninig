from sorting.base import BaseSorting, SortAlgFactory


@SortAlgFactory.register('bubble')
class BubbleSort(BaseSorting):
    """Bubble Sort"""
    def __init__(self, data:list):
        super().__init__(data)
        self.data = data

    def result(self):
        last_el_index = len(self.data)-1
        for pass_no in range(last_el_index, 0, -1):
            for id in range(pass_no):
                if self.data[id] > self.data[id+1]:
                    self.data[id], self.data[id+1] = self.data[id+1], self.data[id]
        return self.data