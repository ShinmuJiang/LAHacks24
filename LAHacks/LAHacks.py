"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

from LAHacks.pages.post import post; #STEP ONE: where user makes a post
from LAHacks.pages.event import event; #STEP TWO: use Gemini API to generate event content
from LAHacks.pages.photo import photo; #STEP THREE: users can upload photos from their day

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Townhall!", size="9"),
            rx.text("Get started now "),
            rx.button(
                "Create an event",
                background_image="linear-gradient(144deg,#84b3a1,#7f79a3 50%,#d2d8d9)",
                box_shadow="rgba(175, 247, 168, 0.8) 0 15px 30px -10px",
                _hover={
                    "opacity": 0.5,
                },
                on_click=lambda: rx.redirect("/post"),
                size="4",
            ),
            align="center",
            spacing="7",
            font_size="2em",
            color="#fdfdfd",
        ),
        height="100vh",
        background="#192734"
    )



app = rx.App()
app.add_page(index)

app.add_page(post)
app.add_page(event)
app.add_page(photo)