"""
Configuration parameters for go-kart frame modeling.

All dimensions in inches unless otherwise specified.
"""

class FrameParameters:
    """Parameters defining the go-kart frame geometry"""
    
    # Overall dimensions
    wheelbase = 144.0  # inches (12 feet) - distance front to rear axle
    width = 66.0  # inches (5.5 feet) - overall frame width
    
    # Seating configuration
    num_rows = 5
    seats_per_row = 2
    seat_width = 18.0  # inches per seat
    seat_depth = 16.0  # inches front-to-back
    seat_height = 12.0  # inches off ground
    row_spacing = 24.0  # inches between seat rows
    
    # Frame tubing
    main_tube_od = 1.75  # inches outer diameter
    main_tube_wall = 0.095  # inches wall thickness
    cross_tube_od = 1.5  # inches
    cross_tube_wall = 0.083  # inches
    
    # Roll cage
    roll_hoop_height = 48.0  # inches above seat
    roll_hoop_width = 44.0  # inches
    
    # Suspension pickup points (simple dimensions)
    front_axle_offset = 12.0  # inches from front
    rear_axle_offset = 12.0  # inches from rear
    track_width_front = 54.0  # inches (wheel center to wheel center)
    track_width_rear = 54.0  # inches
    
    # Engine bay
    engine_bay_length = 30.0  # inches
    engine_bay_width = 36.0  # inches
    engine_mount_height = 8.0  # inches above frame floor
    
    # Ground clearance
    ground_clearance = 4.0  # inches
    
    @classmethod
    def get_total_length(cls):
        """Calculate total frame length"""
        return cls.wheelbase + cls.front_axle_offset + cls.rear_axle_offset
    
    @classmethod
    def get_seat_area_length(cls):
        """Calculate length needed for all seats"""
        return (cls.num_rows - 1) * cls.row_spacing + cls.seat_depth
