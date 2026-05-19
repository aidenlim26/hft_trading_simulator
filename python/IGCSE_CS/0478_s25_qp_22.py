def calculate_cuboid():
    valid = False
    while valid == False:
        cuboid_base = float(input("Enter the base length of the cuboid: "))
        cuboid_depth = float(input("Enter the depth length of the cuboid: "))
        cuboid_height = float(input("Enter the height length of the cuboid: "))
    
        if cuboid_base < 0 or cuboid_depth < 0 or cuboid_height < 0:
            print("All inputs must be greater than 0.0 ")
        else:
            cuboid_volume = cuboid_base * cuboid_depth * cuboid_height
            print("The volume of the cuboid is: ", cuboid_volume)
            valid = True
        
def calculate_triangular_prism():
    valid = False
    while valid == False:
        prism_base = float(input("Enter the base length of the prism: "))
        prism_depth = float(input("Enter the depth length of the prism: "))
        prism_height = float(input("Enter the height length of the prism: "))
    
        if prism_base < 0 or prism_depth < 0 or prism_height < 0:
            print("All inputs must be greater than 0.0 ")
        else:
            prism_volume = 0.5 * prism_base * prism_depth * prism_height
            print("The volume of the triangular prism is: ", prism_volume)
            valid = True

def calculate_sphere():
    valid = False
    while valid == False:
        sphere_radius = float(input("Enter the radius for the sphere: "))

        if sphere_radius < 0:
            print("All inputs must be greater than 0.0 ")
        else:
            sphere_volume = (4/3) * 3.142 * sphere_radius * sphere_radius * sphere_radius
            print("The volume of the sphere is: ", sphere_volume)
            valid = True

print("This program calculates the volume of shapes")

continueprogram = False

while continueprogram == False:
    input_shape = int(input("Enter 1 to calculate volume of a cuboid, 2 to calculate volume of a triangular prism, 3 to calculate volume of a sphere, 4 to stop the program: "))
    if input_shape < 1 or input_shape > 4:
        print("Inputs must be between 1 and 4.")
    elif input_shape == 1:
        calculate_cuboid()
    elif input_shape == 2:
        calculate_triangular_prism()
    elif input_shape == 3:
        calculate_sphere()
    else: 
        continueprogram = True
