# generated by appcreator
from django.db.models import Q
from dal import autocomplete
from . models import *


class HapaBelegAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = HapaBeleg.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(short_quote__icontains=self.q)
            )
        return qs


class HapaPlaceNameAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = HapaPlaceName.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
            )
        return qs

