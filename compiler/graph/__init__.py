import os
from pathlib import Path

compiler_base_dir = Path(__file__).parent
graph_base_dir = os.path.join(compiler_base_dir, "graph")
ir_base_dir = os.path.join(compiler_base_dir, "ir")
