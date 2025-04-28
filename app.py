from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Configuration
event_date = datetime(2025, 6, 30, 9, 0, 0)  # Example date: June 15, 2025 at 9:00 AM
event_info = {
    "title": "IndabaX Botswana 2025",
    "tagline": "From Knowledge to Impact: Harnessing AI for Botswana's Growth",
    "description": "Join us for Botswana's premier AI conference, bringing together researchers, practitioners, and enthusiasts to explore the latest in artificial intelligence and its applications for national development.",
    "venue": "Botho University, Gaborone",
    "date_string": "June 30 - July 2, 2025"
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
        "day": "Day 1 - June 15",
        "events": [
            {"time": "08:30 - 09:10", "title": "Registration", "description": ""},
            {"time": "09:10 - 09:15", "title": "Welcome remarks", "description": ""},
            {"time": "09:15 - 10:15", "title": "Community Empowerment through Technology", "description": "Cultivating a Research Culture in Botswana"},
            {"time": "10:20 - 10:50", "title": "Catalyzing Innovation", "description": "Government Initiatives to Boost Technology Research in Botswana"},
            {"time": "10:55 - 11:15", "title": "Tea break", "description": ""},
            {"time": "11:15 - 11:45", "title": "Guest Presentation", "description": "Topic - Guest presentation"},
            {"time": "11:50 - 12:20", "title": "Exploring the Intersection of AI and Industry", "description": "Prospects and Hurdles for Researchers and Startups"},
            {"time": "12:25 - 12:45", "title": "Advancing Frontiers", "description": "The State of Artificial Intelligence in Botswana's Higher Education"},
            {"time": "12:45 - 13:00", "title": "Hackathon starts", "description": ""},
            {"time": "13:00 - 14:00", "title": "Lunch Break & Group Pics", "description": ""},
            {"time": "14:00 - 16:00", "title": "Poster Session", "description": ""},
            {"time": "16:05 - 16:15", "title": "AI in African Industries and Beyond", "description": "Bridging the Gap. Inspiring Data Science Enthusiasts Online: Becoming Heroes."},
            {"time": "16:20", "title": "Closing remarks", "description": ""}
        ]
    },
    {
        "day": "Day 2 - June 16",
        "events": [
            {"time": "08:30 - 09:10", "title": "Registration", "description": ""},
            {"time": "09:10 - 09:15", "title": "Welcome remarks", "description": ""},
            {"time": "09:15 - 10:15", "title": "Community Empowerment through Technology", "description": "Cultivating a Research Culture in Botswana"},
            {"time": "10:20 - 10:50", "title": "Catalyzing Innovation", "description": "Government Initiatives to Boost Technology Research in Botswana"},
            {"time": "10:55 - 11:15", "title": "Tea break", "description": ""},
            {"time": "11:15 - 11:45", "title": "Guest Presentation", "description": "Topic - Guest presentation"},
            {"time": "11:50 - 12:20", "title": "Exploring the Intersection of AI and Industry", "description": "Prospects and Hurdles for Researchers and Startups"},
            {"time": "12:25 - 12:45", "title": "Advancing Frontiers", "description": "The State of Artificial Intelligence in Botswana's Higher Education"},
            {"time": "12:45 - 13:00", "title": "Hackathon continues", "description": ""},
            {"time": "13:00 - 14:00", "title": "Lunch Break & Group Pics", "description": ""},
            {"time": "14:00 - 16:00", "title": "Poster Session", "description": ""},
            {"time": "16:05 - 16:15", "title": "AI in African Industries and Beyond", "description": "Bridging the Gap. Inspiring Data Science Enthusiasts Online: Becoming Heroes."},
            {"time": "16:20", "title": "Closing remarks", "description": ""}
        ]
    },
    {
        "day": "Day 3 - June 17",
        "events": [
            {"time": "08:30 - 09:10", "title": "Registration", "description": ""},
            {"time": "09:10 - 09:15", "title": "Welcome remarks", "description": ""},
            {"time": "09:15 - 10:15", "title": "Community Empowerment through Technology", "description": "Cultivating a Research Culture in Botswana"},
            {"time": "10:20 - 10:50", "title": "Catalyzing Innovation", "description": "Government Initiatives to Boost Technology Research in Botswana"},
            {"time": "10:55 - 11:15", "title": "Tea break", "description": ""},
            {"time": "11:15 - 11:45", "title": "Guest Presentation", "description": "Topic - Guest presentation"},
            {"time": "11:50 - 12:20", "title": "Exploring the Intersection of AI and Industry", "description": "Prospects and Hurdles for Researchers and Startups"},
            {"time": "12:25 - 12:45", "title": "Advancing Frontiers", "description": "The State of Artificial Intelligence in Botswana's Higher Education"},
            {"time": "12:45 - 13:00", "title": "Hackathon Finals", "description": "Presentation of solutions"},
            {"time": "13:00 - 14:00", "title": "Lunch Break & Group Pics", "description": ""},
            {"time": "14:00 - 16:00", "title": "Poster Session", "description": ""},
            {"time": "16:05 - 16:15", "title": "AI in African Industries and Beyond", "description": "Bridging the Gap. Inspiring Data Science Enthusiasts Online: Becoming Heroes."},
            {"time": "16:20", "title": "Closing Ceremony", "description": "Awards and closing remarks"}
        ]
    }
]

sponsors = [
    {"name": "Ministry of Tertiary Education", "level": "Platinum", "logo": "ministry_logo.png"},
    {"name": "Botswana Innovation Hub", "level": "Gold", "logo": "bih_logo.png"},
    {"name": "University of Botswana", "level": "Gold", "logo": "uob_logo.png"},
    {"name": "Orange Botswana", "level": "Silver", "logo": "orange_logo.png"},
    {"name": "Mascom", "level": "Silver", "logo": "mascom_logo.png"}
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
