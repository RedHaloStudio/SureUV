import bpy
from bpy.types import Operator


class OBJECT_PT_SureUVPanel(bpy.types.Panel):
    bl_label = "Sure UV Mapping v.0.7"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Sure UV Addon"
    bl_category = "Sure UV Map"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj and obj.type == 'MESH')

    def draw(self, context):
        # wm = context.window_manager
        scene = context.scene
        obj = context.object
        # settings = scene.sure_uv_settings
        settings = obj.redhalo_uv_settings
        opname = 'object.sure_uv_operator'
        layout = self.layout

        aspect = settings.texaspect if settings.texaspect != 0.0 else 1.0

        layout.label(text="UV Mapping:")
        
        op = layout.operator(opname, text="UV Box Map")
        op.action='box'
        # if settings.autotexaspect:
        #     op.texaspect = aspect

        op = layout.operator(opname, text="Best Planar Map")
        op.action='bestplanar'
        # if settings.autotexaspect:
        #     op.texaspect = aspect

        # layout.label(text="1. Make Material With Raster Texture")
        # layout.label(text="2. Select Texture to determine TexAspect")        
        # layout.label(text="3. Use Box mapping on whole object")
        # layout.label(text="4. Use Best Planar on selected faces")

        # layout.prop(settings,"autotexaspect")

        # layout = self.layout
        # layout.label(text="Size")
        # row = layout.row()
        # row.prop(obj.redhalo_uv_settings,'size', text="")
        # row.prop(self,'reset_size', icon="LOOP_BACK", text="")

        # row = layout.row()
        # row.label(text="XYZ rotation")
        # row.prop(self,'reset_xyz_rot',text="", icon="LOOP_BACK")
        # layout.prop(obj.redhalo_uv_settings,'rot', text="")

        # row = layout.row()
        # row.label(text="XYZ offset")
        # row.prop(self,'reset_xyz_offset',text="", icon="LOOP_BACK")

        # layout.prop(obj.redhalo_uv_settings,'offset', text="")
        # layout.label(text="Texture Aspect")
        # layout.prop(obj.redhalo_uv_settings,'texaspect', text="")
        # row = layout.row()
        # row.prop(self,'reset_texaspect')
        # row.prop(obj.redhalo_uv_settings,'guess_texaspect')
