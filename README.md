# Townhall
## Inspiration 💡
Over 75% of adults in the United States do not participate in volunteering activities, missing out on over a projected 12 billion hours of community service projects. As 32% of nonprofits reported that recruiting was their biggest challenge, much of the lost volunteer hours can be attributed to a lack of exposure to volunteer events. The pervasive difficulty nonprofits face finding passionate volunteers is unacceptable, given technology’s extensive capabilities and reach throughout society today.

Over 35% of volunteers said their main reason for volunteering was socializing. This led us to imagine a world where nonprofits had plentiful, passionate volunteers to carry out their missions. Through Townhall, we developed a solution to this persisting issue by incorporating people’s interests and accommodations into community bonding service events to encourage volunteering and social connection.

We know that if Townhall were implemented in larger cities with more users, the database would be curated more precisely to each individual’s interests, leading to a lasting improvement in each community across the US. Townhall currently only has a limited database of users, so the suggestions may be vague. As more people use Townhall, each generated project will become more diverse and impactful – connecting a collaborative environment for communities and nonprofits.

## What it does 😼
With Townhall, you can connect with your local community and collaborate on nonprofit-sponsored volunteer events that are in your best interests. Find your cause, and make a difference. Here’s how the app works:

**Create**
Enter personal preference details like available location, time, and activity

**See Your Event**
Gemini API generates a detailed event based on multiple data entries from people in the area. Using this data, the API matches people with similar interests and availabilities and creates an event. The event page will include the venue/directions, time/date, and even a description of the event and its activities. It also includes a social aspect of going for food after the event. The API will find local restaurants and display detailed descriptions of their menus.

**Post**
See photos taken by other volunteers around the world who you can draw inspiration from. You can also upload your pictures onto the website and share them on various social media platforms. This not only increases exposure for the website, but also allows volunteers to be proud of their work.

## Challenges we ran into 😩

Out of our team of 4, three of us have almost no coding experience (2 have minimal coding experience, and another has less than a year of experience). With this experience, we spent a lot of time with setting up environments, and experimented a lot with each of the tools below.

