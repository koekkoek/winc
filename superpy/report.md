# Highlight three technical elements
Please include a short, 300-word report that highlights three technical elements of your implementation that you find notable.

Explain what problem they solve and why you chose to implement them in this way.

## Maak een lijst waarop alle producten die vandaag te koop zijn
Het is mogelijk om een totaaloverzicht te maken van producten die vandaag te koop zijn. Dit doe ik in een aantal stappen:
1. Een 'inventory' list maken om later producten aan toe te voegen.
2. Ophalen wat de huidige datum is volgens het programma.
3. Open het bestand waarin alle aangekochte producten te vinden zijn.
    * Lees het bestand, maak er een dictionary van in de variabele 'items'
    * Ga elk product 1 voor 1 langs
4. Check wat de aangekochte datum is
5. Check wat de uiterste houdbaarheidsdatum is
6. Voeg product toe aan 'inventory' lijst als...
    * ... De huidige datum later is dan aankoopdatum
    * ... De uiterste houdbaarheidsdatum later is dan de huidige datum
    * ... Het product niet inmiddels verkocht is (en dus nog niet op de sold lijst staat)
7. Nu hebben we een lijst met daarin alle producten van vandaag. Ieder product is een dictionary in die lijst. Return de lijst

        def get_todays_inventory():
            """Get today's inventory and show to user"""
            inventory = []
            date = date_to_datetime(get_current_date())
            with open(bought_path) as file:
                items = csv.DictReader(file)
                for item in items:
                    item_buy_date = datetime.strptime(
                        item['buy_date'], '%Y-%m-%d').date()
                    item_expiration_date = datetime.strptime(
                        item['expiration_date'], '%Y-%m-%d').date()
                    # Get items in bought.csv who aren't expired
                    # And check if item isn't in sold.csv list
                    if date > item_buy_date and (
                        item_expiration_date > date) and (
                            check_if_sold(item['id'])):
                        inventory.append(item)
            return inventory

Ik heb een andere functie gemaakt voor het opmaken van de lijst. Zo hoef ik eenmalig de code te schrijven voor een mooie opmaak en dat vervolgens ook bij andere functies gebruiken.
De code voor een mooie-layout ziet er zo uit:

    def make_table(inventory):
    """Show inventory in beautiful table"""
    if inventory:
        print(tabulate(inventory, headers="keys", tablefmt="rounded_outline"))
    else:
        print("No inventory.")

1. Aan deze functie kan een lijst met producten (dictionairy) worden meegegeven
2. Als er een lijst met producten is, maak dan een tabel.
3. Voor de tabel gebruik ik de module 'tabulate'. De 'keys' van de dictionary vormen de 1e rij. Voor een mooie opmaak heb ik 'rounded_outline' gekozen.

### Welk probleem lost dit op?
Allereerst helpt deze functie te voorkomen dat we een lijst van producten zien die nog niet aangekocht zijn, die over de datum zijn of die al verkocht zijn.
Vervolgens wordt de lay-out in een andere functie verzorgd, zodat deze ook voor andere functies gebruikt kan worden.

### Hoe roep ik de functie aan?
Gebruik de volgende commando in je CLI:

    python super.py report inventory --today

Wil je liever het overzicht van gisteren? Gebruik dan:

    python super.py report inventory --today
