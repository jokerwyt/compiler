import os
from pathlib import Path

root_base_dir = Path(__file__).parent.parent
compiler_base_dir = os.path.join(root_base_dir, "compiler")
graph_base_dir = os.path.join(compiler_base_dir, "graph")

property_base_dir = os.path.join(root_base_dir, "examples/property")
