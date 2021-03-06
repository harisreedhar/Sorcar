import bpy

from bpy.props import StringProperty
from bpy.types import Node
from .._base.node_base import ScNode

class ScString(Node, ScNode):
    bl_idname = "ScString"
    bl_label = "String"

    prop_string: StringProperty(name="String", update=ScNode.update_value)

    def init(self, context):
        super().init(context)
        self.outputs.new("ScNodeSocketString", "Value")
    
    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.prop(self, "prop_string")
    
    def post_execute(self):
        return {"Value": self.prop_string}