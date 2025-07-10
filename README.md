## Isaac Sim Quickstart 

Welcome to the **Isaac Sim Quickstart** repository — your go-to starting point for exploring [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim), a robotics simulation platform built on the powerful Omniverse framework.

This repo provides an easy and modular way to get started with robot simulation, environment setup, scripting, and control logic in Isaac Sim. Whether you’re a beginner looking to learn, a researcher prototyping algorithms, or a developer integrating with real hardware, this repo is designed for **rapid iteration and experimentation**.

### Features

-  Minimal boilerplate Isaac Sim setup
-  Load and simulate popular robots (e.g., Unitree Go1, Franka, UR10)
-  Modular standalone scripts for:
  - Scene loading
  - Robot articulation and control
  - Basic sensor integration
-  Isaac Sim standalone scripting mode
-  Keyboard/CLI control templates
-  Extendable for reinforcement learning or perception tasks

###  Prerequisites

> Make sure your system meets Isaac Sim’s requirements.

- Ubuntu 20.04 or Windows 10 (Linux strongly recommended)
- Dedicated GPU with NVIDIA RTX (Ampere or newer)
- Driver ≥ 525+, CUDA ≥ 11.7
- Python ≥ 3.7 (Conda or venv preferred)
- [Isaac Sim installed](https://docs.omniverse.nvidia.com/isaacsim/latest/installation/install-launch.html) and running

###  Installation
Clone the Repository

```bash
git clone https://github.com/your-username/isaacsim-quickstart.git
cd isaacsim-quickstart
