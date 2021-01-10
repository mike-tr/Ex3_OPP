def is_primitive(obj):
    return not hasattr(obj, '__dict__')


class _HeapMember:
    def modify(self, index, priority, heap_id):
        self.heap_index = index
        self.heap_priority = priority
        self.heap_id = heap_id

    def remove(self):
        delattr(self, "heap_index")
        delattr(self, "heap_priority")
        delattr(self, "heap_id")

    def __init__(self):
        self.heap_index = -3
        self.heap_priority = -1
        self.heap_id = -1


def is_member(item):
    return hasattr(item, "heap_id")


class Heap:
    next_id = 0

    def __init__(self):
        self._arr = []
        self._size = 0
        self.id = Heap.next_id
        self._bound = 0
        self.real_size = 0
        Heap.next_id += 1

    def in_heap(self, item):
        return hasattr(item, "heap_id") and item.heap_id == self.id

    def __str__(self):
        s = "["
        b = False

        for i in range(self._size):
            item = self._arr[i]
            if b:
                s += ", %d" % item.heap_priority
            else:
                s += "%d" % item.heap_priority
                b = True
        s += "]"
        return s

    def __del__(self):
        for i in range(self._size):
            _HeapMember.remove(self.get_item(i))
        # for item in self._arr:
        #     _HeapMember.remove(item)
        self._arr = []
        self._size = 0

    def add_item(self, item, priority):
        if is_primitive(item):
            print("primitives types are not supported by heap!")
            return
        if is_member(item):
            return
        _HeapMember.modify(item, self._size, priority, self.id)
        # item.heap_index = self._size
        # item.heap_priority = priority
        self._bound = int(self._size / 2) - 1

        if self.real_size > self._size:
            self._arr[self._size] = item
        else:
            self._arr.append(item)
            self.real_size += 1

        self._size += 1
        self._heapify_up(item)

    def getlast(self):
        if self._size > 0:
            return self._arr[self._size - 1]

    def remove(self, item: _HeapMember):
        if is_member(item) and item.heap_id == self.id:
            priority = item.heap_priority
            last = self.getlast()
            self._swap(item, last)
            _HeapMember.remove(item)
            self._size -= 1
            self._bound = int(self._size / 2) - 1
            # self._arr.remove(item)
            if self.size() > 0:
                self._heapify_down(last)
            return item, priority
        else:
            print("Cannot remove : Item not in heap")

    def size(self):
        return self._size

    def pop_first(self):
        if self._size > 0:
            return self.remove(self.get_item(0))

    def heapify_up(self, item: _HeapMember, priority: float):
        if is_member(item):
            if item.heap_id != self.id:
                print("item is member of another heap, can't heapify")
                return
            if item.heap_priority < priority:
                print("can't heapify down wrong priority")
                return
            item.heap_priority = priority
            self._heapify_up(item)
            return
        print("item not in heap, can't heapify")

    def heapify_down(self, item: _HeapMember, priority: float):
        if is_member(item):
            if item.heap_id != self.id:
                print("item is member of another heap, can't heapify")
                return
            if item.heap_priority > priority:
                print("can't heapify down wrong priority")
                return
            item.heap_priority = priority
            self._heapify_down(item)
            return
        print("item not in heap, can't heapify")

    def get_item(self, index) -> _HeapMember:
        return self._arr[index]

    def _swap(self, item1: _HeapMember, item2: _HeapMember):
        index1 = item1.heap_index

        item1.heap_index = item2.heap_index
        item2.heap_index = index1

        self._arr[item1.heap_index] = item1
        self._arr[item2.heap_index] = item2

    def _heapify_up(self, item: _HeapMember):
        if item.heap_index == 0:
            return
        target_index = int((item.heap_index - 1) / 2)
        target = self.get_item(target_index)

        while target.heap_priority > item.heap_priority:
            self._swap(target, item)
            if item.heap_index == 0:
                return
            target_index = int((item.heap_index - 1) / 2)
            target = self.get_item(target_index)

    def _heapify_down(self, item: _HeapMember):
        if item.heap_index > self._bound:
            return

        child_index = (item.heap_index + 1) * 2
        target = self.get_item(child_index - 1)
        while target.heap_priority < item.heap_priority:
            if child_index < self._size:
                right_child = self.get_item(child_index)
                if right_child.heap_priority < target.heap_priority:
                    target = right_child
            else:
                self._swap(target, item)
                return
            self._swap(target, item)
            if item.heap_index > self._bound:
                return
            child_index = item.heap_index * 2 + 1
            target = self.get_item(child_index)
            child_index += 1

        if child_index < self._size:
            right_child = self.get_item(child_index)
            if right_child.heap_priority < item.heap_priority:
                self._swap(right_child, item)
                self._heapify_down(item)

        # child_index = (item.heap_index + 1) * 2
        # left = self.get_item(child_index - 1)
        # if child_index >= self._size:
        #     if left.heap_priority < item.heap_priority:
        #         self._swap(left, item)
        #     return
        #
        # right = self.get_item(child_index)
        # if left.heap_priority < item.heap_priority:
        #     if right.heap_priority < left.heap_priority:
        #         self._swap(right, item)
        #     else:
        #         self._swap(left, item)
        #     self._heapify_down(item)
        # elif right.heap_priority < item.heap_priority:
        #     self._swap(item, right)
        #     self._heapify_down(item)
