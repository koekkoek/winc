# Do not modify these lines
__winc_id__ = "04da020dedb24d42adf41382a231b1ed"
__human_name__ = "classes"


# Add your code after this line
class Player:
    def __init__(self, name, speed, endurance, accuracy):
        for x in [speed, endurance, accuracy]:
            if x > 1 or x < 0:
                raise ValueError(
                    "Speed, endurance and accuracy should be between 0 and 1."
                )

        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        best = (None, -1)
        for attribute in ["speed", "endurance", "accuracy"]:
            value = getattr(self, attribute)
            if value > best[1]:
                best = (attribute, value)
        return best


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
            strength_a = object_a.strength()[1]
            strength_b = object_b.strength()[1]

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
