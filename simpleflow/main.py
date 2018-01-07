"""SimpleFlow

A naive implementation of TensforFlow
"""

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
        _default.graph.variables.append(self)


class Graph(object):
    """Represents the SimpleFlow graph"""
    def __init__(self):
        self.operations = []
        self.placeholders = []
