from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[0]
        less = [x for x in data[1:] if x.speed < pivot.speed]
        greater = [x for x in data[1:] if x.speed >= pivot.speed]
        return self.sort(less) + [pivot] + self.sort(greater)

class MergeSortStrategy(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        middle = len(data) // 2
        left = self.sort(data[:middle])
        right = self.sort(data[middle:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        while left and right:
            if left[0].speed < right[0].speed:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left)
        result.extend(right)
        return result
