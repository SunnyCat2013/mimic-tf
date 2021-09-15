class Graph():
    def __init__(self):
        self.Placerholder = []
        self.Variable = []
        self.Operator = []
        self.Constant = []

    def as_default(self):
        global _default_graph
        _default_graph = self

Graph().as_default()


class Placeholder():
    def __init__(self, value):
        _default_graph.Placeholder.append(self)
        self.output = value


class constant():
    def __init__(self, value):
        _default_graph.Constant.append(self)
        self.output = value


class Operator():
    def __init__(self, **inputs):
        _default_graph.Operator.append(self)
        self.inputs = inputs # set inputs to get input operatoers' outputs
        self.output = None



class BiOperator(Operator):
    def __init__(self, input1, input2):
        super.__init__([input1, input2])

class multiply(BiOperator):
    def __init__(self, input1, input2):
        self.input1 = input1.output
        self.input2 = input2.output
    
    def forward(self):
        self.output = self.input1 * self.input2
    
class add(BiOperator):
    def __init__(self, input1, input2):
        self.input1 = input1.output
        self.input2 = input2.output
    
    def forward(self):
        self.output = self.input1 + self.input2
 
class div(BiOperator):
    def __init__(self, input1, input2):
        self.input1 = input1.output
        self.input2 = input2.output
    
    def forward(self):
        self.output = self.input1 / self.input2
 
def top_sort(last_node):
    if last_node.inputs is None:
        return []
    res = []
    for node in last_node.inputs:
        res += top_sort(node)
    res += [last_node]

    return res

class Session():
    def __init__(self, target)
        self.target = target

        self.top_sort_nodes = []
        t_set = set()
        def top_sort(last_node):
            for node in last_node.inputs:
                if node not in t_set:
                    self.top_sort_nodes.insert(node, 0)
                    t_set.add(node)
                    top_sort(node)
        top_sort(target)

    def run(self):
        for node in self.top_sort_nodes:
            if isinstance(node, 'constant'):
                continue
            for inode in node.inputs:
                inode.forward()

        return self.target.output
                    
        
        
