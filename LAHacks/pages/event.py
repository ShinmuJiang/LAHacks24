import reflex as rx

# def event():
#     return rx.text("Event Page")
import google.generativeai as genai

genai.configure(api_key="AIzaSyDxIzgfd9deVd4WTXfHQaLL262NkcxooHA")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

text = """You will be asked a question. Your reply should include a title, a descriptive paragraph, and a concluding paragraph as illustrated below. Format it well in markdown with bulletpoints too. 

Real question: Create a volunteering event in Los Angeles, around noon, that combines some general aspects of poverty, park , cleanup, sustainability, planting, and painting. Find one restaurant close to the venue and suggest it with details on the popular menu items. Include the rating of the restaurant. Fill it all in with specific details. For the venue of the event and the restaurant, include a link to google maps.

Example question: Create a volunteering event in Los Angeles, around noon, that combines some general aspects of poverty, park , cleanup, sustainability, planting, and painting. Find one restaurant close to the venue and suggest it with details on the popular menu items. Include the rating of the restaurant. Fill it all in with specific details. For the venue of the event and the restaurant, include a link to google maps. 
Example reply:
Be the Change: Community Revitalization Project at Gloria Molina Grand Park!
Join us for a volunteer event that tackles several important issues in a fun and impactful way!

Date: Saturday, May 18th

Time: 12:00 PM - 4:00 PM

Location: Gloria Molina Grand Park (200 N Grand Ave, Los Angeles, CA 90012, USA) Link to park on Google Maps

Description:

We'll be working together to revitalize Gloria Molina Grand Park, a vital green space in a neighborhood grappling with poverty.

Activities will include:

Park Cleanup: We'll pick up trash, remove debris, and make the park a more welcoming space for everyone.
Sustainability Workshop: Learn about easy ways to incorporate sustainable practices in your daily life, like water conservation and composting.
Planting Project: Plant drought-resistant flowers, shrubs, and trees to beautify the park and create a habitat for pollinators.
Community Mural Project: Help create a vibrant mural on the park wall that reflects the neighborhood's spirit and history. (All artistic abilities welcome!)
Why volunteer?

By participating, you'll be:

Contributing to a cleaner and more vibrant park for the community, especially those facing economic challenges.
Learning about sustainability and how to make a difference.
Creating a beautiful and welcoming space for everyone to enjoy.
Building a sense of community pride and connection.
Lunch Break:

Take a break at 1:30 PM and grab a bite to eat at Bottega Louie, a delicious local spot just a short walk from the park (700 S Grand Ave, Los Angeles, CA 90017, USA). Link to restaurant on Google Maps

About Bottega Louie:

Bottega Louie offers a variety of fresh, flavorful pizzas, pastas, and small plates in a bright, bustling space. They also have a popular weekend brunch menu and macarons to-go.

Here are some of their most popular menu items:

Pizzas: Choose from a variety of classic and creative pizzas, like the Margherita or the Spicy soppressata diavola.
Pastas: Their pastas are made fresh daily and come in a variety of sauces, including pomodoro, pesto, and carbonara.
Small Plates: They offer a selection of small plates, perfect for sharing or for a light meal. Some popular options include the roasted Brussels sprouts, the grilled artichoke hearts, and the beef carpaccio.
Bottega Louie also has a great selection of wines, beers, and cocktails.

Registration:

Register for the event at [link to volunteer registration website]. Spots are limited, so sign up today!

We look forward to seeing you there and making a positive impact together!
"""
response = chat.send_message(text)
without_title = chat.send_message(f"repeat this but without the title: {response.text}")
title = chat.send_message("repeat the title without the bold")
def event():
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            #rx.heading(title.text, size="9", color_scheme="crimson"),
            rx.markdown(response.text),
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
            spacing="2",
            font_size="2em",
            margin_left= "8em",
            margin_right= "8em",
        ),
        background="blue"
    )