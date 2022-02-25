
from game.casting.artifact import Artifact

class Score (Artifact):

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

    def add_points(self, artifacts, robot):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        points = 0
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                if artifact.get_text() == '*':
                    points = 1
                elif artifact.get_text() == 'o':
                    points = -1
                artifact.set_text("")
                self._points += points
        return self._points