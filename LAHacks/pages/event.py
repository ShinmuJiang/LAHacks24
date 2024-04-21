import reflex as rx

# def event():
#     return rx.text("Event Page")

def event():
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.heading("Event page!", size="9"),
            rx.text("blah blah blah"),
            rx.button(
                "Next",
                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                _hover={
                    "opacity": 0.5,
                },
                on_click=lambda: rx.redirect("/photo"),
                size="4",
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )