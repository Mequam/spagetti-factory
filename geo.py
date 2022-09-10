import bpy

#make a new geometry node group to edit
ng = bpy.data.node_groups.new("test group", "GeometryNodeTree")

#create input and output nodes for the group
input_node = ng.nodes.new("NodeGroupInput")
output_node = ng.nodes.new("NodeGroupOutput")


#create inputs that automatically get added to our input node
ng.inputs.new("NodeSocketFloat","x")
ng.input.new("NodeSocketGeometry","geo")

#create a new math node inside of the shader group
math_node = ng.nodes.new("ShaderNodeMath")

math_node.operation = "SINE" #DUmb sinE

#ng.outputs.new("NodeSocketVector",""

ng.link.new(input_node.output["geo"],math_node.input[0])