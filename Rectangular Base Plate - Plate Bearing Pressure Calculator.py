# inputs
# refer picture in program folder

plate_length_x = 10 #inch
plate_length_y = 12 #inch

axial_compression = 85 #kip
moment_about_x = 25 #kip-ft
moment_about_y = 15 #kip-ft

# processing

moment_about_y *= 12 # convert to kip-inch
moment_about_x *= 12 # convert to kip-inch

plate_area = plate_length_x * plate_length_y
plate_inertia_about_x = (plate_length_x * (plate_length_y ** 3)) /12
plate_inertia_about_y = (plate_length_y * (plate_length_x ** 3)) /12

pa = axial_compression / plate_area
pmx = moment_about_x * (plate_length_y/2) / plate_inertia_about_x
pmy = moment_about_y * (plate_length_x/2) / plate_inertia_about_y

p1 = pa -pmx +pmy
p2 = pa -pmx -pmy
p3 = pa +pmx -pmy
p4 = pa +pmx +pmy
pressure = max(p1, p2, p3, p4)

# outputs
print("Bearing pressure at Point 1 (top-right):", max(p1, 0), "ksi")
print("Bearing pressure at Point 2 (top-left):", max(p2, 0), "ksi")
print("Bearing pressure at Point 3 (bottom-left):", max(p3, 0), "ksi")
print("Bearing pressure at Point 4 (bottom-right):", max(p4, 0), "ksi")
print("\nMaximum bearing pressure:", pressure, "ksi")

