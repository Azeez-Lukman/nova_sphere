from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
  return render(request, "nova_sphere/home.html")
def about(request):
  return render(request, "nova_sphere/about.html")
def contact(request):
  return render(request, "nova_sphere/contact.html")
def courses(request):
  course_lists = all_courses
  return render(request, "nova_sphere/courses.html", {
    "courses_list": course_lists
  })
def services(request):
  return render(request, "nova_sphere/services.html")
def faq(request):
  faq_list = list(all_faq.keys())
  return render(request, "nova_sphere/faq.html", {
    "faq_questions": faq_list
  })
def faq_by_number(request, faq_num):
  faq_keys = list(all_faq.keys())

  if faq_num > len(faq_keys) or faq_num <= 0:
    return HttpResponseNotFound('FAQ does not exist')
  question_text = faq_keys[faq_num - 1]
  redirect_path = reverse("faq_details", args=[question_text])
  return HttpResponseRedirect(redirect_path)
  


def faq_details(request, faq_details):
  try:
    faq_answer = all_faq[faq_details]
    return render(request, 'nova_sphere/faq_details.html', {
      "faq_value" : faq_answer,
      "faq_name" : faq_details
    })
  except:
    return HttpResponseNotFound('Not found')




# courses offered at Novasphere
all_courses = [
  "Python Programming",
  "Django Web Development",
  "HTML & CSS",
  "JavaScript Development",
  "React.js",
  "UI/UX Design",
  "Data Analysis",
  "Git & GitHub",
  "DMobile App Development",
  "Cybersecurity Fundamentals"
]

# frquently asked question and answer
all_faq = {
  "What courses do you offer?": "We offer web development, programmming, UI/UX design, data analysis, cybersecurity, and many more technology focused courses.",
  "Do ineed previous experirnce?" : "No. Most of our begunner courses require no proir programming experience.",
  "Are classes available online" : "Yes. We offer both physical classroom sesions and online learning options.",
  "Do students receive certificate?" : "Yes. Students who successfully complete their courses receive certificate of completion.",
  "Is mentorship included?" : "Yes. Every student receives mentorship and guidance throughout the learning process.",
}