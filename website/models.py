from django.db import models

class TeamMember(models.Model):
    CLUB_CHOICES = [
        ('amrc', 'AMRC'),
        ('amrc_jr', 'AMRC Jr'),
        ('amag', 'AMAG'),
        ('amag_jr', 'AMAG Jr'),
        ('amo2', 'AMO2'),
        ('kasparov', 'Kasparov'),
        ('inquiry', 'Inquiry'),
        ('anachronism', 'Anachronism'),
    ]
    
    ROLE_CHOICES = [
        ('head', 'Head'),
        ('board', 'Board'),
    ]
    
    BRANCH_CHOICES = [
        ('def', 'Default'),
        ('amb', 'Barsha'),
        ('amg', 'Garhoud'),
        ('amk', 'Khawaneej'),
    ]
    
    name = models.CharField(max_length=100)
    pfp = models.ImageField(upload_to='Teams/')
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)
    club = models.CharField(max_length=20, choices=CLUB_CHOICES)
    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES, default='def')
    
    def __str__(self):
        return self.name
    
class ClubAbout(models.Model):
    CLUB_CHOICES = [
        ('amrc', 'AMRC'),
        ('amrc_jr', 'AMRC Jr'),
        ('amag', 'AMAG'),
        ('amag_jr', 'AMAG Jr'),
        ('amo2', 'AMO2'),
        ('kasparov', 'Kasparov'),
        ('inquiry', 'Inquiry'),
        ('anachronism', 'Anachronism'),
        ('brics', 'Brics'),
        ('gymrats', 'Gym Rats'),
    ]
    
    club = models.CharField(max_length=20, choices=CLUB_CHOICES, unique=True)
    logo = models.ImageField(upload_to='club_logos/', blank=True)
    about_text = models.TextField()

    def __str__(self):
        return self.club


class ClubPhoto(models.Model):
    club = models.ForeignKey(ClubAbout, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='club_photos/')

    def __str__(self):
        return f"Photo for {self.club.club}"

class Book(models.Model):
    CLUB_CHOICES = [
        ('amrc', 'AMRC'),
        ('amrc_jr', 'AMRC Jr'),
        ('amo2', 'AMO2'),
    ]

    title = models.CharField(max_length=100)
    club = models.CharField(max_length=20, choices=CLUB_CHOICES)
    url = models.URLField(max_length=200, blank=True)
    