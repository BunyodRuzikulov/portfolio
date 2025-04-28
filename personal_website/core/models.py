from django.db import models
from ckeditor.fields import RichTextField

# Oldingi modellar (Project, BlogPost, ContactMessage, Service)
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    excerpt = models.TextField(max_length=300)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Rezyume uchun modellar
class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(help_text="Foiz sifatida, 0-100 oralig'ida")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ko'nikma"
        verbose_name_plural = "Ko'nikmalar"

class WorkExperience(models.Model):
    title = models.CharField(max_length=200, help_text="Lavozim nomi, masalan: Veb-dasturchi")
    company = models.CharField(max_length=200, help_text="Kompaniya nomi")
    start_date = models.CharField(max_length=50, help_text="Boshlanish sanasi, masalan: 2020-yil")
    end_date = models.CharField(max_length=50, blank=True, help_text="Tugash sanasi, bo'sh qoldirilsa 'Hozirgacha' ko'rsatiladi")
    description = models.TextField(help_text="Ish tavsifi")

    def __str__(self):
        return f"{self.title} - {self.company}"

    class Meta:
        verbose_name = "Ish tajribasi"
        verbose_name_plural = "Ish tajribalari"

class Education(models.Model):
    degree = models.CharField(max_length=200, help_text="Daraja, masalan: Bakalavr")
    institution = models.CharField(max_length=200, help_text="Ta'lim muassasasi nomi")
    start_date = models.CharField(max_length=50, help_text="Boshlanish sanasi, masalan: 2016-yil")
    end_date = models.CharField(max_length=50, blank=True, help_text="Tugash sanasi, bo'sh qoldirilsa 'Hozirgacha' ko'rsatiladi")
    description = models.TextField(blank=True, help_text="Qo'shimcha ma'lumotlar")

    def __str__(self):
        return f"{self.degree} - {self.institution}"

    class Meta:
        verbose_name = "Ta'lim"
        verbose_name_plural = "Ta'limlar"

class Certificate(models.Model):
    title = models.CharField(max_length=200, help_text="Sertifikat nomi")
    issuer = models.CharField(max_length=200, help_text="Beruvchi tashkilot")
    issue_date = models.CharField(max_length=50, help_text="Berilgan sana, masalan: 2023-yil")
    description = models.TextField(blank=True, help_text="Qo'shimcha ma'lumotlar")

    def __str__(self):
        return f"{self.title} - {self.issuer}"

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"


class Profile(models.Model):
    image = models.ImageField(upload_to='profile/', help_text="Profil rasmi (kvadrat shaklda, masalan, 150x150px)")

    def __str__(self):
        return "Profil rasmi"

    class Meta:
        verbose_name = "Profil rasmi"
        verbose_name_plural = "Profil rasmlari"