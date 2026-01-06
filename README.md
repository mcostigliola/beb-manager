# Domus Bauli — B&B Manager

Landing page moderna in stile Airbnb e accesso account per un B&B a Bacoli. Realizzato con Django e Tailwind via CDN, con asset statici locali per un caricamento affidabile.

## Funzionalità
- Hero con immagini di sfondo a rotazione e parallax leggero
- Palette, tipografia e layout ispirati ad Airbnb
- Pagine di login e registrazione
- Asset statici locali (logo + immagini di Bacoli)

## Stack tecnologico
- Django
- Tailwind CSS (CDN)
- SQLite (predefinito)

## Struttura del progetto
- `config/` — impostazioni Django e URL
- `core/` — home page
- `accounts/` — viste di login e registrazione
- `templates/` — template base e pagine
- `static/` — logo e immagini di Bacoli

## Setup
1) Crea e attiva un virtual environment
2) Installa le dipendenze

```bash
pip install Django
```

3) Esegui le migrazioni e avvia il server

```bash
python manage.py migrate
python manage.py runserver
```

Apri `http://127.0.0.1:8000/`.

## Rotte
- Home: `/`
- Login: `/accounts/login/`
- Registrazione: `/accounts/register/`

## Note
- Tailwind e i font sono caricati via CDN (serve internet al primo caricamento).
- Le immagini dell’hero sono locali in `static/images/bacoli/`.

## Deployment
- Imposta `DEBUG=False` e configura `ALLOWED_HOSTS`.
- Servi i file statici con un web server (es. Nginx) o con lo static handler della piattaforma.
- Configura un database di produzione (consigliato PostgreSQL).
- Imposta i valori sensibili via variabili d’ambiente (es. `SECRET_KEY`).

## Contributi
1) Crea un branch feature da `main`.
2) Mantieni le modifiche focalizzate e per singola PR.
3) Esegui le migrazioni se cambi i modelli.
4) Usa messaggi di commit chiari.

## Licenza
Progetto privato.
