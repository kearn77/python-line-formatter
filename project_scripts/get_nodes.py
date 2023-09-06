# Local imports.
import linked_list as ll

# Create a list of tuples that signifies whether any given line - n -
# has a line that follows it - n + 1.
def model_lines(src: list[str]) -> list[tuple]:
    index_list = []
    for index, _ in enumerate(src):
        if index + 1 < len(src):
            index_list.append((index, index+1))
        else:
            index_list.append((index, None))
    
    return index_list

# Use the return value of model_lines to instantiate text file nodes.
def create_nodes(index_list: list[tuple], src: list[str]) -> dict:
    node_dict: dict = {}
    for a,b in index_list:
        if a not in node_dict.keys():
            next_node: ll.Node = ll.Node(src[b])
            current_node: ll.Node = ll.Node(src[a])
            current_node.next = next_node
            node_dict[a] = node_dict.get(a, current_node)
            node_dict[b] = node_dict.get(b, next_node)

        elif a in node_dict.keys() and b:
            next_node: ll.Node = ll.Node(src[b])
            current_node: ll.Node = node_dict[a]
            current_node.next = next_node
            node_dict[b] = node_dict.get(b, next_node)

    return node_dict