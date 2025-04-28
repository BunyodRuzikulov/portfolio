Shaxsiy portfolio veb-saytim, mening loyihalarim, blog postlarim, rezyumem va aloqa ma'lumotlarimni namoyish qiladi. Sayt zamonaviy dizayn va foydalanuvchi uchun qulay interfeys bilan yaratilgan.
Xususiyatlar

Bosh sahifa: Loyihalar va blog postlarning qisqacha ko'rinishi.
Men haqimda: Shaxsiy ma'lumotlar va ko'nikmalar.
Portfolio: Bajarilgan loyihalarni namoyish qilish.
Blog: Maqolalar va yangiliklar.
Rezyume: Ish tajribasi, ta'lim va sertifikatlar (doira shaklidagi profil rasmi bilan).
Kontakt: Xabar yuborish formasi va aloqa ma'lumotlari.
Xizmatlar: Taklif qilinadigan xizmatlar ro'yxati.
Admin paneli: Kontentni boshqarish uchun Django admin interfeysi.

Texnologiyalar

Backend: Django 4.x, Python 3.8+
Frontend: HTML, CSS (zamonaviy dizayn, neon effektlar, animatsiyalar)
Ma'lumotlar bazasi: SQLite (ishlab chiqarish uchun PostgreSQL tavsiya qilinadi)
Kutubxonalar: Pillow (rasmlarni boshqarish), django-ckeditor (rich text editor)
Statik fayllar: Tailwind CSS (ixtiyoriy, agar ishlatilgan bo'lsa)

O'rnatish
Loyihani mahalliy kompyuteringizda ishga tushirish uchun quyidagi qadamlarni bajaring:

Repozitoriyni klonlash:
git clone https://github.com/your-username/.git
cd 


Virtual muhitni sozlash:
python -m venv venv
 Windows uchun: venv\Scripts\activate


Kerakli kutubxonalarni o'rnatish:
pip install -r requirements.txt


Migratsiyalarni qo'llash:
python manage.py makemigrations
python manage.py migrate


Superuser yaratish (admin paneli uchun):
python manage.py createsuperuser

Serverni ishga tushirish:
python manage.py runserver


Brauzerda http://127.0.0.1:8000 manziliga o'ting. Admin paneliga http://127.0.0.1:8000/admin orqali kiring.


Foydalanish

Admin paneli: Loyihalar, blog postlar, ko'nikmalar, rezyume va profil rasmini qo'shish/o'zgartirish uchun.
Profil rasmi: media/profile/ papkasiga yuklanadi yoki static/images/profile.jpg sifatida ishlatiladi.
Rezyume: Ish tajribasi, ta'lim va sertifikatlar dinamik ravishda ma'lumotlar bazasidan olinadi.

Loyiha tuzilishi
bunyod-portfolio/
├── core/                   # Asosiy ilova
│   ├── migrations/         # Migratsiya fayllari
│   ├── static/            # CSS, JS va rasm fayllari
│   ├── templates/         # HTML shablonlar
│   ├── models.py          # Ma'lumotlar bazasi modellari
│   ├── views.py           # View funksiyalari
│   └── urls.py            # URL yo'nalishlari
├── media/                 # Yuklangan fayllar (profil rasmi va boshqalar)
├── personal_website/      # Loyiha sozlamalari
│   ├── settings.py        # Django sozlamalari
│   └── urls.py            # Asosiy URL'lar
├── requirements.txt       # Kerakli kutubxonalar
└── README.md              # Ushbu fayl

![image](https://github.com/user-attachments/assets/61944a08-c524-4f40-b00e-4e8707c2fe8d)


Hissalar
Loyihaga hissa qo'shmoqchi bo'lsangiz:

Repozitoriyni fork qiling.
Yangi branch yarating (git checkout -b feature/your-feature).
O'zgartirishlaringizni commit qiling (git commit -m 'Add your feature').
Branch’ni push qiling (git push origin feature/your-feature).
Pull request oching.

Aloqa
Telegram: https://t.me/Bunyod_Ruziqulov

