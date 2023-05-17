# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, greeting="Hello, <name>!"):
    return greeting.replace("<name>", name)


def force(mass, body="earth"):
    gravity = {
        "mercury": 3.7,
        "venus": 8.0,
        "earth": 9.8,
        "moon": 1.6,
        "mars": 3.7,
        "jupiter": 23.1,
        "saturn": 9.0,
        "uranus": 8.7,
        "neptune": 11.0,
        "pluto": 0.7,
    }

    force = mass * gravity[body]
    return force


def pull(m1, m2, d):
    G = 6.674 * (10**-11)
    pull = G * ((m1 * m2) / d**2)
    return pull
