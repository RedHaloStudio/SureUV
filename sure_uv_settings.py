import bpy
from bpy.props import (
    BoolProperty,
    BoolVectorProperty,
    FloatProperty,
    FloatVectorProperty,
    StringProperty,
)


def update_func(self, context):
    img = self['teximage']
    if img:
        self.texaspect = img.size[0] / img.size[1] if img.size[0] / img.size[1] else 1.0


class SureUVSettings(bpy.types.PropertyGroup):   
    teximage: bpy.props.PointerProperty(
        name="Image", 
        type=bpy.types.Image,
        update=update_func
    )
    autotexaspect: BoolProperty(name="Auto Aspect", default=True)
    texaspect: FloatProperty(name="Texture Aspect", default=1.0, precision=4)

def update_f(self, context):
    ...


class RedHaloUVSettings(bpy.types.PropertyGroup):
    size: FloatProperty(name="Size", default=1.0, precision=4)
    rot: FloatVectorProperty(name="XYZ Rotation")
    offset: FloatVectorProperty(name="XYZ offset", precision=4)

    zrot: FloatProperty(name="Z rotation", default=0.0)
    xoffset: FloatProperty(name="X offset", default=0.0, precision=4)
    yoffset: FloatProperty(name="Y offset", default=0.0, precision=4)
    
    texaspect: FloatProperty(name="Texture aspect", default=1.0, precision=4)
