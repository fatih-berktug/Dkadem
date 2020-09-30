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




# @login_required
def main(request):

    #
    # if not perm:
    #     logout(request)
    #     return redirect('accounts:login')
    # athlete = Athlete.objects.get(pk=pk)
    # belts_form = athlete.belts.all()
    # licenses_form = athlete.licenses.all()
    # user = User.objects.get(pk=athlete.user.pk)
    # person = Person.objects.get(pk=athlete.person.pk)
    # communication = Communication.objects.get(pk=athlete.communication.pk)
    # user_form = UserForm(request.POST or None, instance=user)
    # person_form = PersonForm(request.POST or None, instance=person)
    # communication_form = CommunicationForm(request.POST or None, instance=communication)
    # say=0
    # say=athlete.licenses.all().filter(status='Onaylandı').count()
    #

    # if request.method == 'POST':
    #
    #     if user_form.is_valid() and communication_form.is_valid() and person_form.is_valid():
    #         user = user_form.save(commit=False)
    #         print('user=', user.first_name)
    #         user.username = user_form.cleaned_data['email']
    #         user.first_name = user_form.cleaned_data['first_name'].upper()
    #         user.last_name = user_form.cleaned_data['last_name'].upper()
    #         user.email = user_form.cleaned_data['email']
    #         user.save()
    #         person_form.save()
    #         communication_form.save()
    #
    #
    #         messages.success(request, 'Sporcu Başarıyla Güncellenmiştir.')
    #         return redirect('sbs:update-athletes', pk=pk)
    #
    #     else:
    #
    #         messages.warning(request, 'Alanları Kontrol Ediniz')

    return render(request, 'tempate/Main.html')
                  # {'user_form': user_form, 'communication_form': communication_form,
                  #  'person_form': person_form, 'belts_form': belts_form, 'licenses_form': licenses_form,
                  #  'athlete': athlete,'say':say})