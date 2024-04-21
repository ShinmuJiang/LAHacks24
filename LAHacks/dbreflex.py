from rxconfig import config

import reflex as rx

class Events(rx.Model, table=True):
    id: int
    name: str
    location: str
    details: str

with rx.session() as session:
    session.add(
        Events(
            id=0,
            name="Trash Cleanup",
            location="Emeryville",
            details="Come pickup trash!"
        )
    )
    session.commit()
