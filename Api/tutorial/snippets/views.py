from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import renderers
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework import permissions
class SnippetViewSet(viewsets.ModelViewSet):
   queryset = Snippet.objects.all()
   serializer_class = SnippetSerializer
   permission_classes = [permissions.IsAuthenticatedOrReadOnly,
   IsOwnerOrReadOnly]
@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
def highlight(self, request, *args, **kwargs):
   snippet = self.get_object()
   return Response(snippet.highlighted)
def perform_create(self, serializer):
   serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
 queryset = User.objects.all()
 serializer_class = UserSerializer



