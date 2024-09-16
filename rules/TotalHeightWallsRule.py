import ifcopenshell
import ifcopenshell.geom

# Insert the path to the IFC file (make sure it's correct)
file_path = 'import ifcopenshell
import ifcopenshell.geom

# Insert the path to the IFC file (make sure it's correct)
file_path = 'C:\\Users\\leviz\\Documents\\università\\Erasmus +\\Courses\\BIM\\CES_BLD_24_06_STR.ifc'

# Open the IFC file
ifc_file = ifcopenshell.open(file_path)

# Find all elements of type IfcWall
walls = ifc_file.by_type("IfcWall")

# Loop through the found walls and read their dimensions
for wall in walls:
    # Print the wall's ID
    print(f"Wall ID: {wall.GlobalId}")
    
    # Get the wall's geometry
    shape = ifcopenshell.geom.create_shape(ifcopenshell.geom.settings(), wall)
    
    # Extract the vertices of the geometry
    vertices = shape.geometry.verts
    
    # Extract the Z coordinates (height)
    z_coords = [vertices[i+2] for i in range(0, len(vertices), 3)]  # Take only the Z coordinates
    
    # Calculate the wall height as the difference between the max and min Z
    min_z = min(z_coords)
    max_z = max(z_coords)
    height = max_z - min_z
    
    # Print the wall's height
    print(f"Height of Wall {wall.GlobalId}: {height} meters")'
