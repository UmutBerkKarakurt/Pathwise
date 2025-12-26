from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "core/home.html")


def ace(request):
    return render(request, "core/ace.html")


def dashboard(request):
    cohorts = [
        {
            "name": "1st Year",
            "path": "",
            "gpa": "3.24",
            "attendance": "94%",
            "success": "87%",
            "progress": 35,
        },
        {
            "name": "2nd Year",
            "path": "200-level Path",
            "gpa": "3.18",
            "attendance": "92%",
            "success": "83%",
            "progress": 50,
        },
        {
            "name": "3rd Year",
            "path": "300-level Path",
            "gpa": "N/A (ongoing)",
            "attendance": "88%",
            "success": "N/A",
            "progress": 70,
        },
        {
            "name": "4th Year",
            "path": "400-level Path",
            "gpa": "N/A",
            "attendance": "N/A",
            "success": "N/A",
            "progress": 0,
        },
    ]

    attendance_trend = [
        {"label": "Laboratories", "delta": "+3.2%", "spark": "spark-1"},
        {"label": "Core lectures", "delta": "+1.4%", "spark": "spark-2"},
        {"label": "Project reviews", "delta": "-0.8%", "spark": "spark-3"},
    ]

    upcoming_milestones = [
        {"title": "Data Analysis assignment", "time": "Week 6"},
        {"title": "Group Project presentation", "time": "Week 9"},
        {"title": "Vocabulary quiz", "time": "Week 12"},
    ]

    context = {
        "cohorts": cohorts,
        "attendance_trend": attendance_trend,
        "upcoming_milestones": upcoming_milestones,
    }

    return render(request, "core/dashboard.html", context)


def courses(request):
    courses_data = [
        {"code": "CSE 331", "title": "Exploratory Data Analysis", "los": ["1", "3", "5"], "credits": 3},
        {"code": "CSE 321", "title": "Data Systems", "los": ["2", "4", "6"], "credits": 3},
        {"code": "CSE 311", "title": "Software", "los": ["3", "7"], "credits": 3},
        {"code": "CSE 301", "title": "Computer Architecture", "los": ["2", "5", "8"], "credits": 3},
        {"code": "ACU 216", "title": "Advanced English", "los": ["9"], "credits": 2},
        {"code": "ATA 101", "title": "Atatürk İlkeleri ve İnkılap Tarihi", "los": ["7"], "credits": 2},
    ]

    learning_outcomes = [
        {"code": "LO1", "description": "Model computing problems with mathematical rigor."},
        {"code": "LO3", "description": "Design efficient algorithms under resource constraints."},
        {"code": "LO5", "description": "Integrate hardware/software for embedded solutions."},
        {"code": "LO8", "description": "Lead collaborative software projects with modern tooling."},
    ]

    context = {
        "courses": courses_data,
        "learning_outcomes": learning_outcomes,
    }

    return render(request, "core/courses.html", context)


def outcomes(request):
    program_outcomes = [
        {"code": "PO1", "text": "Foundations in math & science"},
        {"code": "PO2", "text": "Systems analysis & design"},
        {"code": "PO3", "text": "Ethics & professional responsibility"},
        {"code": "PO4", "text": "Communication and teamwork"},
        {"code": "PO5", "text": "Lifelong learning and development"},
    ]

    mapping = [
        {"lo": "LO1", "values": [1, 0, 1, 1, 0]},
        {"lo": "LO2", "values": [0, 1, 1, 0, 1]},
        {"lo": "LO3", "values": [1, 1, 0, 0, 1]},
        {"lo": "LO4", "values": [0, 0, 1, 1, 1]},
        {"lo": "LO5", "values": [1, 0, 0, 1, 0]},
    ]

    actions = [
        "Yeni Embedded Systems lab rubriğini PO3 ile uyumlu olacak şekilde güncelliyoruz.",
        "Etik vaka çalışmalarını PO4 için tekrar gözden geçiriyoruz.",
        "Bitirme projesi için PO5 kapsamındaki hedefleri netleştirip paylaşıyoruz.",
    ]

    po_headers = ["PO1", "PO2", "PO3", "PO4", "PO5"]

    context = {
        "program_outcomes": program_outcomes,
        "mapping": mapping,
        "actions": actions,
        "po_headers": po_headers,
    }

    return render(request, "core/outcomes.html", context)


def students(request):
    student_profile = {
        "name": "Sude Atacan",
        "summary": "3rd year · Computer Engineering student",
        "gpa": "3.42",
        "attendance": "92%",
        "credits": 96,
    }

    current_courses = [
        {"title": "CSE 331 · Exploratory Data Analysis", "grade": "AA", "attendance": "95%"},
        {"title": "CSE 321 · Data Systems", "grade": "BA", "attendance": "90%"},
        {"title": "CSE 311 · Software", "grade": "AA", "attendance": "95%"},
        {"title": "CSE 301 · Computer Architecture", "grade": "BB", "attendance": "80%"},
        {"title": "ACU 216 · Advanced English", "grade": "BB", "attendance": "85%"},
        {"title": "ATA 101 · Atatürk İlkeleri ve İnkılap Tarihi", "grade": "AA", "attendance": "90%"},
    ]

    attendance_summary = [
        {"label": "Lectures", "value": "96%", "spark": "spark-2"},
        {"label": "Laboratories", "value": "91%", "spark": "spark-1"},
        {"label": "Project reviews", "value": "88%", "spark": "spark-3"},
    ]

    advisor_notes = [
        "Schedule systems lab observation · Week 7",
        "Share ethics case feedback · Week 8",
        "Review internship proposal · Week 10",
    ]

    timeline = [
        {"title": "Capstone sprint demo", "meta": "Scored 4.6 / 5 rubric · Feb 12"},
        {"title": "Industry mentor session", "meta": "Focus on embedded safety · Feb 6"},
        {"title": "Attendance alert cleared", "meta": "Recovered to 92% · Jan 24"},
    ]

    context = {
        "student": student_profile,
        "current_courses": current_courses,
        "attendance_summary": attendance_summary,
        "advisor_notes": advisor_notes,
        "timeline": timeline,
    }

    return render(request, "core/students.html", context)


def software(request):
    return render(request, "core/lectures/software.html")


