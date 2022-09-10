import bpy
import pydice

def parse_exp(exp,name=None):
    p = ParseNodeGroup(exp,name)
    return p.parse()

class ParseNodeGroup():    
    def __init__(self,exp,name=None):
        if name == None:
            name = exp
        
        self.group = bpy.data.node_groups.new(name , "GeometryNodeTree")
        self.name = name
        self.expr = exp

        self.input_node = self.group.nodes.new("NodeGroupInput")
        self.output_node = self.group.nodes.new("NodeGroupOutput")

        #create all of the math node modifires    
        self.add = self.create_math_node("ADD") #create a math node :D
        self.sub = self.create_math_node("SUBTRACT") #create a math node :D
        self.mult = self.create_math_node("MULTIPLY") #create a math node :D
        self.div = self.create_math_node("DIVIDE") #create a math node :D

    def parse(self):
        pydice.parse(self.expr,
        [('+',self.add),('-',self.sub),('*',self.mult),('/',self.div)],
        self.parse_var,
        [self])
    
    @staticmethod
    def parse_var(args,name):
        self = args[0]
        
        if name in self.input_node.outputs: 
            return self.input_node.outputs[name]
        
        self.group.inputs.new("NodeSocketFloat",name)
        return self.input_node.outputs[name]

    @staticmethod
    def create_math_node(opp="ADD"):
        @staticmethod
        def f(args,socket_input_a,socket_input_b):
            self = args[0]
            
            math_node = self.group.nodes.new("ShaderNodeMath")
            math_node.operation = opp
            
            self.group.links.new(socket_input_a,math_node.inputs[0])
            self.group.links.new(socket_input_b,math_node.inputs[1])

            return math_node.outputs[0]
        return f