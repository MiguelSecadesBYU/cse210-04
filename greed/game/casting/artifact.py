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

    def get_points(self):
         """Gets the artifacts's point value.
        
        Returns:
            int: the points
        """
    pass

    def set_points(self): 
        """Assigns points based on artifact type (rock or gem).
        
        Returns:
            _points (int): the appropriate number of points for the 
            given artifact type.
        """
    pass