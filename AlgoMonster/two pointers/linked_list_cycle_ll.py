def next_node(nodes):
    return nodes.next or nodes


def cycle_size(nodes):
    # WRITE YOUR BRILLIANT CODE HERE
    tortoise = next_node(nodes)
    hare = next_node(next_node(nodes))

    while tortoise != hare and hare.next is not None:
        tortoise = next_node(tortoise)
        hare = next_node(next_node(hare))

    if hare.next is None:
        return -1

    count = 1
    # Start again from the beginning of the cycle
    tortoise = next_node(tortoise)
    hare = next_node(next_node(hare))

    while tortoise != hare:
        count += 1
        tortoise = next_node(tortoise)
        hare = next_node(next_node(hare))
    return count
