bl_info = {
    "name": "Sure UV Map",
    "author": "Alexander Milovsky (milovsky.ru),Edit by RedHalo Studio(发霉的红地蛋)",
    "version": (0, 7, 0),
    "blender": (2, 80, 0),
    "location": "View 3D > UI tab (Press `N` to see panel), Mapping parameters in Tool Properties (bottom left corner)",
    "description": "Box / Best Planar UV Map (Make Material With Raster Texture First!)",
    "warning": "",
    "category": "UV"
}

import bpy
from . sure_uv_panel import OBJECT_PT_SureUVPanel
from . sure_uv_operator import OBJECT_OT_SureUVOperator
from . sure_uv_settings import SureUVSettings, RedHaloUVSettings

classes = (
    OBJECT_PT_SureUVPanel,
    OBJECT_OT_SureUVOperator,
    RedHaloUVSettings,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Object.redhalo_uv_settings = bpy.props.PointerProperty(type = RedHaloUVSettings)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Object.redhalo_uv_settings

