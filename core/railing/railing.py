import bmesh

from .railing_types import create_railing
from ...utils import get_edit_mesh


class Railing:
    @classmethod
    def build(cls, context, props):
        me = get_edit_mesh()
        bm = bmesh.from_edit_mesh(me)
        faces = [face for face in bm.faces if face.select]

        if cls.validate(faces):

            bmesh.update_edit_mesh(me, True)
            return {"FINISHED"}
        return {"CANCELLED"}

    @classmethod
    def validate(cls, faces):
        if faces:
            if all([round(f.normal.z, 1) for f in faces]):
                return True
        return False
