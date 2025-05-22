from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Configuration
event_date = datetime(2025, 7, 30, 9, 0, 0)  # July 30, 2025 at 9:00 AM
event_info = {
    "title": "IndabaX Botswana 2025",
    "tagline": "From Knowledge to Impact: Harnessing AI for Botswana's Growth",
    "description": "Join us for Botswana's premier AI conference, bringing together researchers, practitioners, and enthusiasts to explore the latest in artificial intelligence and its applications for national development.",
    "venue": "Botho University, Gaborone",
    "date_string": "July 30 - August 1, 2025",
    "contact_email": "indabax_botswana@deeplearningindaba.com",
    "contact_phone": "+267 72781727",
    "register_link": "https://lnkd.in/dtvbnTQH",
    "speakers_link": "https://lnkd.in/dUzQ6exF",
    "festival_link": "https://lnkd.in/drPJs_JK"
}

organizers = [
    {"name": "Dr. DT", "role": "Conference Chair", "bio": "AI researcher at University of Botswana"},
    {"name": "Dr. Rre Tlotleng", "role": "Technical Program Chair", "bio": "Machine Learning specialist"},
    {"name": "Ms. Robert", "role": "Sponsorship Coordinator", "bio": "Tech industry liaison"},
    {"name": "Dr. Kim", "role": "Conference Chair", "bio": "AI researcher at University of Botswana"},
    {"name": "Dr. Freedmore", "role": "Technical Program Chair", "bio": "Machine Learning specialist"},
    {"name": "Ms. Tlamelo", "role": "Sponsorship Coordinator", "bio": "Tech industry liaison"},
    {"name": "Dr. Sibusiso", "role": "Conference Chair", "bio": "AI researcher at University of Botswana"},
    {"name": "Dr. Gobakwe", "role": "Technical Program Chair", "bio": "Machine Learning specialist"},
    {"name": "Ms. BK", "role": "Sponsorship Coordinator", "bio": "Tech industry liaison"}
]

programme = [
    {
        "day": "Day 1 - JULY 30",
        "theme": "AI Expo & Posters",
        "events": [
            {"time": "08:30 - 09:10", "title": "Registration", "description": ""},
            {"time": "09:10 - 09:30", "title": "Welcome Remarks & Opening Ceremony", "description": ""},
            {"time": "09:30 - 10:30", "title": "Community Empowerment through Technology", "description": "Cultivating a Research Culture in Botswana"},
            {"time": "10:30 - 11:00", "title": "Tea Break & Networking", "description": ""},
            {"time": "11:00 - 13:00", "title": "AI Festival & Demos Exhibition", "description": "Showcase of research projects, AI demos, creative installations & tech products"},
            {"time": "13:00 - 14:00", "title": "Lunch Break & Group Photos", "description": ""},
            {"time": "14:00 - 16:00", "title": "Poster Session", "description": "Poster presentations from researchers, students, and professionals"},
            {"time": "16:00 - 16:30", "title": "AI in African Industries and Beyond", "description": "Bridging the Gap: Inspiring Data Science Enthusiasts"},
            {"time": "16:30 - 17:00", "title": "Closing Remarks for Day 1", "description": ""}
        ]
    },
    {
        "day": "Day 2 - JULY 31",
        "theme": "Python & R Workshops",
        "events": [
            {"time": "08:30 - 09:00", "title": "Registration", "description": ""},
            {"time": "09:00 - 09:15", "title": "Welcome to Day 2", "description": ""},
            {"time": "09:15 - 10:45", "title": "Morning Workshop Sessions (Parallel Tracks)", "description": "- Track 1: Introduction to Python for ML<br>- Track 2: Advanced Python for Data Science<br>- Track 3: Introduction to R for Statistical Analysis"},
            {"time": "10:45 - 11:15", "title": "Tea Break & Networking", "description": ""},
            {"time": "11:15 - 13:00", "title": "Mid-day Workshop Sessions (Parallel Tracks)", "description": "- Track 1: Data Visualization with Python<br>- Track 2: Deep Learning Fundamentals<br>- Track 3: Data Analysis with R"},
            {"time": "13:00 - 14:00", "title": "Lunch Break & Networking", "description": ""},
            {"time": "14:00 - 16:00", "title": "Afternoon Workshop Sessions (Parallel Tracks)", "description": "- Track 1: Machine Learning with Scikit-Learn<br>- Track 2: NLP Applications<br>- Track 3: R for Machine Learning"},
            {"time": "16:00 - 16:30", "title": "Workshop Showcase", "description": "Highlighting key learnings and participant projects"},
            {"time": "16:30 - 17:00", "title": "Closing Remarks for Day 2", "description": ""}
        ]
    },
    {
        "day": "Day 3 - AUGUST 1",
        "theme": "Keynotes & Talks",
        "events": [
            {"time": "08:30 - 09:00", "title": "Registration", "description": ""},
            {"time": "09:00 - 09:15", "title": "Welcome to Day 3", "description": ""},
            {"time": "09:15 - 10:15", "title": "Keynote Address", "description": "From Knowledge to Impact: Harnessing AI for Botswana's Growth"},
            {"time": "10:15 - 10:45", "title": "Tea Break & Networking", "description": ""},
            {"time": "10:45 - 12:15", "title": "Technical Talks Session", "description": "- AI for Social Good<br>- NLP & Local Language AI<br>- Computer Vision Applications"},
            {"time": "12:15 - 13:00", "title": "Panel Discussion", "description": "AI in Agriculture, Health, Finance, and Astronomy"},
            {"time": "13:00 - 14:00", "title": "Lunch Break & Networking", "description": ""},
            {"time": "14:00 - 15:30", "title": "Technical Talks Session", "description": "- Machine Learning Research<br>- Responsible & Ethical AI<br>- AI for Business & Industry"},
            {"time": "15:30 - 16:15", "title": "Panel Discussion", "description": "Policy, Governance & Future Trends in AI"},
            {"time": "16:15 - 17:00", "title": "Closing Ceremony", "description": "Awards, acknowledgments, and closing remarks"}
        ]
    }
]

sponsors = [
    {"name": "Previous Partners", "level": "Previous", "logo": "image.png"},
    {"name": "Botswana Innovation Hub", "level": "Academic", "logo": "bih_logo.png"},
    {"name": "University of Botswana", "level": "Academic", "logo": "uob_logo.png"},
    {"name": "Botho University", "level": "Academic", "logo": "uob_logo.png"}
]

@app.route('/')
def home():
    now = datetime.now()
    time_left = event_date - now
    countdown = {
        "days": time_left.days,
        "hours": time_left.seconds // 3600,
        "minutes": (time_left.seconds % 3600) // 60,
        "seconds": time_left.seconds % 60
    }
    
    return render_template('index.html', 
                          event=event_info, 
                          countdown=countdown,
                          event_date=event_date)

@app.route('/about')
def about():
    return render_template('about.html', 
                          event=event_info, 
                          organizers=organizers)

@app.route('/programme')
def programme_page():
    return render_template('programme.html', 
                          event=event_info, 
                          programme=programme)

@app.route('/sponsors')
def sponsors_page():
    return render_template('sponsors.html', 
                          event=event_info, 
                          sponsors=sponsors)

@app.route('/register')
def register():
    return render_template('register.html', 
                          event=event_info)

if __name__ == '__main__':
    app.run(debug=True)