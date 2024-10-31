# inputs
# refer picture in program folder

plate_length_x = 18 #inch
plate_length_y = 30 #inch
number_bolts_x = 3
number_bolts_y = 4
bolt_edge_offset = 1.5 #inch
bolt_shear_strength = 24 #ksi
bolt_tensile_strength = 45 #ksi
bolt_area = 0.3 #sq.inch

axial_tension = 10 #kip
moment_about_x = 5 #kip-ft
moment_about_y = 6 #kip-ft
shear_x = 2 #kip
shear_y = 2 #kip

# processing

moment_about_y *= 12 # convert to kip-inch
moment_about_x *= 12 # convert to kip-inch

phi = 0.75

number_bolts_total = number_bolts_x * 2 + number_bolts_y * 2 - 4

bolts_arm_x = plate_length_x - 2 * bolt_edge_offset
bolts_arm_y = plate_length_y - 2 * bolt_edge_offset

bolt_tension = axial_tension / number_bolts_total
bolt_tension += (moment_about_y / bolts_arm_x) /number_bolts_y
bolt_tension += (moment_about_x / bolts_arm_y) /number_bolts_x
bolt_tension = max(0,bolt_tension) # eliminate compression in bolt

shear_resultant = (shear_x ** 2 + shear_y ** 2) ** 0.5
bolt_shear = shear_resultant / number_bolts_total

dc_shear = bolt_shear / (phi * bolt_shear_strength * bolt_area)
dc_tension = bolt_tension / (phi * bolt_tensile_strength * bolt_area)

# outputs
print("Total number of bolts:",number_bolts_total)
print("\nMaximum tensile force in one bolt:",bolt_tension, "kip")
print("\nShear force in one bolt:", bolt_shear, "kip")
print("\nD/c ratio in shear:", dc_shear)
print("\nD/c ratio in tension:", dc_tension)
print("\nD/c ratio total:", dc_shear + dc_tension)

