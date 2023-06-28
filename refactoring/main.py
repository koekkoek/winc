# Do not modify these lines
__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


# Add your code after this line


class Homeowner:
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs

    def make_contract(self, specialists):
        contract = []

        # Zoeken in lijst van needs
        for need in self.needs:
            price = 1000
            # Iedere specialist langsgaan
            for prof in specialists:
                # Checken of de 'need' overeenkomt met de 'profession'
                if need == getattr(prof, "profession"):
                    # Als het overeenkomt: checken op prijs
                    if getattr(prof, "pricing") <= price:
                        # Laagste prijs:
                        tmp_contract = {need: getattr(prof, "name")}
                        price = getattr(prof, "pricing")

            # Zodra goedkoopste specialist uit van huidige 'need'
            # gevonden is, dan toevoegen aan contract lijst.
            contract.append(tmp_contract)

        return contract


class Specialist:
    profession = ""
    specialist_list = []

    def __init__(self, name, pricing):
        self.name = name
        self.pricing = pricing
        self.specialist_list.append(self)


class Electrician(Specialist):
    profession = "electrician"


class Painter(Specialist):
    profession = "painter"


class Plumber(Specialist):
    profession = "plumber"


# Add Specialists
alice = Electrician("Alice Aliceville", 50)
bob = Painter("Bob Bobsville", 60)
craig = Plumber("Craig Craigsville", 75)
john = Painter("John The Man", 40)
mees = Painter("Mees Kees", 40)


# Add Homeowners
alfred = Homeowner("Alfred Alfredson", "Alfredslane 123", ["painter", "plumber"])
bert = Homeowner("Bert Bertson", "Bertslane 231", ["plumber"])
candice = Homeowner(
    "Candice Candicedottir", "Candicelane 312", ["electrician", "painter"]
)

# Contracten van Alfred
print("\nAlfred's contracten:")
print(alfred.make_contract(Specialist.specialist_list))

# Contracten van Bert
print("\nBert's contracten:")
print(bert.make_contract(Specialist.specialist_list))

# Contracten van Candice
print("\nCandice's contracten:")
print(candice.make_contract(Specialist.specialist_list))
