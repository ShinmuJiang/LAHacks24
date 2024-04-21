import reflex as rx

# def event():
#     return rx.text("Event Page")
import google.generativeai as genai

genai.configure(api_key="AIzaSyDxIzgfd9deVd4WTXfHQaLL262NkcxooHA")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

from rxconfig import config
from sqlmodel import Field, Session, SQLModel, create_engine, select
import reflex as rx

from event import Post;

import reflex as rx

datelist = []
timelist = []
locationlist = []
descriptionlist = []

def select_events():
    with rx.session() as session:
        statement = select(Post)
        results = session.exec(statement)
        for hero in results:
            datelist.append(self.form_data['date'])
            timelist.append(self.form_data['time'])
            locationlist.append(self.form_data['location'])
            descriptionlist.append(self.form_data['description'])

text = """
You will be asked the following question: Create a volunteering event surrounding places in ${locationlist}, around the time of ${timelist} and ${datelist}, that combines some general aspects of ${descriptionlist}. Find one restaurant close to the venue and suggest it with details on the popular menu items. Include the rating of the restaurant. Fill it all in with specific details. For the venue of the event and the restaurant.
Your reply should be just like the example below. Format it as in markdown with bulletpoints too.

Example question: Create a volunteering event in Los Angeles, on 05/18/2024, around noon, that combines some general aspects of poverty, park , cleanup, sustainability, planting, and painting. Find one restaurant close to the venue and suggest it with details on the popular menu items. Include the rating of the restaurant. Fill it all in with specific details. For the venue of the event and the restaurant, include a link to google maps.
Example reply: (Don't include "volunteer event:")(make sure don't include "title:")(make sure you don't include a note about registration)
Be the Change: Community Revitalization Project at Gloria Molina Grand Park!
Join us for a volunteer event that tackles several important issues in a fun and impactful way!

**Date:** Saturday, May 18th (make new line)

**Time:** 12:00 PM - 4:00 PM (make new line)

**Location:** Gloria Molina Grand Park (200 N Grand Ave, Los Angeles, CA 90012, USA) (make new line)

**Description:**

We'll be working together to revitalize Gloria Molina Grand Park, a vital green space in a neighborhood grappling with poverty.

**Activities will include:**

Park Cleanup: We'll pick up trash, remove debris, and make the park a more welcoming space for everyone.
Sustainability Workshop: Learn about easy ways to incorporate sustainable practices in your daily life, like water conservation and composting.
Planting Project: Plant drought-resistant flowers, shrubs, and trees to beautify the park and create a habitat for pollinators.
Community Mural Project: Help create a vibrant mural on the park wall that reflects the neighborhood's spirit and history. (All artistic abilities welcome!)
Why volunteer?

**By participating, you'll be:**

Contributing to a cleaner and more vibrant park for the community, especially those facing economic challenges.
Learning about sustainability and how to make a difference.
Creating a beautiful and welcoming space for everyone to enjoy.
Building a sense of community pride and connection.
Lunch Break:

Take a break at 1:30 PM and grab a bite to eat at Bottega Louie, a delicious local spot just a short walk from the park (700 S Grand Ave, Los Angeles, CA 90017, USA).

**About Bottega Louie:**

Bottega Louie offers a variety of fresh, flavorful pizzas, pastas, and small plates in a bright, bustling space. They also have a popular weekend brunch menu and macarons to-go.

**Here are some of their most popular menu items:**

Pizzas: Choose from a variety of classic and creative pizzas, like the Margherita or the Spicy soppressata diavola.
Pastas: Their pastas are made fresh daily and come in a variety of sauces, including pomodoro, pesto, and carbonara.
Small Plates: They offer a selection of small plates, perfect for sharing or for a light meal. Some popular options include the roasted Brussels sprouts, the grilled artichoke hearts, and the beef carpaccio.
Bottega Louie also has a great selection of wines, beers, and cocktails.

We look forward to seeing you there and making a positive impact together!
Make sure there is no "volunteer event:" at the top of the page

"""
response = chat.send_message(text)
def event():
    before_date, after_date = response.text.split("**Date:", 1)

    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.markdown(before_date),
            rx.image(src="https://i.ibb.co/d6R638Z/Green-Plant-Leaves.jpg"),
            rx.markdown("**Date:" + after_date),
            rx.button(
                "Next",
                background_image="linear-gradient(144deg,#84b3a1,#7f79a3 50%,#d2d8d9)",
                box_shadow="rgba(175, 247, 168, 0.8) 0 15px 30px -10px",
                _hover={
                    "opacity": 0.5,
                },
                on_click=lambda: rx.redirect("/photo"),
                size="4",
            ),
            color="#fdfdfd",
            align="center",
            spacing="2",
            font_size="2em",
            margin_left= "10em",
            margin_right= "10em",
            margin_top= "2em",
            margin_bottom="2em"
        ),
        background="#192734"
    )