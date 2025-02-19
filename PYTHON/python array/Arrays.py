


class Arrays:
    def __init__(self, array_size:int, type):
        self.array_size = array_size
        self.type = type
        self.array = [None]*array_size


    def insert(self, index:int, value) -> None:
        if self.is_index_out_of_range(index):
            raise IndexError("Index out of range")
        if self.is_a_correct_type(value):
            raise TypeError(f"Value {value} is not of type {self.type}")

        self.array[index] = value
        return self.successful_message()

    def delete(self, index:int):
        if self.is_index_out_of_range(index):
            raise IndexError("Index out of range")

        if self.array[index] is None:
            return
        self.array[index] = None
        return self.successful_message()

    def get(self,index:int):
        if self.is_index_out_of_range(index):
            raise IndexError("Index out of range")
        return self.array[index]

    def update(self, index:int, value) -> None:
        if self.is_index_out_of_range(index):
            raise IndexError("Index out of range")
        self.array[index] = value
        return self.successful_message()

    def search(self, value):
        for element in self.array:
            if value == element:
                return element
        return f"element {value} not found"

    def length(self):
        return len(self.array)

    @staticmethod
    def successful_message():
        print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n Successful")

    def is_index_out_of_range(self, index) -> bool:
        if index >= self.array_size - 1:
            return True
        return False

    def is_a_correct_type(self, value) -> bool:
        if not isinstance(value, self.type):
            return True
        return False


nA = Arrays(5, str)
nA.insert(2, "wisdom")
print(nA.array)

