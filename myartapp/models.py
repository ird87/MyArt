from django.db import models
from django.core.validators import MinLengthValidator


class CulturalCenter(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, validators=[MinLengthValidator(1)])
    repertoire_url = models.URLField(blank=True)
    poster_url = models.URLField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    image_url = models.URLField(blank=True)


class RepertoireEvent(models.Model):
    cultural_center = models.ForeignKey(CulturalCenter, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=200, unique=True, blank=False, validators=[MinLengthValidator(1)])
    description = models.TextField(blank=True)
    duration = models.DurationField(blank=True)
    age_limit = models.IntegerField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    director = models.CharField(max_length=200, blank=True)
    cast = models.JSONField(blank=True, default=list)
    event_url = models.URLField(blank=True)
    images_url = models.JSONField(blank=True, default=list)
    want_to_go = models.BooleanField(default=False)
    visited = models.BooleanField(default=False)


class ScheduleEvent(models.Model):
    repertoire_event = models.ForeignKey(RepertoireEvent, on_delete=models.CASCADE, unique=True)
    date_time = models.DateTimeField(unique=True)
    tickets_url = models.URLField(blank=True)


class TicketEvent(models.Model):
    repertoire_event = models.ForeignKey(RepertoireEvent, on_delete=models.CASCADE, unique=True)
    date_time = models.DateTimeField(unique=True)

    def get_attending_friends(self):
        return [fte.friend for fte in FriendTicketEvent.objects.filter(ticket_event=self)]


class Friend(models.Model):
    name = models.CharField(max_length=200, blank=True)
    full_name = models.CharField(max_length=200, unique=True, blank=False, validators=[MinLengthValidator(1)])

    def get_events(self):
        return [fte.ticket_event for fte in FriendTicketEvent.objects.filter(friend=self)]

    def get_debt_details(self):
        debts = Debt.objects.filter(friend=self)
        return {debt.reason: debt.amount for debt in debts}

    def get_total_debt(self):
        debts = Debt.objects.filter(friend=self)
        return sum(debt.amount for debt in debts)


class Debt(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, unique=True)
    reason = models.TextField(unique=True, blank=False, validators=[MinLengthValidator(1)])
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)


class FriendTicketEvent(models.Model):
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE, unique=True)
    ticket_event = models.ForeignKey(TicketEvent, on_delete=models.CASCADE, unique=True)
