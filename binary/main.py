# a function that takes a 'list' and 'target' param
def bi_search(my_list, target):
# multiple variables: middle, start, end, steps
    middle = 0
    start = 0
    end = len(my_list)
    steps = 0
    
# recursion or while loop
    while start <= end:
        print("step", steps, ":", str(my_list[start:end+1]))
        
        
# increase steps each time a split is done
        steps = steps + 1
        middle = (start + end) // 2
        
# conditions to track target position
        if target == my_list[middle]:
            return middle
        elif target < my_list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return - 1

my_list = [1, 2, 3, 4, 5, 6, 7,8, 9, 10]
element = 2

bi_search(my_list, element)