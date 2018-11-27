from random import choice


class RandomWalk():
    """A class to generate  random walks"""

    def __init__(self, num_points = 5000):
        """Initiates attributes of the walk"""
        self.num_points = num_points

        #All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """Calculate all walk postitions"""

        #Main while loop to walk until len is reched
        while len(self.x_values) < self.num_points:
            #Decide random direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            #Reject Moves that do nothing.
            if x_step == 0 and y_step == 0:
                continue

            #calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)