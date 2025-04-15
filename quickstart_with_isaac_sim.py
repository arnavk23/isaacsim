# Add a Ground Plane
from isaacsim.core.api.objects.ground_plane import GroundPlane
GroundPlane(prim_path="/World/GroundPlane", z_position=0)

# Add a Light Source 
from pxr import Sdf, UsdLux
stage = omni.usd.get_context().get_stage()
distantLight = UsdLux.DistantLight.Define(stage, Sdf.Path("/DistantLight"))
distantLight.CreateIntensityAttr(300)

# Add a Visual Cube
import numpy as np
from isaacsim.core.api.objects import VisualCuboid
VisualCuboid(
   prim_path="/visual_cube",
   name="visual_cube",
   position=np.array([0, 0.5, 0.5]),
   size=0.3,
   color=np.array([255, 255, 0]),
)

# Add Physics and Collision Properties
from isaacsim.core.prims import RigidPrim
RigidPrim("/visual_cube")

# Add only Collision Properties
from isaacsim.core.prims import GeometryPrim
prim = GeometryPrim("/visual_cube")
prim.apply_collision_apis()

# Move, Rotate and Scale the Cube
import numpy as np
from isaacsim.core.prims.xform_prim import XformPrim
from isaacsim.core.prims.prim import Prim

translate_offset = np.array([[1.5,-0.2,1.0]])
rotate_offset = np.array([[90,-90,180]])
scale = np.array([[1,1.5,0.2]])

cube_in_coreapi = XformPrim(Prim(prim_paths_expr="/test_cube"))
cube_in_coreapi.set_world_poses(translate_offset, rotate_offset)
cube_in_coreapi.set_scales(scale)

