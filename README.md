# ☕ Coffee Bean Collector

Een Django-webapplicatie waarmee koffieliefhebbers hun koffieproefnotities (tastings) kunnen bijhouden, bonen kunnen toevoegen en een community-newsfeed kunnen raadplegen.

Gebouwd als eindopdracht voor het keuzevak Django aan de Hogeschool Rotterdam.

---

## Technologieën

- Python 3 / Django
- SQLite (lokale database)
- HTML, CSS
- Django Admin

---

## Functionaliteiten

- Gebruikersregistratie en -login
- Profielpagina (bewerkbaar)
- Bonen toevoegen en goedkeuren via admin
- Proefsessies (tastings) aanmaken, bewerken en verwijderen
- Newsfeed met alle tastings
- Publieke profielpagina's

---

## Installatie

```bash
git clone https://github.com/mb0m/Project-Koffie.git
cd Project-Koffie
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Opmerkingen

**Wachtwoord & authenticatie:** De superuser maakt gebruik van een eenvoudig wachtwoord (`admin`). Dit is op expliciete instructie van de docent zo opgezet voor testdoeleinden.

**Minimale uitwerking:** Het project voldoet aan de minimale projectvereisten. Verdere uitbreiding was niet toegestaan binnen de opdrachtkaders.

**Beperkt aantal commits:** Het project is grotendeels lokaal ontwikkeld. Door het uitvallen van mijn projectpartner heeft de docent toestemming gegeven om het lokaal te werken in plaats van via GitHub. Hierdoor is de commit-geschiedenis niet representatief voor de daadwerkelijk geleverde inspanning.

---

## Auteur

[mb0m](https://github.com/mb0m) — Hogeschool Rotterdam, Informatica
