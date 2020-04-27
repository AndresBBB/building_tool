import bpy

from .railing_ops import BTOOLS_OT_add_railing
from .railing_props import PostFillProperty, RailFillProperty, WallFillProperty, RailProperty

classes = (
    PostFillProperty,
    RailFillProperty,
    WallFillProperty,
    RailProperty,
    BTOOLS_OT_add_railing,
)


def register_railing():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister_railing():
    for cls in classes:
        bpy.utils.unregister_class(cls)
