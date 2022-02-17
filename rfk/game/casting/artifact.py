from game.casting.actor import Actor


class Artifact(Actor):
    """ 
    The responsibility of Artifact is to keep track of the rock and gem artifacts 
    and add or remove points as necessary.
    
    Attributes:
        _points (int): the points the player earns or loses when catching an artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self):
        """Returns the current score.
        
        Returns:
            int: The current score.
        """
        return self._points

    def add_points(self, points):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")