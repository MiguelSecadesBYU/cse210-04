from game.casting.actor import Actor

class Score(Actor):
    """
    Points earned or lost by Actor.
    
    The responsibility of an Score is to provide a message about itself.

    Attributes:
        _score_points (int): the number of points Actor wins or loses to print to Score.
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