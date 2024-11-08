from config import *
from rotate import *

# Function to change the cube's color
def change_color(color_index):
    global color
    color = color_index[random.randint(0, len(color_index) - 1)]


# Function to render the cube according to its current rotational value
def rotate(angle_x, angle_y):
    rotation_matrix_x = rotate_x(angle_x)
    rotation_matrix_y = rotate_y(angle_y)
    rotation_matrix = np.dot(rotation_matrix_y, rotation_matrix_x)
    projected_vertices = []
    
    for vertex in vertices:
        x, y, z = vertex
        vertex_array = np.array([x, y, z])
        rotated_vertex = np.dot(rotation_matrix, vertex_array)
        x, y, z = rotated_vertex
        x = x * 100 + WIDTH // 2
        y = -y * 100 + HEIGHT // 2
        projected_vertices.append([x, y])
    
    for edge in edges:
        pygame.draw.line(screen, color, projected_vertices[edge[0]], projected_vertices[edge[1]])