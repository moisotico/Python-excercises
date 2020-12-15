
# function to count and parse valid commands
def getCommand(inp, N):
    arguments = inp.split()
    cmd = arguments[0]
    # Remove command from arguments & convert to int
    arguments.pop(0)
    if len(arguments) > 0:
        arguments = list(map(int, arguments))
    # Get the function from switcher dictionary, packing arguments
    func = switcher.get(cmd, "Command error!")(*arguments)
    if func != "Commmand error!":
        N -= 1
    return N

# functions in dictionary


def insert_lst(i, e):
    arr_list.insert(i, e)


def print_lst():
    print(arr_list)


def remove_lst(e):
    arr_list.remove(e)


def append_lst(e):
    arr_list.append(e)


def sort_lst():
    arr_list.sort()


def pop_lst():
    arr_list.pop()


def reverse_lst():
    arr_list.reverse()


# Switcher is a dictionary of functions
switcher = {
    "insert": insert_lst,
    "print": print_lst,
    "remove": remove_lst,
    "append": append_lst,
    "sort": sort_lst,
    "pop": pop_lst,
    "reverse": reverse_lst
}

if __name__ == '__main__':
    arr_list = []
    N = None
    # error catching
    if isinstance(N, int) is False:
        try:
            N = int(input())
        except():
            print("Please write the number of commands to run!")
    while N > 0:
        N = getCommand(input(), N)
        
