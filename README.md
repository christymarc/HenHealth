# HenHealth
Hackathon 2020 Project

Created by Christiana Marchese, Saatvik Kher, and Rachel Homan

Overview:
Our team tackled the prompt of being a college student on campus in the spring during the Covid-19 pandemic. As Pomona students, we saw this as an opportunity to increase peace of mind and efficiency in the campus community with a health app: HenHealth. Our app helps students keep track of users they have interacted with and alerts them if they’ve been in recent contact with someone who contracted Covid-19. We used the programming language Python (with the Kivy, Pandas, and NumPy libraries), a Twilio API, and an SQLite database to create our app, log user data, and send the text alerts. 

Motivation:
Our motivation is to provide peace of mind for the students and faculty at Pomona College. The text alert cuts down response time, hence the individual is less likely to spread the virus. This project is important to our team because we’re all first years who have yet to experience college in-person. We want to be on campus, but only if we feel safe. The future of this project is for the Pomona community to download the app. With mass use, the college might be more open to allowing students back and we’ll have a happier and healthier campus.  

Functionality:
The users are met with our logo/welcome screen. They are then prompted to login or create an account. Once in, a menu appears with “Log a New Interaction”, “Wellness Evaluation”, “Alert Friends”, and  “Logout”. To “Log a New Interaction”, the user inputs the person they’ve been in contact with and our database stores it. If the user contracts Covid-19, they can use the “Alert Friends” feature to send a text to all the users they’ve been in contact with in the past 2 weeks. The user can also use the "Welness Evaluation" feature to take a test that uses WHO recommendations and questions to evaluate whether or not a user should be tested for COVID.
