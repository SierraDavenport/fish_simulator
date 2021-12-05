import os
os.environ['RAYLIB_BIN_PATH'] = '.'

from game.audio_service import AudioService
import raylibpy
from game import constants

audio_service = AudioService()


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        
    def start_game(self,cast):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            # TODO: Add some logic like the following to handle game over conditions
            if len(self._cast["score"]) == 0:
                audio_service.play_sound(constants.SOUND_OVER)
                ocean = cast["ocean"][0]
                end = cast["end"][0]
                # end.set_image(constants.IMAGE_END)
                # ocean.set_image(constants.IMAGE_END)
                end.set_image("")
                ocean.set_image("")

            if raylibpy.window_should_close():
                print('ending 2')
                self._keep_playing = False


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)