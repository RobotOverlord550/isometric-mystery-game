from game import Game


def update():
    """gets passed into the Game class instance's loop function to run logic every frame
    """    
    pass


if __name__ == "__main__":
    game = Game()
    game.loop(update)