from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.


def unique_koala_facts(n):
    collected_facts = []
    count = 0
    dubbelcheck = 0

    while count < n and dubbelcheck < 1000:
        fact = random_koala_fact()

        if fact in collected_facts:
            dubbelcheck += 1
            continue

        collected_facts.append(fact)
        count += 1

    return collected_facts


def num_joey_facts():
    term = "joey"
    count = 0
    unique_term = []

    while count < 10:
        fact = random_koala_fact()

        if term in fact and fact not in unique_term:
            unique_term.append(fact)
            count += 1
        elif term in fact and fact in unique_term:
            count += 1

    return len(unique_term)


def koala_weight():
    while True:
        # get a fact
        fact = random_koala_fact()

        # finding 'kg' in a fact. If not, return and get a new fact.
        if "kg" in fact:
            # what is the starting location of 'kg' in that fact?
            kg_location = fact.find("kg")

            # and the starting number before 'kg'?
            weight_start = fact.rfind(" ", 0, kg_location)

            # check if there is a space before 'kg'. If there is: try again.
            if weight_start == kg_location - 1:
                weight_start = fact.find(" ", weight_start, 0)

            # if not, we know the starting location. Now we can slice
            # the number and save it to a var.
            if weight_start < kg_location - 1:
                answer = fact[weight_start + 1:kg_location]
                break

    return int(answer)


if __name__ == "__main__":
    print(random_koala_fact())
    # Try if they work...
    # print(unique_koala_facts(2))
    # print(num_joey_facts())
    # print(koala_weight())
