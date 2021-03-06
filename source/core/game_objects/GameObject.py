from source.core.utils import Constants
from source.core.utils.Pose import Pose


class GameObject:
    """
    A GameObject is an element that will be placed on the map. Possible
    GameObjects: BomberBoy, bomb, powerup and obstacles.
    """

    def __init__(self, initial_tile, id):
        """
        Default constructor for the GameObject.
        :param initial_tile: Initial tile coordinates for the object.
        :param id: Character id owner of this object.
        """

        self._pose = Pose((2 * initial_tile[1] + 1) * Constants.SQUARE_SIZE / 2,
                          (2 * initial_tile[0] + 1) * Constants.SQUARE_SIZE / 2)
        self.__id = id

    def update(self, clock, tilemap):
        """
        Abstract method which updates the game object intrinsic information.
        :param clock: Pygame.time.Clock object with the game's clock.
        :param tilemap: Numpy array, optional, which contains the current map
        information.
        :return: True if the object still exists.
        """

        pass

    def draw(self, display):
        """
        Abstract method which updates the game object icon on the screen.
        :param display: Pygame display object.
        """

        pass

    @property
    def pose(self):
        """
        Getter for the game object's pose on the map in pixels.
        :return: Object's pose in pixels.
        """

        return self._pose

    @property
    def tile(self):
        """
        Getter for the game object's tile coordinate on the map.
        :return: Object's coordinate.
        """

        return (int(self._pose.y / Constants.SQUARE_SIZE),
                int(self._pose.x / Constants.SQUARE_SIZE))

    @property
    def id(self):
        """
        Getter for the character id.
        :return: Character id.
        """

        return self.__id
