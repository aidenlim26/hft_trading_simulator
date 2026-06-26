# Single Linked List is an additional linear data structure that works a little bit different than an array 
# Different implementation and faster time complexity

# Arrays have contingous memory blocks while Linked Lists use non-contingous memory dynamically allocated via Pointers

# EXAMPLE
# [7] -> [4] -> [3] -> [2]

# Each [] is a "Node"
# Inside each box is a "Value"
# The "Next" property / "Pointer" will store the next location to the node that comes next in the list
# The "->" are the "Pointers"
# Right here, [7] is the "Head". It allows us to access all of the different values
# [2] is currently the "Tail"


# EXAMPLE PSUEDOCODE PRINTING LAST VALUE OF SINGLE LINKED LIST
# current = head
# while current.next != null:           # because the last node's pointer is a null value, nothing after the last node
#   current = current.next              # this grabs the "current.next" of the second last value    
# print current.value                   # which stores the last value [2]


# EXAMPLE PSUEDOCODE REMOVING A NODE IN THE MIDDLE OF THE LINKED LIST
# nextnode = node.next
# prev.next = nextnode      # O(n)