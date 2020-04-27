import bpy
from bpy.props import PointerProperty, EnumProperty

from .fill import Fill
from .fill_props import FillBars, FillPanel, FillLouver, FillGlassPanes


class BTOOLS_OT_add_fill(bpy.types.Operator):
    """Add various fill types to selected faces (bars, panels, etc.)"""

    bl_idname = "btools.add_fill"
    bl_label = "Fill"
    bl_options = {"REGISTER", "UNDO"}

    fill_items = [
        ("BAR", "Bar", "", 0),
        ("PANELS", "Panels", "", 1),
        ("GLASS_PANES", "Glass_Panes", "", 2),
        ("LOUVER", "Louver", "", 3),
    ]

    fill_type: EnumProperty(
        name="Fill Type",
        items=fill_items,
        default="BAR",
        description="Type of fill",
    )

    user_items = [
        ("GENERIC", "Generic", "", 0),
        ("DOOR", "Door", "", 1),
        ("WINDOW", "Window", "", 2)
    ]

    user_type: EnumProperty(
        name="User Type",
        items=user_items,
        default="DOOR",
        description="Type of element the fill is created on"
    )

    bar_fill: PointerProperty(type=FillBars)
    panel_fill: PointerProperty(type=FillPanel)
    louver_fill: PointerProperty(type=FillLouver)
    glass_fill: PointerProperty(type=FillGlassPanes)

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.mode == "EDIT_MESH"

    def execute(self, context):
        return Fill.build(self.fill_type, [self.bar_fill, self.panel_fill, self.louver_fill, self.glass_fill])

    def draw(self, context):
        self.layout.row().prop(self, "user_type", expand=True)
        row = self.layout.row()
        row.prop_menu_enum(self, "fill_type", text=self.fill_type.title().replace('_', ' '))

        {
            "BAR" : self.bar_fill,
            "PANELS" : self.panel_fill,
            "GLASS_PANES" : self.glass_fill,
            "LOUVER" : self.louver_fill
        }.get(self.fill_type).draw(self.layout)
