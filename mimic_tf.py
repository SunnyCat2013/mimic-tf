class Graph():
    def __init__(self):
        self.Placerholder = []
        self.Variable = []
        self.Operator = []
        self.Constant = []

    def as_default(self):
        global _default_graph
        _default_graph = self

'''
what's the point of default graph?
Since there is no use of _default_graph?
'''
Graph().as_default()


class Placeholder():
    def __init__(self, value):
        _default_graph.Placeholder.append(self)
        self.output = value


class constant():
    def __init__(self, value):
        _default_graph.Constant.append(self)
        self.inputs = value
        self.output = value
    def forward(self):
        return self.output


class Operator():
    def __init__(self, inputs):
        _default_graph.Operator.append(self)
        self.inputs = inputs # set inputs to get input operatoers' outputs
        self.output = None



class BiOperator(Operator):
    def __init__(self, input1, input2):
        super(BiOperator, self).__init__([input1, input2])
        #Operator.__init__([input1, input2])

class multiply(BiOperator):
    
    def forward(self):
        self.output = self.inputs[0].output * self.inputs[1].output
    
class add(BiOperator):
    
    def forward(self):
        self.output = self.inputs[0].output + self.inputs[1].output
 
class div(BiOperator):
    
    def forward(self):
        self.output = self.inputs[0].output / self.inputs[1].output
 
def top_sort(last_node):
    if last_node.inputs is None:
        return []
    res = []
    for node in last_node.inputs:
        res += top_sort(node)
    res += [last_node]

    return res

def print_node(nodes):
    for node in nodes:
        print('node:', type(node))

class Session():
    def __init__(self):
        print('init session')

    def run(self, target):
        self.target = target

        self.top_sort_nodes = []
        t_set = set()
        def top_sort(nodes):
            if not nodes:
                return
            new_nodes = []
            for node in nodes:
                if node not in t_set:
                    t_set.add(node)
                    self.top_sort_nodes.insert(0, node)
                    if not isinstance(node, constant):
                        new_nodes += node.inputs
            top_sort(new_nodes)

                    
        top_sort([target])
        print_node(self.top_sort_nodes)
        
        for node in self.top_sort_nodes:
            if isinstance(node, constant):
                continue
            node.forward()
            print('node.forward():', type(node), node.output)


        return self.target.output
    def __enter__(self):
        print('enter session')
        return self
    def __exit__(self, ty, value, trace):

        print('exit session', ty, value, trace)
        return self.target.output
                    
        
        
