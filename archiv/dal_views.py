# generated by appcreator
from django.db.models import Q
from dal import autocomplete
from mptt.settings import DEFAULT_LEVEL_INDICATOR

from . models import HapaBeleg, HapaPlaceName
from vocabs.models import SkosConcept


class LangAC(autocomplete.Select2QuerySetView):
    def get_result_label(self, item):
        level_indicator = DEFAULT_LEVEL_INDICATOR * item.level
        return level_indicator + ' ' + str(item)

    def get_queryset(self):
        qs = SkosConcept.objects.filter(collection__name='orig_sprache')
        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)
        return qs


class AdmUnitsAC(autocomplete.Select2QuerySetView):
    def get_result_label(self, item):
        result = f"{item} << {item.broader_concept} << {item.broader_concept.broader_concept}"
        return result

    def get_queryset(self):
        qs = SkosConcept.objects.filter(
            collection__name='adm_unit'
        ).filter(
            narrower_concepts=None
        )
        if self.q:
            qs = qs.filter(pref_label__icontains=self.q)
        return qs


class HapaBelegAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = HapaBeleg.objects.all()

        if self.q:
            qs = qs.filter(
                Q(short_quote__icontains=self.q) |
                Q(page_nr__icontains=self.q)
            )
        return qs


class HapaPlaceNameAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = HapaPlaceName.objects.all()

        if self.q:
            qs = qs.filter(
                Q(name__icontains=self.q)
            )
        return qs
