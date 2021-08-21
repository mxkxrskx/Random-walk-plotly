from random import choice

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=10000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        #x and y
        self.x_values = [0]
        self.y_values = [0]

        self.x_first_dot = []
        self.y_first_dot = []

        self.x_last_dot = []
        self.y_last_dot = []

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0 :
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def take_first_dot(self):
        """Add first value from x_values and y_values"""

        x = self.x_values.pop(1)
        y = self.y_values.pop(1)
        self.x_first_dot.append(x)
        self.y_first_dot.append(y)

    def take_last_dot(self):
        """Add last value from x_values and y_values"""

        x = self.x_values.pop(-1)
        y = self.y_values.pop(-1)
        self.x_last_dot.append(x)
        self.y_last_dot.append(y)
