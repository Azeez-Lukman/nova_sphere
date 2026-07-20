# 🎓 NovaSphere Tech Academy

A beginner-friendly Django project that demonstrates **URL routing**, **template inheritance**, **dynamic content rendering**, and **responsive web design** without using a database.

---

## 📖 About the Project

NovaSphere Tech Academy is a fictional technology training institution created as a foundation-level Django project.

The goal of this project is to practice Django fundamentals by building a professional multi-page website using:

- URL Routing
- Function-Based Views
- Template Rendering
- Template Inheritance
- Dynamic Data
- Static Files
- Responsive Design

This project intentionally avoids databases and authentication so learners can focus on mastering Django's core concepts first.

---

## 🌟 Features

- 🏠 Home Page
- ℹ️ About Us Page
- 📚 Courses Page
- 💼 Services Page
- ❓ FAQ Page
- 📄 Dynamic FAQ Detail Page
- 📞 Contact Page
- 📱 Fully Responsive Design
- 🎨 Modern UI
- ⚡ Reusable Templates

---

## 🛠 Technologies Used

### Backend

- Python
- Django

### Frontend

- HTML5
- Tailwind CSS
- JavaScript

### Tools

- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```
NovaSphere/
│
├── academy/
│   ├── static/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── courses.html
│   │   ├── services.html
│   │   ├── faq.html
│   │   ├── faq-detail.html
│   │   └── contact.html
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── NovaSphere/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
└── README.md
```

---

# 📄 Website Pages

## 🏠 Home

The homepage welcomes visitors to NovaSphere Tech Academy with a professional hero section, academy overview, reasons to choose the academy, and a call-to-action encouraging prospective students to begin their learning journey.

---

## ℹ️ About

The About page introduces NovaSphere Tech Academy, explaining its mission, vision, and core values while highlighting its commitment to practical, career-focused technology education.

---

## 📚 Courses

The Courses page showcases the academy's technology programs, including:

- Python Programming
- Django Web Development
- HTML & CSS
- JavaScript Development
- React.js
- UI/UX Design
- Data Analysis
- Git & GitHub
- Mobile App Development
- Cybersecurity Fundamentals

---

## 💼 Services

Students and organizations can explore services such as:

- Professional Training
- One-on-One Mentorship
- Workshops & Bootcamps
- Career Support
- Corporate Training

---

## ❓ Frequently Asked Questions

The FAQ page answers common questions regarding:

- Available courses
- Beginner requirements
- Online classes
- Certificates
- Mentorship

---

## 📄 Dynamic FAQ Detail

Each FAQ links to a dedicated page that displays the selected question and answer dynamically using Django views.

Example URL:

```
/faq/1
```

Example context:

```python
{
    "question": {
        "title": "What courses do you offer?",
        "answer": "We provide comprehensive training in Python, Django, JavaScript, React, UI/UX Design, Data Analysis, Cybersecurity, and many other in-demand technology skills."
    }
}
```

---

## 📞 Contact

The Contact page provides visitors with:

- Phone Number
- Email Address
- Office Address
- Office Hours

making it easy for prospective students to reach the academy.

---

## 🎯 Learning Outcomes

By completing this project, you'll gain hands-on experience with:

- Creating Django projects and apps
- URL configuration
- Function-based views
- Rendering templates
- Passing data from views to templates
- Template inheritance
- Static files
- Dynamic URL parameters
- Building responsive multi-page websites

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/novasphere-tech-academy.git
```

### 2. Navigate to the Project

```bash
cd novasphere-tech-academy
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 5. Install Django

```bash
pip install django
```

Or install all dependencies:

```bash
pip install -r requirements.txt
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

Add screenshots of your completed project here.

```
screenshots/
├── home.png
├── about.png
├── courses.png
├── services.png
├── faq.png
└── contact.png
```

---

## 🚀 Future Improvements

Possible enhancements include:

- Student Registration
- User Authentication
- Database Integration
- Contact Form Backend
- Course Detail Pages
- Instructor Profiles
- Blog Section
- Search Functionality
- Student Dashboard
- Online Enrollment

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 👨‍💻 Author

**Lukman Azeez**

Frontend Developer • Django Developer

GitHub: https://github.com/Azeez-Lukman

---

## 📄 License

This project is licensed under the MIT License.

---

### ⭐ If you found this project helpful, consider giving it a star on GitHub!