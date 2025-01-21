# the binary search function takes a sorted array/list and an item to search for

# create binary search for a list of numbers

def binary_search(list_of_numbers:list, item:int)->int:
    first_index = 0
    last_index = len(list_of_numbers) -1
    print(f"firs_index = {first_index}, last_index = {last_index}")

    while first_index <= last_index:
        print("checking")
        middle_index = (first_index + last_index)//2
        guess = list_of_numbers[middle_index]
        if guess == item:
            return middle_index
        if guess > item: # meaning the number is smaller than the middle number
            last_index = middle_index -1 #break the array/list to have index[0]-index[middle_index -1]
            print(f"last index is now = {last_index}")
        else:
            first_index = middle_index + 1
            print(f"first index is now = {first_index}")
            
    

print(binary_search([1,2,3,4,5,6,7,8, 9, 10, 11, 12, 13], 3))         