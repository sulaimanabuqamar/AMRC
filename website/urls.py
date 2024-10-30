from django.urls import path
from website import views

urlpatterns = [
    # Home
    path("", views.Home, name="home"),
    
    # AMRC URLs
    path("AMRC/About/", views.AMRC_About, name="amrc_about"),
    path("AMRC/Team/Barsha", views.AMRC_Team_Barsha, name="amrc_team_barsha"),
    path("AMRC/Team/Garhoud", views.AMRC_Team_Garhoud, name="amrc_team_garhoud"),
    path("AMRC/Team/Khawaneej", views.AMRC_Team_Khawaneej, name="amrc_team_khawaneej"),
    
    # AMRC Jr URLs
    path("AMRC/Jr/About/", views.AMRC_Jr_About, name="amrc_jr_about"),
    path("AMRC/Jr/Team/", views.AMRC_Jr_Team, name="amrc_jr_team"),
    path("AMRC/Jr/Kasparov/", views.AMRC_Jr_Kasparov, name="amrc_jr_kasparov"),
    path("AMRC/Jr/Inquiry/", views.AMRC_Jr_Inquiry, name="amrc_jr_inquiry"),
    path("AMRC/Jr/Anachronism/", views.AMRC_Jr_Anachronism, name="amrc_jr_anachronism"),

    # AMAG URLs
    path("AMAG/About/", views.AMAG_About, name="amag_about"),
    path("AMAG/Team/", views.AMAG_Team, name="amag_team"),
    path("AMAG/Brics/", views.AMAG_Brics, name="amag_brics"),

    # AMAG Jr URLs
    path("AMAG/Jr/About/", views.AMAG_Jr_About, name="amag_jr_about"),
    path("AMAG/Jr/Team/", views.AMAG_Jr_Team, name="amag_jr_team"),

    # AMO2 URLs
    path("AMO2/About/", views.AMO2_About, name="amo2_about"),
    path("AMO2/Team/", views.AMO2_Team, name="amo2_team"),

    # Projects URLs
    path("Projects/GymRats/", views.Projects_GymRats, name="projects_gymrats"),
    
    # Archives URLs
    path("Archives/", views.Archives, name="archives"),
    path("Archives/<str:club_type>/", views.Books, name="books"),

]