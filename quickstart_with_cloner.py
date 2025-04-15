# CREATE a scene with 4 cubes
from isaacsim.core.cloner import Cloner    # import Cloner interface
from isaacsim.core.utils.stage import get_current_stage
from pxr import UsdGeom

# create our base environment with one cube
base_env_path = "/World/Cube_0"
UsdGeom.Cube.Define(get_current_stage(), base_env_path)

# create a Cloner instance
cloner = Cloner()

# generate 4 paths that begin with "/World/Cube" - path will be appended with _{index}
target_paths = cloner.generate_paths("/World/Cube", 4)

# clone the cube at target paths
cloner.clone(source_prim_path="/World/Cube_0", prim_paths=target_paths) #same positiona
cloner.clone(source_prim_path="/World/Cube_0", prim_paths=target_paths, positions = cube_positions) #different positions

# ACCESSING Cloned Objects
# import the XFormPrimView interface from isaacsim.core.api for APIs for XForm prims
from isaacsim.core.prims import XFormPrimView

# retrieve a View containing all 4 boxes by using a wildcard expression that matches the prim paths for all boxes
boxes = XFormPrimView("/World/Cube_*")

# retrieve the global transforms of all boxes
#   - positions will be a vector of shape (4, 3) for X, Y, Z axes of translation
#   - orientations will be a vector of shape (4, 4) for W, X, Y, Z axes of quaternion
positions, orientations = boxes.get_world_poses()

# increase positions on the Z axis to move boxes up by 1.5 units
positions[:, 2] += 1.5
# apply the new positions
boxes.set_world_poses(positions, orientations)

# ADDITIONAL PARAMETERS
cloner.clone(
    source_prim_path="/World/Ants/Ant_0",
    prim_paths=target_paths,
    position_offsets=position_offsets,
    replicate_physics=True,
    base_env_path="/World/Ants",
    root_path="/World/Ants/Ant_",
    copy_from_source=True
)