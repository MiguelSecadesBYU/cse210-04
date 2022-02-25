from game.casting.artifact import Artifact

class Score(Artifact):

    """
    Points earned or lost by Artifact.
    
    The responsibility of a Score is to provide a message about itself.

    Attributes:
        _points (int): the number of points Actor wins or loses to print to Score.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def add_points(self, artifacts, robot):
        """Updates the message to the given one.
        
        Returns:
            _points (int): The updated score.
        """
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                if artifact.get_text() == '*':
                    points = 1
                elif artifact.get_text() == 'o':
                    points = -1
                artifact.set_text("")
                self._points += points
        return self._points