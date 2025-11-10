import bpy

# Delete default cube if it exists
if "Cube" in bpy.data.objects:
    bpy.data.objects["Cube"].select_set(True)
    bpy.ops.object.delete()

# Add a UV Sphere
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 1))
sphere = bpy.context.active_object
bpy.ops.object.shade_smooth()

# Add a ground plane
bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))

# Add Sunlight
bpy.ops.object.light_add(type='SUN', location=(5, -5, 5))
sun = bpy.context.active_object
sun.rotation_euler = (0.8, 0.5, 0.2)  # tilt the sun
sun.data.energy = 5  # brightness
sun.data.angle = 0.5  # softness of shadows

# Add Camera
bpy.ops.object.camera_add(location=(6, -6, 4), rotation=(1.1, 0, 0.8))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

# Set renderer to Cycles for realism
bpy.context.scene.render.engine = 'CYCLES'
