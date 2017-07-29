"""Module for generating Searching Cards resource."""

from random import sample, shuffle
from math import ceil
from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont
from yattag import Doc
from utils.retrieve_query_parameter import retrieve_query_parameter


def resource(request, resource):
    """Create a copy for Searching Cards resource.

    Args:
        request: HTTP request object (HttpRequest).
        resource: Object of resource data (Resource).

    Returns:
        A list of Pillow image objects (list).
    """
    data = []
    IMAGE_PATH = "static/img/resources/searching-cards/{}-cards-{}.png"
    X_BASE_COORD = 1803
    X_COORD_DECREMENT = 516
    Y_COORD = 240
    FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
    FONT = ImageFont.truetype(FONT_PATH, 200)

    parameter_options = valid_options()
    number_cards = int(retrieve_query_parameter(request, "number_cards", parameter_options["number_cards"]))
    max_number = retrieve_query_parameter(request, "max_number", parameter_options["max_number"])
    help_sheet = retrieve_query_parameter(request, "help_sheet", parameter_options["help_sheet"])

    if max_number == "cards":
        numbers = list(range(1, number_cards + 1))
        shuffle(numbers)
        range_text = "1 to {}".format(number_cards)
    elif max_number != "blank":
        numbers = sample(range(1, int(max_number) + 1), number_cards)
        range_text = "1 to {}".format(max_number)
    else:
        numbers = []
        range_text = "Add list of numbers below:"

    if help_sheet:
        data.append(["html", create_help_sheet(numbers, range_text)])

    number_of_pages = range(ceil(number_cards / 4))
    for page in number_of_pages:
        if page == number_of_pages[-1]:
            image_path = IMAGE_PATH.format(3, 1)
        else:
            image_path = IMAGE_PATH.format(4, page + 1)

        image = Image.open(image_path)

        if max_number != "blank":
            draw = ImageDraw.Draw(image)
            page_numbers = numbers[:4]
            numbers = numbers[4:]
            coord_x = X_BASE_COORD
            for number in page_numbers:
                text = str(number)
                text_width, text_height = draw.textsize(text, font=FONT)
                draw.text(
                    (coord_x - (text_width / 2), Y_COORD - (text_height / 2)),
                    text,
                    font=FONT,
                    fill="#000"
                )
                coord_x -= X_COORD_DECREMENT

        image = image.rotate(90, expand=True)
        data.append(["image", image])

    return data


def create_help_sheet(numbers, range_text):
    """Create helper sheet for resource.

    Args:
        numbers: Numbers used for activity (list).
        range_text: String describing range of numbers (str).

    Returns:
        Pillow image object (Image).
    """
    doc, tag, text, line = Doc().ttl()
    with tag("div"):
        with tag("h1"):
            text("Helper page for binary search activity")
        with tag("p"):
            text(
                "Use this sheet to circle the number you are asking your class ",
                "to look for when you are demonstrating how the binary search ",
                "works. This allows you to demonstrate the maximum number of ",
                "searches it would take. When students are playing the treasure ",
                "hunt game, they can choose any number. Avoid those that are in ",
                "red as they are key binary search positions (avoiding them is a ",
                "good thing to do for demonstrations, but in practice students, ",
                "or computers, won’t intentionally avoid these)."
            )
        with tag("h2"):
            text("Sorted numbers")
        with tag("ul", klass="list-unstyled"):
            numbers.sort()
            red_number_jump = (len(numbers) + 1) // 4
            for (index, number) in enumerate(numbers):
                if (index + 1) % red_number_jump == 0:
                    line("li", number, klass="text-danger")
                else:
                    line("li", number)
    return doc.getvalue()


def subtitle(request, resource):
    """Return the subtitle string of the resource.

    Used after the resource name in the filename, and
    also on the resource image.

    Args:
        request: HTTP request object (HttpRequest).
        resource: Object of resource data (Resource).

    Returns:
        text for subtitle (str).
    """
    number_cards = retrieve_query_parameter(request, "number_cards")
    max_number = retrieve_query_parameter(request, "max_number")
    help_sheet = retrieve_query_parameter(request, "help_sheet")
    paper_size = retrieve_query_parameter(request, "paper_size")

    if max_number == "blank":
        range_text = "blank"
    elif max_number == "cards":
        range_text = "0 to {}".format(number_cards)
    else:
        range_text = "0 to {}".format(max_number)

    if help_sheet:
        help_text = "with helper sheet"
    else:
        help_text = "without helper sheet"

    return "{} cards - {} - {} - {}".format(number_cards, range_text, help_text, paper_size)


def valid_options():
    """Provide dictionary of all valid parameters.

    This excludes the header text parameter.

    Returns:
        All valid options (dict).
    """
    return {
        "number_cards": ["15", "31"],
        "max_number": ["cards", "99", "999", "blank"],
        "help_sheet": [True, False],
        "paper_size": ["a4", "letter"],
    }
