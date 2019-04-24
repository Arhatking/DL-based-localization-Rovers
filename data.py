
"""
Program to separate POL and VRT projections. 

To download ALL the projections data: 
	Spirit: wget -r -nH --cut-dirs=2 --no-parent --reject="index.html*" robots=off  https://pds-imaging.jpl.nasa.gov/data/mer/spirit/mer2om_0xxx/browse/navcam/
	Opportunity: wget -r -nH --cut-dirs=2 --no-parent --reject="index.html*" robots=off  https://pds-imaging.jpl.nasa.gov/data/mer/opportunity/mer1om_0xxx/browse/navcam/

"""

import os
import subprocess 

def pol_vrt_separated(src, dst_pol, dst_vrt):
	pol, vrt = 0, 0
	for path, subdir, files in os.walk(src):
		for file in files:
			if file[11:14] == "pol":
				subprocess.call(['cp', os.path.join(path, file), dst_pol])
				pol += 1
			elif file[11:14] == "vrt":
				subprocess.call(['cp', os.path.join(path, file), dst_vrt])	
				vrt += 1
	return pol, vrt



directory1 = './../Desktop/Rover/opportunity/mer1om_0xxx/browse/navcam/'
directory2 = './../Desktop/Rover/spirit/mer2om_0xxx/browse/navcam/'

dst_pol = './../Desktop/Rover/ground-pol/'
dst_vrt = './../Desktop/Rover/ground-vrt/'

pol_o, vrt_o = pol_vrt_separated(directory1, dst_pol, dst_vrt)
pol_s, vrt_s = pol_vrt_separated(directory2, dst_pol, dst_vrt)

print("There are ", pol_o, " POL and ", vrt_o, " VRT projections for Opportunity") # 1151, 1316
print("There are ", pol_s, " POL and ", vrt_s, " VRT porjections for Spirit") #383, 429
print("Total: ", pol_s+pol_o, " POL", vrt_o+vrt_s, " VRT") # 1534, 1745




