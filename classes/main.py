# Do not modify these lines
__winc_id__ = "04da020dedb24d42adf41382a231b1ed"
__human_name__ = "classes"


# Add your code after this line
class Player:
    def __init__(self, name, speed, endurance, accuracy):
        if (
            speed < 0
            or speed > 1
            or endurance < 0
            or endurance > 1
            or accuracy < 0
            or accuracy > 1
        ):
            raise ValueError("Speed, endurance and accuracy should be between 0 and 1.")
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        if self.speed > self.endurance and self.speed > self.accuracy:
            return ("speed", self.speed)
        elif self.speed == self.endurance and self.speed > self.accuracy:
            return ("speed", self.speed)
        elif self.speed == self.accuracy and self.speed > self.endurance:
            return ("speed", self.speed)
        elif self.endurance > self.speed and self.endurance > self.accuracy:
            return ("endurance", self.endurance)
        elif self.endurance > self.speed and self.endurance == self.accuracy:
            return ("endurance", self.endurance)
        elif self.accuracy > self.speed and self.accuracy > self.endurance:
            return ("accuracy", self.accuracy)
        elif self.accuracy > self.speed and self.accuracy == self.endurance:
            return ("accuracy", self.accuracy)


class Commentator:
    def __init__(self, name):
        self.name = name

    def sum_player(self, object):
        tmp_speed = getattr(object, "speed")
        tmp_endurance = getattr(object, "endurance")
        tmp_accuracy = getattr(object, "accuracy")

        sum = tmp_speed + tmp_endurance + tmp_accuracy

        return sum

    def compare_players(self, object_a, object_b, attribute):
        name_a = getattr(object_a, "name")
        name_b = getattr(object_b, "name")

        score_a = getattr(object_a, attribute)
        score_b = getattr(object_b, attribute)

        if score_a > score_b:
            return name_a
        elif score_b > score_a:
            return name_b
        elif score_a == score_b:
            strength_a = object_a.strength()
            strength_b = object_b.strength()

            if strength_a > strength_b:
                return name_a
            elif strength_b > strength_a:
                return name_b
            elif strength_a == strength_b:
                sum_a = self.sum_player(object_a)
                sum_b = self.sum_player(object_b)

                if sum_a > sum_b:
                    return name_a
                elif sum_b > sum_a:
                    return name_b
                elif sum_a == sum_b:
                    return "These two players might as well be twins!"
