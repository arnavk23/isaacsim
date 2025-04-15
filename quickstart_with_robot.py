# Starting the Simulator
from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False})  # start the simulation app, with GUI open

# Using a World object
my_world = World(stage_units_in_meters=1.0)

# Stopping the Simulation explicitly
 # At the bottom of the script, there is a loop, and a stepping function my_world.step() is called every iteration. Inside this stepping function, it move forward a fixed number of rendering and physics calculation.
 # The script will run for 4 cycles, and at each cycle, the arm and the car will move or stop moving. The car’s joint positions will be printed at every physics step in the last cycle.
    for i in range(4):
        print("running cycle: ", i)
        if i == 1 or i == 3:
            print("moving")
            # move the arm
            arm.set_joint_positions([[-1.5, 0.0, 0.0, -1.5, 0.0, 1.5, 0.5, 0.04, 0.04]])
            # move the car
            car.set_joint_velocities([[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]])
        if i == 2:
            print("stopping")
            # reset the arm
            arm.set_joint_positions([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
            # stop the car
            car.set_joint_velocities([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])

        for j in range(100):
            # step the simulation, both rendering and physics
            my_world.step(render=True)
            # print the joint positions of the car at every physics step
            if i == 3:
                car_joint_positions = car.get_joint_positions()
                print("car joint positions:", car_joint_positions)

# Running the Actuator Network
current_joint_pos = self.get_joint_positions()
current_joint_vel = self.get_joint_velocities()

joint_torques, _ = self._actuator_network.compute_torques(
    current_joint_pos, current_joint_vel, self._action_scale * self.action
)

self.set_joint_efforts(joint_torques)

# Robot Joint Order
# Open your USD and PLAY the simulation before running this snippet
prim = Articulation(prim_path=<your_robot_prim_path>)
prim.initialize()
print(str(prim.dof_names))

# Robot Joint Properties
# Open your USD and PLAY the simulation before running this snippet
prim = Articulation(prim_path=<your_robot_prim_path>)
prim.initialize()
print(str(prim.dof_properties))

