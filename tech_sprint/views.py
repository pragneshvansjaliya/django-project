from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import routers, serializers, viewsets
from newsapi import NewsApiClient
# Create your views here.


@api_view(['GET', 'POST'])
def dashboard(request, *args, **kwargs):    
    newsapi = NewsApiClient(api_key='8d3f042c3715480e8737a046721b64db')

    if request.method == 'GET':
        snippets = newsapi.get_sources()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    # return render(request, "tech_sprint/index.html",sources)