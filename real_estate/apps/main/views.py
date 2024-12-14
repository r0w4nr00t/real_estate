from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404

class Healthz(APIView):
    def get(self, request): 
        return Response({'state':'ready'})

