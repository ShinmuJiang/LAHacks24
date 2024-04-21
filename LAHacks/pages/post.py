import reflex as rx

# def post():
#     return rx.text("Post Page")

# def post():
#     return rx.center(
#         # rx.theme_panel(),
#         rx.vstack(
#             rx.heading("Post page!", size="9"),
#             rx.text("Fill in your interests here"),
            # rx.button(
            #     "Submit",
            #     background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
            #     box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
            #     _hover={
            #         "opacity": 0.5,
            #     },
            #     on_click=lambda: rx.redirect("/event"),
            #     size="4",
            # ),
#             align="center",
#             spacing="7",
#             font_size="2em",
#         ),
#         height="100vh",
#     )

config = rx.Config(
    app_name="townhall_app",
    db_url="sqlite:///reflex.db",
)

class Post(rx.Model, table=True):
    date: str
    time: str
    location: str
    description: str

class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

def post():
    return rx.center(
        rx.vstack(
            rx.heading("Post", size="9"),
            rx.text("Fill in your interests here"),
                rx.form(
                    rx.vstack(
                        rx.hstack(rx.icon("calendar"), rx.text("Event Date", size="1"),
                        rx.input(
                            placeholder="Month, Date",
                            name="eventTime",
                            style={"maxWidth": 500},
                        ),
                        ),

                        rx.hstack(rx.icon("locate-fixed"), rx.text("Location", size="1"),
                        rx.input(
                            placeholder="Location",
                            name="eventLocation",
                            style={"maxWidth": 500},
                        ),
                        ),

                        rx.hstack(rx.icon("text"), rx.text("Description", size="1"),
                        rx.text_area(
                            placeholder="Description",
                            name="eventDescription",
                        ),
                        ),
                        rx.button(
                            "Submit",
                            background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                            box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                            _hover={
                                "opacity": 0.5,
                            },
                            size="3",
                            type="submit"
                        ),
                        style={"maxWidth": 500},
                    ),
                    on_submit=FormState.handle_submit,
                    reset_on_submit=True,
                ),
            style={"maxWidth": 500},

            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

    return rx.center(
        rx.vstack(
            rx.heading("Post page!", size="9"),
            rx.text("Fill in your interests here"),

            rx.form(
                rx.vstack(
                    # rx.file_input(
                    #     name="image",
                    #     thumbnail="default.jpg",  # replace with your default image path
                    # ),
                    # rx.datetime_input(
                    #     placeholder="Start",
                    #     name="start",
                    # ),
                    # rx.datetime_input(
                    #     placeholder="End",
                    #     name="end",
                    # ),
                    rx.select.root(
                        rx.select.trigger(
                            placeholder="Select Interests",
                        ),
                        rx.select.content(
                            rx.select.group(
                                rx.select.item(
                                    "Helping homeless people", value="homeless"
                                ),
                                rx.select.item(
                                    "Picking up trash", value="sustainability"
                                ),
                            ),
                        ),
                        name="interstForm",
                    ),
                    # rx.textarea(
                    #     placeholder="Description",
                    #     name="description",
                    # ),
                    # rx.switch("Public", name="public"),
                    # rx.button("Submit", type="submit"),
                    # rx.button(
                    #     "Submit",
                    #     background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                    #     box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                    #     _hover={
                    #         "opacity": 0.5,
                    #     },
                    #     on_click=lambda: rx.redirect("/event"),
                    #     size="4",
                    # ),
                ),
                # on_submit=PostFormState.handle_submit,
                # reset_on_submit=True,
            ),
            rx.divider(),
            # rx.heading("Results"),
            # rx.text(PostFormState.form_data.to_string()),
            rx.button(
                "Submit",
                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                _hover={
                    "opacity": 0.5,
                },
                on_click=lambda: rx.redirect("/event"),
                size="4",
            ),

            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )
