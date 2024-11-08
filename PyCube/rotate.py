from config import *

# Rotation matrices
def rotate_x(angle):
    return np.array([
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ])

def rotate_y(angle):
    return np.array([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ])

def rotate_z(angle):
    return np.array([
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ])

def rotate(angle_x, angle_y):
    # Rotate cube
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

