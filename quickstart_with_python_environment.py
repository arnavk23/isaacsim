import carb
import omni.kit.app

framework = carb.get_framework()
framework.load_plugins(
    loaded_file_wildcards=["omni.kit.app.plugin"],
    search_paths=[os.path.abspath(f'{os.environ["CARB_APP_PATH"]}/kernel/plugins')],
)

# Inject a experience config
sys.argv.insert(1, f'{os.environ["EXP_PATH"]}/isaacsim.exp.base.python.kit')

# Add paths to extensions
sys.argv.append(f"--ext-folder")
sys.argv.append(f'{os.path.abspath(os.environ["ISAAC_PATH"])}/exts')

# Run headless
sys.argv.append("--no-window")

app = omni.kit.app.get_app()
app.startup("Isaac-Sim", os.environ["CARB_APP_PATH"], sys.argv)

app.shutdown()
framework.unload_all_plugins()

