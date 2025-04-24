from notes_app.models import Note

Note.objects.create(
    title='Willkommen',
    content='Das ist deine erste Notiz!',
    marked=False,
    trash=False
)

Note.objects.create(
    title='Alte Idee',
    content='Diese Notiz wurde gelöscht.',
    marked=True,
    trash=False
)

print("populate.py wurde ausgeführt!")
