import os
import sys

# Define some needed locations
scripts_path = os.path.abspath(os.path.dirname(__file__))
root_path, _ = os.path.split(scripts_path)

superbuild_path = os.path.join(root_path, 'SuperBuild')
ccd_widths_path = os.path.join(root_path, 'ccd_defs.json')

# add opencv to python path
pyopencv_path = os.path.join(superbuild_path, 'install/lib/python2.7/dist-packages')
sys.path.append(pyopencv_path)

# add opensfm to python path
opensfm_path = os.path.join(superbuild_path, "src/opensfm")

# Define supported image extensions
supported_extensions = {'.jpg','.jpeg'}