from game.casting.actor import Actor


class Artifact(Actor):
    """ 
    The responsibility of Artifact is to keep track of the rock and gem artifacts 
    and assign points values
    
    Attributes:
        
        _points (int): the points the player earns or loses when catching an artifact.
    """

    def __init__(self):
        super().__init__()
        self._points = 1
        self._text = ""

    def get_points(self):
        """Gets the artifacts's point value.
        
        Returns:
            int: the points
        """
        return self._points
    

    def set_points(self): 
        """Assigns points based on artifact type (rock or gem).
        
        Returns:
            _points (int): the appropriate number of points for the 
            given artifact type.
        """
        self._points = self._points

    def get_text(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._text

    def set_text(self, text): 
        """Assigns points based on artifact type (rock or gem).
        
        Returns:
            _points (int): the appropriate number of points for the 
            given artifact type.
        """
        self._text = text

    def set_position(self, position):
            """Updates the position to the given one.
            
            Args:
                position (Point): The given position.
            """
            self._position = position

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
    