import bpy

from bpy.props import BoolProperty, FloatVectorProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_operator import ScEditOperatorNode
from ...helper import get_override

class ScExtrudeEdges(Node, ScEditOperatorNode):
    bl_idname = "ScExtrudeEdges"
    bl_label = "Extrude Edges (Individually)"
    
    in_value: FloatVectorProperty(update=ScNode.update_value)
    in_use_normal_flip: BoolProperty(update=ScNode.update_value)
    in_mirror: BoolProperty(update=ScNode.update_value)
    
    def init(self, context):
        super().init(context)
        self.inputs.new("ScNodeSocketVector", "Value").init("in_value", True)
        self.inputs.new("ScNodeSocketBool", "Flip Normals").init("in_use_normal_flip")
        self.inputs.new("ScNodeSocketBool", "Mirror Editing").init("in_mirror")
    
    def functionality(self):
        bpy.ops.mesh.extrude_edges_move(
            get_override(self.inputs["Object"].default_value, True),
            MESH_OT_extrude_edges_indiv = {
                "use_normal_flip": self.inputs["Flip Normals"].default_value,
                "mirror": self.inputs["Mirror Editing"].default_value
            },
            TRANSFORM_OT_translate = {
                "value": self.inputs["Value"].default_value
            }
        )