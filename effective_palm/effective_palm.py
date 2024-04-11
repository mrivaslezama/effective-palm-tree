"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from effective_palm.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from effective_palm.pages.tools import tools
from effective_palm.pages.team import team
from effective_palm.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
