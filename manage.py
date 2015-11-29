__author__ = 'Nick'
import click


@click.group()
def cli():
    pass


@cli.command()
def createdb():
    from model import Beer, BeerStyle, Brewery, BrewerySize

    tables = [Beer, BeerStyle, Brewery, BrewerySize]

    for table in tables:
        if not table.table_exists():
            print("Creating %s table" % table.__name__)
            table.create_table(fail_silently=True)


    BrewerySize.create(label="Microbrewery", description="")
    BrewerySize.create(label="Nanobrewery", description="")
    BrewerySize.create(label="Craftbrewery", description="")
    BrewerySize.create(label="Other", description="")

    styles = [
        "American Amber / Red Ale",
        "American Barleywine",
        "American Black Ale",
        "American Blonde Ale",
        "American Brown Ale",
        "American Dark Wheat Ale",
        "American Double / Imperial IPA",
        "American Double / Imperial Stout",
        "American IPA",
        "American Pale Ale (APA)",
        "American Pale Wheat Ale",
        "American Porter",
        "American Stout",
        "American Strong Ale",
        "American Wild Ale",
        "Black & Tan",
        "Chile Beer",
        "Cream Ale",
        "Pumpkin Ale",
        "Rye Beer",
        "Wheatwine",
        "Belgian Dark Ale",
        "Belgian IPA",
        "Belgian Pale Ale",
        "Belgian Strong Dark Ale",
        "Belgian Strong Pale Ale",
        "Biere de Champagne / Biere Brut",
        "Biere de Garde",
        "Dubbel",
        "Faro",
        "Flanders Oud Bruin",
        "Flanders Red Ale",
        "Gueuze",
        "Lambic - Fruit",
        "Lambic - Unblended",
        "Quadrupel (Quad)",
        "Saison / Farmhouse Ale",
        "Tripel",
        "Witbier",
        "Baltic Porter",
        "Braggot",
        "English Barleywine",
        "English Bitter",
        "English Brown Ale",
        "English Dark Mild Ale",
        "English India Pale Ale (IPA)",
        "English Pale Ale",
        "English Pale Mild Ale",
        "English Porter",
        "English Stout",
        "English Strong Ale",
        "Extra Special / Strong Bitter (ESB)",
        "Foreign / Export Stout",
        "Milk / Sweet Stout",
        "Oatmeal Stout",
        "Old Ale",
        "Russian Imperial Stout",
        "Winter Warmer",
        "American Adjunct Lager",
        "American Amber / Red Lager",
        "American Double / Imperial Pilsner",
        "American Malt Liquor",
        "American Pale Lager",
        "California Common / Steam Beer",
        "Light Lager",
        "Low Alcohol Beer",
    ]

    for style in styles:
        BeerStyle.create(label=style)

@cli.command()
def run():
    from app import app
    app.run(debug=True)


if __name__ == "__main__":
    cli()