import reflex as rx

def photo():
    return rx.center(
        rx.flex(
            rx.hstack(
                rx.image(src="https://i.ibb.co/KDqgRJr/Two-dogs-in-cage.jpg", width="auto", height="500px"),
                rx.image(src="https://images.unsplash.com/photo-1618477462146-050d2767eac4?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width="auto", height="500px"),
                rx.image(src="https://i.ibb.co/d6R638Z/Green-Plant-Leaves.jpg", width="auto", height="500px"),
                direction="row",
                spacing="4",
                style={"width": "100%"},
            ),
            rx.heading("Photo Page", size="9"),
            rx.text("Upload photos from your day"),
            rx.button(
                "Post photo",
                background_image="linear-gradient(144deg,#84b3a1,#7f79a3 50%,#d2d8d9)",
                box_shadow="rgba(175, 247, 168, 0.8) 0 15px 30px -10px",
                _hover={
                    "opacity": 0.5,
                },
                on_click=lambda: rx.redirect("/"),
                size="4",
            ),
            direction="column",
            align="center",
            spacing="7",
            font_size="2em",
            color="#fdfdfd",
        ),
        height="100vh",
        background="#192734",
    )