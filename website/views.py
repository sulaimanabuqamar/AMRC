from .models import TeamMember, ClubAbout
from django.shortcuts import get_list_or_404, render, get_object_or_404
from .models import Book

# Home view
def Home(request):
    return render(request, "Home.html")

# AMRC views
def AMRC_About(request):
    about = get_object_or_404(ClubAbout, club='amrc')
    return render(request, "AMRC/About.html", {'about': about})

def AMRC_Team(request):
    heads = TeamMember.objects.filter(club='amrc', role='head')
    board = TeamMember.objects.filter(club='amrc', role='board')
    return render(request, "AMRC/Team.html", {'heads': heads, 'board': board})

# AMRC Jr views
def AMRC_Jr_About(request):
    about = get_object_or_404(ClubAbout, club='amrc_jr')
    return render(request, "AMRC Jr/About.html", {'about': about})

def AMRC_Jr_Team(request):
    heads = TeamMember.objects.filter(club='amrc_jr', role='head')
    return render(request, "AMRC Jr/Team.html", {'heads': heads})

def AMRC_Jr_Kasaporov(request):
    about = get_object_or_404(ClubAbout, club='kasaporov')
    heads = TeamMember.objects.filter(club='kasaporov', role='head')
    return render(request, "AMRC Jr/Kasaporov.html", {'about': about, 'heads': heads})

def AMRC_Jr_Inquiry(request):
    about = get_object_or_404(ClubAbout, club='inquiry')
    heads = TeamMember.objects.filter(club='inquiry', role='head')
    return render(request, "AMRC Jr/Inquiry.html", {'about': about, 'heads': heads})

def AMRC_Jr_Anachronism(request):
    about = get_object_or_404(ClubAbout, club='anachronism')
    heads = TeamMember.objects.filter(club='anachronism', role='head')
    return render(request, "AMRC Jr/Anachronism.html", {'about': about, 'heads': heads})

# AMAG views
def AMAG_About(request):
    about = get_object_or_404(ClubAbout, club='amag')
    return render(request, "AMAG/About.html", {'about': about})

def AMAG_Team(request):
    heads = TeamMember.objects.filter(club='amag', role='head')
    return render(request, "AMAG/Team.html", {'heads': heads})

def AMAG_Brics(request):
    about = get_object_or_404(ClubAbout, club='brics')
    return render(request, "AMAG/Brics.html", {'about': about})

# AMAG Jr views
def AMAG_Jr_About(request):
    about = get_object_or_404(ClubAbout, club='amag_jr')
    return render(request, "AMAG Jr/About.html", {'about': about})

def AMAG_Jr_Team(request):
    heads = TeamMember.objects.filter(club='amag_jr', role='head')
    return render(request, "AMAG Jr/Team.html", {'heads': heads})

# AMO2 views
def AMO2_About(request):
    about = get_object_or_404(ClubAbout, club='amo2')
    return render(request, "AMO2/About.html", {'about': about})

def AMO2_Team(request):
    heads = TeamMember.objects.filter(club='amo2', role='head')
    return render(request, "AMO2/Team.html", {'heads': heads})

# Projects views
def Projects_GymRats(request):
    about = get_object_or_404(ClubAbout, club='gymrats')
    return render(request, "Projects/GymRats.html", {'about': about})

# Archives views

def Archives(request):
    return render(request, "Archives.html")

def Books(request, club_type):
    books = get_list_or_404(Book, club=club_type)  
    return render(request, "Books.html", {"books": books, "club_type": club_type})