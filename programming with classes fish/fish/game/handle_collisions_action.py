from game.action import Action
from game import constants
from game.point import Point
from game.audio_service import AudioService
from game.score import Score

import random
food_x = 540
audio_service = AudioService()

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        fish = cast["fish"][0]
        shark = cast["shark"][0]
        shark1 = cast["shark"][1]
        shark2 = cast["shark"][2]
        food = cast["food"][0]

        scores = cast["score"]


        if self._physics_service.is_collision(shark, fish):
            audio_service.play_sound(constants.SOUND_BOUNCE)
            fish.set_position(Point(10, random.randint(0,560)))
            if len(scores) != 0:
                x = len(scores) - 1
                scores.pop(x)
        if self._physics_service.is_collision(shark1, fish):
            audio_service.play_sound(constants.SOUND_BOUNCE)
            fish.set_position(Point(10, random.randint(0,560)))
            if len(scores) != 0:
                x = len(scores) - 1
                scores.pop(x)
        if self._physics_service.is_collision(shark2, fish):
            audio_service.play_sound(constants.SOUND_BOUNCE)
            fish.set_position(Point(10, random.randint(0,560)))
            if len(scores) != 0:
                x = len(scores) - 1
                scores.pop(x)

        if self._physics_service.is_collision(food, fish):
            audio_service.play_sound(constants.SOUND_BOUNCE)
            food.set_position(Point((random.randint(10,750)), 0))
            if len(scores) != 12 or 0:
                score = Score()
                num = (len(scores))
                x = cast["score"][num - 1]
                # print('this ran')
                if x != 0:
                    if x.get_position().get_x() >= 60:
                        new = x.get_position().get_x()
                        x = new - 65
                        score.set_position(Point(x, 550))
                        score.set_image(constants.IMAGE_SHELL)
                        scores.append(score)
                        food.set_velocity(Point(0, random.randint(5,10)))
                        # print('this ran')
                        cast["score"] = scores

        

