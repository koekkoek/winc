# Inleiding
Ik vond het erg leuk om te werken aan deze opdracht. Ik heb er wat meer functies aan toegevoegd dan nodig was en heb nog steeds ideeën hoe het programma verder uit te bouwen. Alle mogelijkheden staan beschreven voor de gebruiker in het 'Readmy.md' bestand. Daar kun je ook alle mogelijke commands voor de terminal vinden.

Verder heb ik gebruik gemaakt van de volgende mogelijkheden:
* Werken met CSV bestanden (openen, wijzigen, importeren en exporteren)
* Werken met JSON bestanden (importeren en exporteren)
* Rich module voor opmaak 
    * Voor een mooie statusbalk bij exporteren gebruik je: *inventory --now --export*
    * Ik heb ook ingebouwd dat er per dag een nieuw CSV bestand wordt aangemaakt (dus met huidige datum in bestandsnaam). Zo kun je exports van andere dagen dus makkelijk terugvinden.
* Tabulate module voor het opmaken van tabellen.
* Datetime module voor aanmaken datum, converteren tussen str en datetime objecten, dagen toevoegen, enz.
* Re module (regular expressions) om te checken of een gebruiker echt een datum meegeeft
    * Bekijk de functie "it_is_a_valid_input()" in functions.py om te zien hoe ik het gedaan heb.
    * Proberen of het werkt? Vul bijvoorbeeld een ongeldige datum in, bijvoorbeeld: *python super.py set_date 2023-01-011*

# Een aantal functies verder uitgelicht
## Inkomsten berekenen
Via het command *python super.py report revenue* kunnen drie verschillende inkomsten rapporten worden opgevraagd:
1. Van wat het programma ziet als vandaag
2. Van wat het programma ziet als gisteren
3. Van een specifieke datum die gebruiker opgeeft.

De functie doorloopt de volgende stappen:
1. Het wanneer (vandaag, gisteren of specifieke datum) wordt in de functie meegegeven als argument.
2. Vervolgens wordt de datum als datetime format in een variabele gezet.
3. Daarna wordt het bestand geopend waar alle verkochte items in zitten
4. Deze gegevens voeg ik toe in een dictionary
5. Elk item wordt een voor een doorlopen
6. Per item wordt gekeken of de verkoopdatum overeenkomt met de eerder bepaalde datum (stap 1-2)
7. Als een item op die dag verkocht is, dan wordt de verkoopprijs toegevoegd aan de variabele 'total_revenue'
8. De functie geeft de waarde van total_revenue terug.

### Hierbij de code:

    def get_revenue_report(when):
    """Get reveneu report of today, yesterday or specific date"""
    total_revenue = 0
    if when == "today":
        date = get_current_date()
    elif when == "yesterday":
        date = date_to_datetime(get_current_date())
        date = date - timedelta(days=1)
    else:
        date = datetime.strptime(when, '%Y-%m-%d').date()
    # Open sold file
    with open(sell_path) as sell_file:
        sold_items = csv.DictReader(sell_file)
        # Iterate over sold items
        for item in sold_items:
            # Check is sold date is the same as today
            if item['sell_date'] == str(date):
                total_revenue += float(item['sell_price'])
    return total_revenue

### Welk probleem lost dit op?
Natuurlijk het ophalen van een inkomsten rapport. En daarnaast ook dat in deze functie in 1 keer drie mogelijkheden gebruikt kunnen worden: vandaag, gisteren en een specifieke datum.

### Hoe roep ik de functie aan?
De functie is aan te roepen met het volgende command:

    python super.py report revenue


## Importeren van standaard data om super.py als demo te gebruiken
Ik heb het mogelijk gemaakt om data in te laden, zodat je het programma snel kunt gebruiken.

Er worden vervolgens vier bestanden uitgelezen:
1. Importeren van .json file met daarin aangekochte producten
2. Importeren van .json file met daarin verkochte producten.
3. id.txt wordt uitgelezen voor het eerstvolgende id dat meegegeven moet worden
4. current_day.txt wordt gebruikt om de huidige datum in te stellen. 

Bij de aangekochte en verkochte producten worden ook de 'keys' uitgelezen en in rij 1 in het bestreffende csv document geplaatst.

