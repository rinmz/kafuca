# kafuca

A small Django blog: publish entries and let visitors comment on them.

## Features

- Entries with automatic slug URLs (`/<slug>/`)
- Comments on each entry
- Admin interface for managing content

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/. Create entries at `/admin/`.

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `DJANGO_SECRET_KEY` | random per start | Set this in production |
| `DJANGO_DEBUG` | `1` | Set to `0` in production |

## License

MIT
