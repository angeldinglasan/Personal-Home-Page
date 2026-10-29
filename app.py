from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = "any-secret-words-you-like"

your_gmail = "angelcamatadinglasan@gmail.com"
app_password = "PUT-YOUR-16-LETTER-APP-PASSWORD-HERE"

logo = "AD"
full_name = "Angel Dinglasan"
tag_text = "Open to Work · Hire Me"
greeting = "Hello world, I'm"
display_name = "Angel Dinglasan"
hero_text = "BS Information Technology student majoring in Service Management at Batangas State University – Lipa. An aspiring customer service professional who enjoys helping people and solving their concerns with patience and care."

about_text = "I am a <strong>BS Information Technology</strong> student majoring in <strong>Service Management</strong> at Batangas State University The NEU – Lipa Campus. I am interested in customer service and helping customers with their questions and concerns. I have developed communication, teamwork, and problem-solving skills through school projects and activities. I am willing to learn, adapt, and gain more experience in the customer service field."
about_chips = ["Customer Service", "Communication", "Problem-Solving", "Teamwork"]
location = "Lipa City, Batangas"

# Icon 
clock_icon = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
layers_icon = '<path d="M12 3 3 8l9 5 9-5-9-5Z"/><path d="m3 12 9 5 9-5"/><path d="m3 16 9 5 9-5"/>'
arrows_icon = '<path d="M20 11a8 8 0 0 0-14.9-3M4 4v4h4"/><path d="M4 13a8 8 0 0 0 14.9 3M20 20v-4h-4"/>'
book_icon = '<path d="M3 5.5A1.5 1.5 0 0 1 4.5 4H11v15H4.5A1.5 1.5 0 0 0 3 20.5v-15Z"/><path d="M21 5.5A1.5 1.5 0 0 0 19.5 4H13v15h6.5a1.5 1.5 0 0 1 1.5 1.5v-15Z"/>'
people_icon = '<circle cx="9" cy="8" r="3.2"/><path d="M3 20v-1a5 5 0 0 1 5-5h2a5 5 0 0 1 5 5v1"/><path d="M16 4.8a3.2 3.2 0 0 1 0 6.4"/><path d="M18 14.3a5 5 0 0 1 3 4.7v1"/>'

skills = [
    {"name": "Time Management", "icon": clock_icon},
    {"name": "Multitasking", "icon": layers_icon},
    {"name": "Adaptability", "icon": arrows_icon},
    {"name": "Willingness to Learn", "icon": book_icon},
    {"name": "Teamwork", "icon": people_icon},
]

projects = [
    {
        "title": "UNICONNECT: A Unified Organizational Management System for Batangas State University – Lipa Campus",
        "text": "An academic project focused on developing a web-based organizational management system for campus organizations. The system is designed to consolidate all organizations in one place to organize information, membership records, announcements, and events. Through this project, I developed teamwork, communication, and problem-solving skills.",
        "tags": ["Teamwork", "Communication", "Problem-Solving"],
    },
    {
        "title": "REBASE: Resilient & Environmental Barangay Assistance for Sustainability and Emergencies",
        "text": "A web-based system created to support the residents of Brgy. Namunga, Rosario, Batangas in addressing frequent environmental hazards caused by natural disasters and poor settlement management. It provides a simple, user-friendly platform where community members can instantly file real-time reports, while local officials can efficiently organize and monitor these submissions. By turning residents into active partners in disaster management, REBASE helps build a safer and more resilient community.",
        "tags": ["Web-Based System", "Community Service", "Disaster Management"],
    },
]

edu_degree = "Bachelor of Science in Information Technology"
edu_major = "Major in Service Management"
edu_school = "Batangas State University – The National Engineering University – Lipa Campus"

cert_names = [
    "CCNA: Introduction to Networks",
    "CCNA: Switching, Routing, and Wireless Essentials",
]
cert_from = "Cisco Networking Academy"

exp_title = "Avon Sales Representative"
exp_place = "Lipa Branch · 2023 – 2024"
exp_text = "Dealt directly with customers, built relationships, and handled their questions and orders."

footer_text = "© 2026 Angel Dinglasan. Built while learning."

@app.route("/")
def home():
    return render_template(
        "index.html",
        logo=logo,
        full_name=full_name,
        tag_text=tag_text,
        greeting=greeting,
        display_name=display_name,
        hero_text=hero_text,
        about_text=about_text,
        about_chips=about_chips,
        location=location,
        skills=skills,
        projects=projects,
        edu_degree=edu_degree,
        edu_major=edu_major,
        edu_school=edu_school,
        cert_names=cert_names,
        cert_from=cert_from,
        exp_title=exp_title,
        exp_place=exp_place,
        exp_text=exp_text,
        email=your_gmail,
        footer_text=footer_text,
    )

@app.route("/send", methods=["POST"])
def send():
    visitor_name = request.form["name"]
    visitor_email = request.form["email"]
    visitor_message = request.form["message"]

    msg = EmailMessage()
    msg["Subject"] = "New message from " + visitor_name + " (Hire Me page)"
    msg["From"] = your_gmail
    msg["To"] = your_gmail
    msg["Reply-To"] = visitor_email
    msg.set_content(
        "Name: " + visitor_name + "\n"
        "Email: " + visitor_email + "\n\n"
        "Message:\n" + visitor_message
    )

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(your_gmail, app_password)
        server.send_message(msg)
        server.quit()
        flash("Thank you! Your message was sent.")
    except Exception as error:
        print("Email error:", error)
        flash("Sorry, the message was not sent. Please try again.")

    return redirect("/#contact")

if __name__ == "__main__":
    app.run(debug=True)