# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from src.utilities.Heap import Heap


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Test:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(arr)

    arr[3] = 10
    print(arr)

    heap = Heap()

    for i in range(10):
        x = Test(150 - i * 5)
        heap.add_item(x, 150 - i * 5)
    print(heap)

    item = heap.get_item(5)
    print(item)
    item.x = 10
    heap.heapify_up(item, 10)
    print(heap)

    k = heap.pop_first()
    print(k[0], heap)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
