# Standard library imports.
from dataclasses import dataclass

# Local imports.
from format_fns import keep_line
from format_fns import send_line


@dataclass
class Node:
    line: str

    def __post_init__(self):
        self.next: Node = None
        self.length: int = None

    def eval_node(self) -> None:
        if not self.next:
            return 
        
        if self.next and len(self.line) < self.length:
            self.next.length = self.length
            return 
        else:
            keep = keep_line(self.line, self.length)
            send = send_line(self.line, self.length)
            self.line = keep
            self.next.line = send + self.next.line
            self.next.length = self.length


class LinkedList:
    """
    A list of Nodes.  Each node comprises two values: 
    a string of text and a pointer to the next node.
    """
    def __init__(self, head: Node) -> None:
        """
        Instantiate a linked list with a head node.
        """
        self.head = head

    def eval_recursive(self, current_node: Node) -> None:
        """
        Evaluate nodes recursively.
        """
        
        # The method's base case.  Change not current_node.next to is
        # None.
        if (len(current_node.line) < current_node.length and 
                not current_node.next):
            
            return
        
        # The method's recursive cases.

        # Evaluate non-whitespace lines ending in newlines with next
        # values.
        if all([
                current_node.next,
                current_node.line != '\n',
                current_node.line[-1] == '\n']):

            new_node: Node = Node('\n')
            new_node.next = current_node.next
            current_node.line = current_node.line[:-1].rstrip()
            current_node.next = new_node
            current_node.eval_node()
            current_node = current_node.next
            self.eval_recursive(current_node)
        
        # Evaluate nodes with next values, including newline only
        # lines.
        elif current_node.next:
            current_node.eval_node()
            current_node = current_node.next
            self.eval_recursive(current_node)

        # Evalute nodes without a next value.
        else:
            current_node.next = Node("")
            current_node.eval_node()
            current_node = current_node.next
            self.eval_recursive(current_node)
        
    def merge_nodes(self) -> str:
        """
        Iterate through a linked list,  concatenating 
        all values and returning them as a string.
        """
        self.eval_recursive(current_node = self.head)
        current_node = self.head
        text = str()
        while current_node.next:
            if current_node.line == '\n':
                text += current_node.line
            else:
                text += current_node.line + '\n'

            current_node = current_node.next

        return text + current_node.line.rstrip()