### Hierbij de code

    def import_new_data():
    """Function to import standard data to try superpy as a demo"""
    # Get bought data in JSON format
    with open("import\\json_bought.json") as json_file:
        json_data = json.load(json_file)
    # Add JSON data to CSV bought file
    with open(bought_path, mode="w", newline="") as bought_file:
        csv_writer = csv.writer(bought_file)
        # Count var for writing headers to CSV file
        count = 0
        for row in json_data:
            if count == 0:
                header = row.keys()
                csv_writer.writerow(header)
                count += 1
            # Writing JSON data to CSV file
            csv_writer.writerow(row.values())
    # Get sold data in JSON format
    with open("import\\json_sold.json") as json_file:
        json_data = json.load(json_file)
    # Add JSON data to CSV data file
    with open(sell_path, mode="w", newline="") as sold_file:
        csv_writer = csv.writer(sold_file)
        # Count var for writing headers to CSV file
        count = 0
        for row in json_data:
            if count == 0:
                header = row.keys()
                csv_writer.writerow(header)
                count += 1
            # Writing JSON data to CSV file
            csv_writer.writerow(row.values())
    # Set date
    with open("import\\standard_day.txt") as day_file:
        day_data = day_file.read()
        if day_data == "":
            day_data = "2023-09-07"
    with open("data\\current_day.txt", mode="w") as current_day:
        current_day.write(day_data)
    # Set id
    with open("import\\standard_id.txt") as id_file:
        id_data = id_file.read()
        if id_data == "":
            id_data = "30"
    with open("data\\id.txt", mode="w") as current_id:
        current_id.write(id_data)
    # Print succes message
    rprint("[green]Succesfully[/green] imported all data to csv file.")

### Welk probleem lost dit op?
Het handige van deze mogelijkheid is dat de gebruiker het programma alvast kan proberen.

### Hoe roep ik de functie aan?
De functie is aan te roepen met het volgende command:

    python super.py import

## Maak een lijst waarop alle producten die vandaag te koop zijn
Het is mogelijk om een totaaloverzicht te maken van producten die vandaag te koop zijn. Dit doe ik in een aantal stappen:
1. Een 'inventory' list maken om later producten aan toe te voegen.
2. Ophalen wat de huidige datum is volgens het programma. En met andere functie omzetten naar datetime format.
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

### Hierbij de code

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

Ik heb een andere functie gemaakt voor het opmaken van de lijst. Zo hoef ik eenmalig de code te schrijven voor een mooie opmaak en kan ik dat vervolgens ook bij andere functies gebruiken.
De code voor een mooie layout ziet er zo uit:

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

    python super.py report inventory --yesterday

# Verdere verbeteringen
Ik heb veel geleerd van dit project en zie ook nog de volgende mogelijke verbeteringen:
1. Het toevoegen van 'amount' om meerdere van dezelfde producten in één keer aan te kopen
2. Bij sommige functies maak ik het resultaat ook op. Dit kan ik beter gescheiden houden. Zo kan de ene functie zich puur bezighouden met teruggeven van gevraagde resultaat, en andere functie met de opmaak. Dit heb ik bij een aantal functies zo geïmplementeerd, maar dat kan bij meer.
3. Nu staan alle functies in 1 groot bestand. Dit is vrij onverzichtelijk. Het zou beter zijn om de functies te categoriseren en in gescheiden documenten te zetten.
4. Ik gebruik best vaak de mogelijheid om een bestand te openen uit te lezen. Dit is een herhaling van zetten. Het is beter om hier een aparte functie van te maken en die aangeroepen kan worden.
5. Het uitbreiden van tests in test_functions.py
6. Het expliciet toevoegen van welke type argumenten een functie verwacht en wat voor type het retourneert. Zoals ik bijvoorbeeld heb gedaan bij: **def advance_time(number_of_days: int) -> str:**
6. En er zijn nog vele mogelijkheden om aan het programma te voegen. Als je nu de functie om data te importeren gebruikt, ben je de eventuele huidige data kwijt. Je zou hier een check op kunnen maken. Als er al data in bestanden aanwezig is, kun je vragen of de gebruiker zeker is dat hij de data wilt overschrijven.