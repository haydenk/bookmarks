from os.path import dirname

module_dir: str = dirname(__file__)
project_dir: str = dirname(module_dir)
data_dir: str = f"{project_dir}/data"
