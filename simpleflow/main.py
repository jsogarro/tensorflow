"""SimpleFlow

A naive implementation of TensforFlow
"""
import numpy as np


class Placeholder(object):
    """Represents and empty node for a value to be used to produce some output."""
    def __init__(self):
        self.output_nodes = []
        _default_graph.placeholders.append(self)


class Variable(object):
    """Represents a prefilled value to be used by the graph during computations"""
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.output_nodes = []
        _default_graph.variables.append(self)


class Graph(object):
    """Represents the SimpleFlow graph"""
    def __init__(self):
        self.operations = []
        self.placeholders = []
        self.variables = []

    def initialize_globals(self):
        global _default_graph
        _default_graph = self


class Operation():
    """Represents the operations that can be performed on our data"""
    def __init__(self, input_nodes=None):
        self.input_nodes = input_nodes or []
        self.output_nodes = []

        # add the operatiosn to the output nodes
        for node in input_nodes:
            node.output_nodes.append(self)

        _default_graph.operations.append(self)

    def compute(self):
        pass


class add(Operation):
    """Represents and addition operation"""
    def __init__(self, x, y):
        super().__init__([x,y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var + y_var


class multiply(Operation):
    """Represents a multiplication operation"""
    def __init__(self, x, y):
        super().__init__([x,y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var * y_var


class matmul(Operation):
    """Represents a matrix multiplication operation"""
    def __init__(self, x, y):
        super().__init__([x,y])

    def compute(self, x_var, y_var):
        self.inputs = [x_var, y_var]
        return x_var.dot(y_var)


class Session():
    """Represents a session object"""
    def run(self, operation, feed_dict={}):
        nodes = traverse(operation)
        for node in nodes:
            if type(node) == Placeholder:
                node.output = feed_dict[node]
            elif type(node) == Variable:
                node.output = node.value
            else:
                node.inputs = [input_node.output for input_node in node.input_nodes]
                node.output = node.compute(*node.inputs)
            if type(node.output) == list:
                node.output = np.array(node.output)
        return operation.output


def traverse(operation):
    """Perform a post order traversal of the nodes to ensure computations are done in the correct order."""
    nodes = []
    def recurse(node):
        if isinstance(node, Operation):
            for input_node in node.input_nodes:
                recurse(input_node)
        nodes.append(node)
    recurse(operation)
    return nodes
