from rest_framework import viewsets, status
from notes_app.models import Note
from rest_framework.response import Response
from .serializers import NoteSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def destroy(self, request, *args, **kwargs):
        note = self.get_object()
        note.delete()
        return Response(
            {"message": "Note wurde erfolgreich gelöscht."},
            status=status.HTTP_204_NO_CONTENT
        )