import bmesh

from .fill_types import fill_panel, fill_glass_panes, fill_bar, fill_louver
from ...utils import get_edit_mesh, FaceMap, add_facemap_for_groups


class Fill:
    @classmethod
    def build(cls, fill_type, props):
        me = get_edit_mesh()
        bm = bmesh.from_edit_mesh(me)
        faces = [face for face in bm.faces if face.select]

        if cls.validate(faces):
            for f in faces:
                cls.execute_fill(bm, f, fill_type, props)
            return {"FINISHED"}
        return {"CANCELLED"}

    @classmethod
    def validate(cls, faces):
        if faces:
            if not any([round(f.normal.z, 1) for f in faces]):
                return True
        return False

    @classmethod
    def execute_fill(cls, bm, face, fill_type, props):
        prop, function = {
            "BAR" : (props[0], fill_bar),
            "PANELS" : (props[1], fill_panel),
            "GLASS_PANES" : (props[3], fill_glass_panes),
            "LOUVER" : (props[2], fill_louver),
        }.get(fill_type)
        # function(bm, face, prop)