**Github**
![alt text](https://i.ibb.co/crMY4kc/Database-Components-Styling-Presentation-1.jpg)

Alvin Tan pushed 4 million lines of code 💀 less than a day after downloading VS Code for the first time. As first-year students with minimal project experience, navigating and learning git was difficult; we experienced hours of encounters with merge conflicts, “fatal errors”, and learning about maintaining the project structure through git.

**Gemini**
Gemini is a crucial API used on our website. The automatic curation of an event is an important aspect of making volunteering opportunities more accessible and available. However, even though the Gemini output was amazing beyond expectations, we encountered many problems with its consistency. A 50/50 chance that the API printing “The Volunteer Event:” was a typical and common problem that was only fixed with two specific statements asking it not to write that. We also encountered a difference in the responses provided by the API vs the Gemini website. This was fixed using specific statements and a specially made template that we suggested the API follow. We had tremendous success and the events made are better than most people can make in a short time.

**Reflex**
One of the things we realized was the documentation for Reflex was missing information regarding some main things:
- Retrieving information from posts
- Styling components
We wrote documentation on the problems we ran into, and the remedies (most of the time which we got from trial and error) for them below:

**Retrieving information from posts**

```
with rx.session() as session:
    print("Checkpoint One")
    session.add(
        Post(
            date=self.form_data['date'],
            time=self.form_data['time'],
            location=self.form_data['location'],
            description=self.form_data['description']
        )
    )
    print("Checkpoint Two")
    session.commit()
```

Above is an excerpt from our code which retrieved information from the post. Each of the post attributes had a name, e.g. “date,” which we could retrieve from the form data as shown above. We figured this out by printing the form_data, and experimenting with how to extract each data value to save within Post.

**Styling components**

```
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
```

Note that “style={“width”: “500px”}, was something that did not appear in the Reflex documentation clearly– the documentation uses widths with percentages, and does not clarify which components it is valid on or not. With this, we were able to change the width of the inputs.

## Accomplishments that we're proud of 🤩
We were able to go from installing Visual Studio Code, and setting up GitHubs to deploying our first website with the help of Reflex!

![alt text](https://i.ibb.co/XZCc0WS/IMG-0091.jpg)

Above is our initial sketch of the outline of our website, Townhall. Through a lot of trouble shooting, and reading through documentations, we were able to implement a lot of **Reflex’s core components** including data displays that utilized the Lucide.dev library, layout features like flex, centers, boxes, and h/vstacks, and forms! Finally, we were able to **upload our form data to Reflex’s sqlmodel.** Finally, we were able to **deploy our app!**

Additionally, we’re proud of how we improved our user interface using Reflex. See progression photos below (contains three iterations).

![alt text] (https://i.ibb.co/ccBr6Q2/Screenshot-2024-04-21-at-6-57-53-AM.png)

## What we learned 👀
A lot! Learning how to utilize 3rd party APIs (Gemini) for leveraging artificial intelligence, databases, and Reflex for the front and back end, git for project structure, and more; with minimal experience, we spent a large portion of time reading documentation, using Gemini to research code and style, and simply traversing the complex world of shell language. Besides the technical exposure, a pivotal moment as a group of mostly first-time hackathon participants was the experience shared with other teams. We loved walking around and sharing ideas, inspiring others and ourselves, and receiving critical suggestions for our product. This irreplaceable experience inspired us to pursue further collaborative developer projects and hackathons.
![alt text](https://i.ibb.co/s5pfFN0/Database-Components-Styling-Presentation.jpg)

## What's next for Townhall 🤔
Townhall goes beyond traditional social media by fostering a community focusing on social good. Townhall has numerous features that will be implemented to provide a more immersive experience. For nonprofits, it will foster a collaborative community, encouraging those driven by intrinsic goals to work together to fulfill their passions. Nonprofits can collaborate on events made through Townhall, paving the way for bigger and more influential volunteer events.

![alt text](https://i.ibb.co/qYnDmLY/Screenshot-2024-04-21-at-7-07-50-AM.png)

Additionally, we’ll begin establishing relations with local restaurants to encourage more users to use our services. This will strengthen the bond between users, who can receive discounts at these restaurants after contributing to Townhall suggested projects, and it will also provide another avenue for users to bond with one another.

With an increase in incentives and exposure, the influx of Townhall users will help curate more specific activities, allowing people to connect with those who share similar interests and have a passion for volunteering. We understand that people pride themselves on their good deeds, and adding a feature that allows users to post photos and share to social media platforms will not only increase awareness, but also provide volunteers with a tangible memory to look back on and encourage them to participate again in Townhall’s events.

# How it was built 🛠️

We used Reflex and Gemini API.

## Setup

### Reflex
First, set up your project environment. Note that this has nothing to do with Reflex/Google yet. `mkdir` means "make a folder/directory on my computer," and `my_app_name` is the name of the folder. `cd` means change directory, which basically navigates your terminal into that folder.

```
mkdir my_app_name
cd my_app_name
```

Next, we set up the python3 virtual environment. The first command creates a virtual environment called `.venv`. The second command activates the environment, which modifies the shell's environment to use the Python interpreter and packages installed within the virtual environment, instead of the system-wide Python interpreter and packages. Overall, a virtual environment is like having a special cooking station within your kitchen for each recipe. It helps us stay organized. More about Python virtual environments [here](https://docs.python.org/3/library/venv.html).
```
python3 -m venv .venv
source .venv/bin/activate
```

Finally we install reflex. `pip` is a package manager written with Python that allows you to install things such as reflex!
```
pip install reflex
```

Follow the steps prompted by Reflex in the terminal; for this project, we selected option (0), which set up an empty Reflex project.

### Gemini API
Think of an API like a menu at a restaurant. Just as you look at the menu and tell the waiter what you want, computer programs use APIs to request specific data or actions from other programs or websites. It's like a set of instructions that helps different programs talk to each other and get what they need without confusion. For example, a weather app might use a weather API to ask a weather website for current temperatures or forecasts. The API acts as a bridge, ensuring smooth communication between different pieces of software.

For the purposes of Gemini API, it allows our application, Townhall, to use Google's Gemini Language model directly in our site! Let's set it up:

First we set up an API key [here](https://ai.google.dev/gemini-api/docs/api-key).

In the terminal, run `pip install -q -U google-generativeai`

Now for the code, we referenced [Google's developer docs](https://ai.google.dev/gemini-api/docs/get-started/python). See our code below.
```
import google.generativeai as genai

genai.configure(api_key="INSERT KEY")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

text = "INSERT PROMPT"

response = chat.send_message(text)
```

In the prompt, we instructed Gemoini to provide the response in markdown, however Gemini also has a feature `to_markdown(response.text)` which we could use for the same utility.

## The Code

### Navigation
Now that we are setup, let's create the app. Given our architecture (shown in sketch above), we need to create 3 pages.

Note how LAHacks.py represents the home page, which links to the next pages `post.py,` `events.py,` and `photo.py.`
For navigation, we set up these 3 pages (in addition to the "home" LAHacks.py page).

We created a folder called `pages,` and created three files (as explained above). Then, in `LAHacks.py,` we have the following.
```
from LAHacks.pages.post import post; #STEP ONE: where user makes a post
from LAHacks.pages.event import event; #STEP TWO: use Gemini API to generate event content
from LAHacks.pages.photo import photo; #STEP THREE: users can upload photos from their day
```

After the implementation of the home page, we have the following:
```
app = rx.App()
app.add_page(index)

app.add_page(post)
app.add_page(event)
app.add_page(photo)
```

### Subpages
Each of the pages has generally the same structure. For the purposes of an example, we take excerpts of code from `photos.py`

```
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
```

First, import reflex as rx, then define a function `photo`. Note that we imported this function in our main home page using `from LAHacks.pages.photo import photo;` Inside the function, we return our page, which uses Reflex.

Important thing to note: notice how in `rx.button`, we have a line of code `on_click=lambda: rx.redirect("/"),`. This basically says that when the button is clicked, it will navigate to `/`, which is just the home page. On other pages, `rx.redirect()` could contain `/event` or `/post`.

### Deployment
To deploy our code, we simply ran the following 2 commands:
```
reflex login
reflex deploy
```