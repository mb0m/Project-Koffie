# Coffee Bean Collector – Stappenplan

Eindopdracht Keuzevak Django – Hogeschool Rotterdam

---

## Setup
- [x] 1. `base` app aanmaken (`python manage.py startapp base`)
- [x] 2. `base` toevoegen aan `INSTALLED_APPS` in `settings.py`
- [x] 3. `base.urls` includen in project `urls.py`

---

## Models (`base/models.py`)
- [ ] 4. `Profile` model schrijven (OneToOne naar User, city, date_of_birth, favorite_method)
- [ ] 5. `Bean` model schrijven (name, country_of_origin, harvest_season, approved, approved_by)
- [ ] 6. `Tasting` model schrijven (FK naar Bean, FK naar User, date, description)
- [ ] 7. `makemigrations` + `migrate` uitvoeren

---

## Admin (`base/admin.py`)
- [ ] 8. Alle 3 modellen registreren
- [ ] 9. Bean admin: unapproved bonen tonen + approve actie (zet approved=True + approved_by)
- [ ] 10. Tasting admin: alleen verwijderen toestaan (change permission verwijderen)
- [ ] 11. Superuser aanmaken met wachtwoord `admin`

---

## Auth – Registratie & Login
- [ ] 12. `urls.py` aanmaken in `base/`
- [ ] 13. Registratieformulier bouwen (extends UserCreationForm, + city/dob/method velden)
- [ ] 14. Register view bouwen (slaat user op + maakt Profile aan)
- [ ] 15. Django's ingebouwde `LoginView` en `LogoutView` gebruiken
- [ ] 16. Wachtwoord wijzigen met Django's `PasswordChangeView`
- [ ] 17. Templates maken: `register.html`, `login.html` — beide namen op de loginpagina vermelden

---

## Profiel
- [ ] 18. Profiel bewerken view + formulier (city, dob, favorite_method)
- [ ] 19. Eigen profielpagina (gebruikersinfo + eigen tastings)
- [ ] 20. Publiek profiel (read-only, bereikbaar via klik op naam in newsfeed)

---

## Bonen
- [ ] 21. "Boon toevoegen" formulier + view (opslaan met approved=False)
- [ ] 22. Boon detailpagina (naam, land, seizoen, aantal tastings, in-seizoen status)
- [ ] 23. "Direct tasting starten" knop op detailpagina (boon vooraf geselecteerd)

---

## Proefsessies (Tastings)
- [ ] 24. Tasting formulier (boon dropdown, datum, omschrijving)
- [ ] 25. Tasting aanmaken view + validatie: blokkeer zelfde boon+user+datum
- [ ] 26. "Mijn tastings" pagina (lijst met bewerk + verwijder knoppen)
- [ ] 27. Tasting bewerken view
- [ ] 28. Tasting verwijderen view (bevestigingspagina)

---

## Newsfeed
- [ ] 29. Newsfeed view (alle tastings, chronologisch aflopend)
- [ ] 30. In newsfeed template: gebruikersnaam als klikbare link naar publiek profiel

---

## Templates & Layout
- [ ] 31. `base.html` maken met navigatie (newsfeed, boon toevoegen, mijn tastings, profiel, uitloggen)
- [ ] 32. Consistente styling toepassen

---

## Eindcontrole
- [ ] 33. Admin kan bonen goedkeuren, tastings verwijderen, bonen direct goedgekeurd toevoegen
- [ ] 34. Gebruiker kan niet twee tastings van dezelfde boon op dezelfde dag plaatsen
- [ ] 35. Beide namen staan op de loginpagina
- [ ] 36. Alles pushen naar GitHub + `Krul-HR` uitnodigen
