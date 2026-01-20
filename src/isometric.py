from pygame import Vector2


def isometric_to_2d(point: Vector2) -> Vector2:
    """convert (visual) isometric coordinates to (logical) 2D coordinates

    Args:
        point (Vector2): input coordinates

    Returns:
        Vector2: new coordinated
    """    
    temp_point = Vector2(0, 0)
    temp_point.x = (2 * point.y + point.x) / 2
    temp_point.y = (2 * point.y - point.x) / 2
    return temp_point


def twod_to_iso(point: Vector2) -> Vector2:
    """convert (logical) 2D coordinates to (visual) isometric coordinates

    Args:
        point (Vector2): input coordinates

    Returns:
        Vector2: output coordinates
    """    
    temp_point = Vector2(0, 0)
    temp_point.x = point.x - point.y
    temp_point.y = (point.x + point.y) / 2
    return temp_point
