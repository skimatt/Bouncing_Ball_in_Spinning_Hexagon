import pygame
import math
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball in Spinning Hexagon")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Hexagon parameters
HEX_RADIUS = 200
HEX_CENTER = (WIDTH // 2, HEIGHT // 2)
NUM_SIDES = 6

# Ball parameters
BALL_RADIUS = 10
ball_pos = [WIDTH // 2, HEIGHT // 2 - HEX_RADIUS // 2]
ball_velocity = [3, 0]
gravity = 0.2
friction = 0.99

# Rotation speed of the hexagon
rotation_speed = 2

def draw_hexagon(center, radius, rotation_angle):
    """Draw a rotating hexagon."""
    points = []
    for i in range(NUM_SIDES):
        angle = (math.pi / 3) * i + rotation_angle
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    pygame.draw.polygon(screen, BLUE, points, 2)

def get_hexagon_edges(center, radius, rotation_angle):
    """Get the edges of the hexagon as line segments."""
    edges = []
    for i in range(NUM_SIDES):
        angle1 = (math.pi / 3) * i + rotation_angle
        angle2 = (math.pi / 3) * ((i + 1) % NUM_SIDES) + rotation_angle
        x1 = center[0] + radius * math.cos(angle1)
        y1 = center[1] + radius * math.sin(angle1)
        x2 = center[0] + radius * math.cos(angle2)
        y2 = center[1] + radius * math.sin(angle2)
        edges.append(((x1, y1), (x2, y2)))
    return edges

def point_to_line_distance(point, line_start, line_end):
    """Calculate the distance from a point to a line segment."""
    px, py = point
    x1, y1 = line_start
    x2, y2 = line_end
    line_vec = (x2 - x1, y2 - y1)
    point_vec = (px - x1, py - y1)
    line_len_sq = line_vec[0]**2 + line_vec[1]**2
    if line_len_sq == 0:
        return math.hypot(px - x1, py - y1)
    t = max(0, min(1, (point_vec[0] * line_vec[0] + point_vec[1] * line_vec[1]) / line_len_sq))
    proj_x = x1 + t * line_vec[0]
    proj_y = y1 + t * line_vec[1]
    return math.hypot(px - proj_x, py - proj_y)

def reflect_vector(vector, normal):
    """Reflect a vector off a surface with a given normal."""
    dot = vector[0] * normal[0] + vector[1] * normal[1]
    return [vector[0] - 2 * dot * normal[0], vector[1] - 2 * dot * normal[1]]

def main():
    global ball_velocity
    rotation_angle = 0

    while True:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update rotation angle
        rotation_angle += math.radians(rotation_speed)

        # Draw the hexagon
        draw_hexagon(HEX_CENTER, HEX_RADIUS, rotation_angle)

        # Get hexagon edges
        edges = get_hexagon_edges(HEX_CENTER, HEX_RADIUS, rotation_angle)

        # Update ball position
        ball_pos[0] += ball_velocity[0]
        ball_pos[1] += ball_velocity[1]

        # Apply gravity
        ball_velocity[1] += gravity

        # Apply friction
        ball_velocity[0] *= friction
        ball_velocity[1] *= friction

        # Collision detection with hexagon walls
        collision_occurred = False
        for edge in edges:
            start, end = edge
            distance = point_to_line_distance(ball_pos, start, end)
            if distance <= BALL_RADIUS:
                # Calculate normal vector of the edge
                edge_vec = (end[0] - start[0], end[1] - start[1])
                edge_len = math.hypot(edge_vec[0], edge_vec[1])
                normal = (-edge_vec[1] / edge_len, edge_vec[0] / edge_len)
                
                # Reflect the velocity vector
                ball_velocity = reflect_vector(ball_velocity, normal)
                collision_occurred = True

        # Prevent the ball from escaping the hexagon
        if not collision_occurred:
            # Check if the ball is outside the hexagon
            ball_dist_from_center = math.hypot(ball_pos[0] - HEX_CENTER[0], ball_pos[1] - HEX_CENTER[1])
            if ball_dist_from_center > HEX_RADIUS - BALL_RADIUS:
                # Push the ball back inside
                direction = [(ball_pos[0] - HEX_CENTER[0]) / ball_dist_from_center,
                             (ball_pos[1] - HEX_CENTER[1]) / ball_dist_from_center]
                ball_pos[0] = HEX_CENTER[0] + direction[0] * (HEX_RADIUS - BALL_RADIUS)
                ball_pos[1] = HEX_CENTER[1] + direction[1] * (HEX_RADIUS - BALL_RADIUS)
                ball_velocity = reflect_vector(ball_velocity, direction)

        # Draw the ball
        pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()