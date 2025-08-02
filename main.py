class Node:
    def __init__(self, number):
        self.number = number
        self.next = None

def make_new_node(x):
    return Node(x)

def order_insert(first, x):
    if first is None:
        return make_new_node(x)
    elif x == first.number:
        print("\t This value in node is Exist")
        return first
    elif x < first.number:
        new_node = make_new_node(x)
        new_node.next = first
        return new_node
    else:
        first.next = order_insert(first.next, x)
        return first

def posh(first, n):
    for i in range(1, n + 1):
        x = int(input(f" Node # {i}\n"))
        first = order_insert(first, x)
    return first

def pop(first):
    if first is None:
        print("No, Node found >>>>")
        return None
    elif first.next is None:
        r = first.number
        print(f"This node's number deleted ----> {r}")
        return None
    else:
        p = first
        while p.next.next is not None:
            p = p.next
        q = p.next
        r = q.number
        p.next = None
        print(f"This node's number deleted ----> {r}")
        return first

def main():
    print("\t\t\t\t\t ********Welcome to my program******** \n")
    first = None

    while True:
        print("\n\n\t WHAT DO YOU WANT TO DO ??\n\n"
              "\t*************************************\n"
              "\t*\t 1- Posh *\n"
              "\t*\t 2- Pop *\n"
              "\t*\t 3- Exit program *\n"
              "\t*************************************")
        r = int(input())
        if r == 1:
            n = int(input("\t Enter number of nodes to create\n"))
            first = posh(first, n)
        elif r == 2:
            first = pop(first)
        elif r == 3:
            ok = input("Are you sure you want to exit [y / n ]\n")
            if ok == 'y':
                print("\t\t\t\t\t ********Goodbye see you later******** \n")
                break
            elif ok == 'n':
                continue
            else:
                print("You did not press a correct character, please Retry.")
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
