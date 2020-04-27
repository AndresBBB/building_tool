import bpy
from bpy.props import PointerProperty

from .railing import Railing
from .railing_props import RailProperty


class BTOOLS_OT_add_railing(bpy.types.Operator):
    """Add railing to selected faces (+z facing)"""

    bl_idname = "btools.add_railing"
    bl_label = "Railing"
    bl_options = {"REGISTER", "UNDO"}

    props: PointerProperty(type=RailProperty)

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.mode == "EDIT_MESH"

    def execute(self, context):
        return Railing.build(context, self.props)

    def draw(self, context):
        self.props.draw(context, self.layout)
