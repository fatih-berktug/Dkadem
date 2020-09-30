from builtins import print, set, property, int
from datetime import timedelta, datetime
from operator import attrgetter
from os import name

from django.db.models.functions import Lower

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect


def main(request):
    print('Hello Word ')
    return render(request, 'Main.html')
                  # {'user_form': user_form, 'communication_form': communication_form,
                  #  'person_form': person_form, 'belts_form': belts_form, 'licenses_form': licenses_form,
                  #  'athlete': athlete,'say':say})