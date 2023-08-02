# Line Formatter:  A CLI Application for Plain Text Files<br/>

line_formatter.py is a command line application with a simple  purpose:<br/>
enforce user-defined line breaks in a plain text file.  Not only do<br/>
line breaks make plain text files more readable, they also allow plain<br/>
text  to serve as an intermediary to other file formats, such as<br/>
markdown and markup.  This application facilitates that process.<br/>

In addition to its core line break functionality, line_formatter.py<br/>
provides some markdown specific features, like the ability to end lines<br/>
with break-tags and designate whether a line is a header.  This has<br/>
expedited my ability to write clean, concise markdown.  I’m sure<br/>
plenty of alternatives exist.  On the off chance that I am mistaken,<br/>
however, my modest application is made available here.<br/>

Broadly speaking, the application slices a text file’s lines into<br/>
keep and send components.  These components are used to create nodes in<br/>
a linked list.  Once all of the nodes have been linked, the node’s<br/>
contents are merged into a string, which is returned to the user.<br/>

## Table of Contents<br/>

format_fns.py<br/>

This module contains four functions: get_attrs, split_at, keep_line,<br/>
and send_line.  Collectively, they are used to create the nodes that<br/>
compose a linked list.  The eval_node method - a member function of the<br/>
Node class - calls this group of functions to format a node’s line<br/>
value.<br/>

linked_list.py<br/>

A linked list is a memory efficient data structure that is well suited<br/>
for insert and delete operations. It is composed of nodes, objects that<br/>
contain some data and a pointer to another node.  This pointer allows<br/>
the list to be stored non-sequentially in memory.  Moreover, in the<br/>
event that a value must be inserted or deleted, no shifting takes<br/>
place.  Rather, the pointers for the affected nodes are amended to<br/>
reflect the updated structure.  The linked list is instantiated with a<br/>
node designated as the head, which serves as the entry point to the<br/>
other nodes in the list.<br/>

The linked_list module implements this data structure.  The Node class<br/>
has three attributes: line, length, and next.  Line is a string taken<br/>
from the input file.  This attribute is accessed by the eval_node<br/>
method, which calls keep_line and send_line to create keep and send<br/>
components.  Line is set equal to the keep component, while the send<br/>
component is pushed to the next node and concatenated with that<br/>
node’s line value.  Length is the user provided number of characters<br/>
in a line.  Note that, in the event that the user does not provide a<br/>
line length, it defaults to eighty.  Effectively, all nodes inherit the<br/>
head node’s length value.<br/>

The LinkedList class has two methods: eval_recursive and merge_nodes.<br/>
Taking a linked list as an argument, the former uses recursion to<br/>
create new nodes to accommodate the changing structure of the input.<br/>
The latter merges the list’s line values into a single string.<br/>

get_nodes.py<br/>

The get_nodes module contains two functions that create the initial<br/>
linked list passed to eval_recursive.   Model lines, a helper function,<br/>
returns a list of two-tuples that index whether any given line is<br/>
followed by a non-empty line.  create_nodes takes this list as an<br/>
argument and returns a dictionary of node values, where the head node<br/>
is accessed by the key 0.<br/>

parse_args.py<br/>

Utilizing python’s argparse library, parse_args.py instantiates an<br/>
ArgumentParser object named ‘parser,’  which creates the command<br/>
line interface the user interacts with to run the program.<br/>

exceptions.py<br/>

Raises an error if the file passed to the command line interface does<br/>
not end in ‘.txt’.<br/>

line_formatter.py<br/>

This module serves as the entry point to the command line application.<br/>
It contains four functions - add_breaks, add_headers, preview, and<br/>
create_file - that are responsible for modifying the output returned by<br/>
the merge_nodes method.<br/>