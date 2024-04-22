import reflex as rx

from rxconfig import config
from sqlmodel import Field, Session, SQLModel, create_engine, select
import reflex as rx

import reflex as rx
import reflex.components.radix.primitives as rdxp

class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        rx.redirect("/event")
        self.form_data = form_data
        print(self.form_data)

        with rx.session() as session:
            print("here")
            session.add(
                Post(
                    date=self.form_data['date'],
                    time=self.form_data['time'],
                    location=self.form_data['location'],
                    description=self.form_data['description']
                )
            )
            print("here1")
            session.commit()
            rx.redirect("/event")
        print("out")
        rx.redirect("/event")

def event_form():
    return rx.flex(
        rx.form.root(
            rx.input.input(
                placeholder="Date",
                name="date",
            ),
            rx.input.input(
                placeholder="Time",
                name="time",
            ),
            rx.input.input(
                placeholder="Location",
                name="location",
            ),
            rx.text_area(
                placeholder="Description",
                name="description",
            ),
            rx.form.submit(
                rx.button("Create Event"),
                as_child=True,
            ),
            on_submit=FormState.handle_submit,
        ),
        direction="column",
        spacing="4",
    )

class Post(rx.Model, table=True):
    date: str
    time: str
    location: str
    description: str

def select_events():
    with rx.session() as session:
        statement = select(Post)
        results = session.exec(statement)
        for hero in results:
            print("debug point one reached")
            print(hero)

def post():
    return rx.center(
        rx.flex(
            rx.vstack(
                rx.heading("Create", size="9", color="#fdfdfd"),
                rx.text("Fill in details here", color="#fdfdfd"),
            ),
            rx.vstack(
            rx.form(
                rx.flex(
                    rx.hstack(rx.icon("calendar"), rx.text("Event Date", size="1"), spacing="4"),
                    rx.input(
                        placeholder="Month, Date",
                        name="date",
                        style={"width": "500px"},
                    ),
                    direction="column",
                ),
                rx.flex(
                    rx.text("\n\n"),
                    direction="column",
                ),
                rx.flex(
                    rx.hstack(rx.icon("clock"), rx.text("Time", size="1")),
                    rx.select(
                        ["Morning", "Noon", "Evening"],
                        placeholder="Time of Day",
                        name="time",
                        style={"width": "500px"},
                    ),
                    direction="column",
                ),
                rx.flex(
                    rx.hstack(rx.icon("locate-fixed"), rx.text("Location", size="1")),
                    rx.input(
                        placeholder="Location",
                        name="location",
                        style={"width": "500px"},
                    ),
                    direction="column",
                ),
                rx.flex(
                    rx.hstack(rx.icon("text"), rx.text("Description", size="1")),
                    rx.text_area(
                        placeholder="Description",
                        name="description",
                        style={"width": "500px"},
                    ),
                    direction="column",
                ),
                direction="column",
                color="#fdfdfd",
            ),
            rx.button(
                "Create an event",
                background_image="linear-gradient(144deg,#84b3a1,#7f79a3 50%,#d2d8d9)",
                box_shadow="rgba(175, 247, 168, 0.8) 0 15px 30px -10px",
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
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
        background="#192734"
    )


# def post():
#     return rx.center(
#         rx.vstack(
#             rx.heading("Post", size="9"),
#             rx.text("Fill in your details here"),
#                 rx.form(
#                     rx.vstack(
#                         rx.hstack(rx.icon("calendar"), rx.text("Event Date", size="1"),
#                         rx.input(
#                             placeholder="Month, Date",
#                             name="date",
#                             style={"width": "500px"},
#                         ),
#                         ),
#                         rx.hstack(rx.icon("clock"), rx.text("Time", size="1"),
#                         rx.select(
#                             ["Morning", "Noon", "Evening"],
#                             placeholder="Time of Day",
#                             name="time",
#                             style={"width": "500px"},
#                         )
#                         ),

#                         rx.hstack(rx.icon("locate-fixed"), rx.text("Location", size="1"),
#                         rx.input(
#                             placeholder="Location",
#                             name="location",
#                             style={"width": "500px"},
#                         ),
#                         ),

#                         rx.hstack(rx.icon("text"), rx.text("Description", size="1"),
#                         rx.text_area(
#                             placeholder="Description",
#                             name="description",
#                             style={"width": "500px"},
#                         ),
#                         ),
#                         # rx.button(
#                         #     "Submit",
#                         #     background_image="linear-gradient(144deg,#84b3a1,#7f79a3 50%,#d2d8d9)",
#                         #     box_shadow="rgba(175, 247, 168, 0.8) 0 15px 30px -10px",
#                         #     _hover={
#                         #         "opacity": 0.5,
#                         #     },
#                         #     size="3",
#                         #     type="submit"
#                         # ),
#                     ),
#                     # on_click=lambda: rx.redirect("/event"),
#                     # on_submit=FormState.handle_submit,
#                     # reset_on_submit=True,
#                     style={"maxWidth": "800px"},
#                 ),
#             rx.button(
#                 "Create an event",
#                 background_image="linear-gradient(144deg,#84b3a1,#7f79a3 50%,#d2d8d9)",
#                 box_shadow="rgba(175, 247, 168, 0.8) 0 15px 30px -10px",
#                 _hover={
#                     "opacity": 0.5,
#                 },
#                 on_click=lambda: rx.redirect("/event"),
#                 size="4",
#             ),
#             # width="100%",

#             align="center",
#             spacing="7",
#             font_size="2em",
#             color="#fdfdfd",
#         ),
#         height="100vh",
#         background="#192734"
#     )

#     return rx.center(
#         rx.vstack(
#             rx.heading("Post page!", size="9"),
#             rx.text("Fill in your interests here"),

#             rx.form(
#                 rx.vstack(
#                     # rx.file_input(
#                     #     name="image",
#                     #     thumbnail="default.jpg",  # replace with your default image path
#                     # ),
#                     # rx.datetime_input(
#                     #     placeholder="Start",
#                     #     name="start",
#                     # ),
#                     # rx.datetime_input(
#                     #     placeholder="End",
#                     #     name="end",
#                     # ),
#                     rx.select.root(
#                         rx.select.trigger(
#                             placeholder="Select Interests",
#                         ),
#                         rx.select.content(
#                             rx.select.group(
#                                 rx.select.item(
#                                     "Helping homeless people", value="homeless"
#                                 ),
#                                 rx.select.item(
#                                     "Picking up trash", value="sustainability"
#                                 ),
#                             ),
#                         ),
#                         name="interstForm",
#                     ),
#                     # rx.textarea(
#                     #     placeholder="Description",
#                     #     name="description",
#                     # ),
#                     # rx.switch("Public", name="public"),
#                     # rx.button("Submit", type="submit"),
#                     # rx.button(
#                     #     "Submit",
#                     #     background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
#                     #     box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
#                     #     _hover={
#                     #         "opacity": 0.5,
#                     #     },
#                     #     on_click=lambda: rx.redirect("/event"),
#                     #     size="4",
#                     # ),
#                 ),
#                 # on_submit=PostFormState.handle_submit,
#                 # reset_on_submit=True,
#             ),
#             rx.divider(),
#             # rx.heading("Results"),
#             # rx.text(PostFormState.form_data.to_string()),
#             rx.button(
#                 "Submit",
#                 background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
#                 box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
#                 _hover={
#                     "opacity": 0.5,
#                 },
#                 on_click=lambda: rx.redirect("/event"),
#                 size="4",
#             ),

#             align="center",
#             spacing="7",
#             font_size="2em",
#         ),
#         height="100vh",
#     )
