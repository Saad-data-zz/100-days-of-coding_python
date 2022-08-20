# import time
# from turtle import Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)
# screen.title("Turtle Crossing Game")
# player = Player()
# car_manager = CarManager()
# scoreboard = Scoreboard()
# screen.listen()
# screen.onkey(player.go_up, "Up")
#
#
# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#
#     car_manager.create_cars()
#     car_manager.move_cars()
#
#     #detect the collision with the car
#     for car in car_manager.all_cars:
#         if car.distance(player) < 20:
#             game_is_on = False
#             scoreboard.game_over()
#
#     #detect the sucessful crossing
#     if player.is_at_finish_line():
#         player.go_to_start()
#         #update the level of game when start over
#         car_manager.level_up()
#         scoreboard.increase_level()
#
# screen.exitonclick()