import asyncio
import multiprocessing
import threading
import time

from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from . import globals

globals.initialize()

def index(request):
    return render(request, 'web_page.html', globals.data)
