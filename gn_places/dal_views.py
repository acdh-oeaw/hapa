# generated by appcreator
from dal import autocomplete
from django.db.models import Q

from gn_places.models import GeoNamesPlace


class GeoNamesPlaceAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = GeoNamesPlace.objects.all()

        if self.q:
            qs = qs.filter(Q(gn_name__icontains=self.q) | Q(gn_id__icontains=self.q))
        return qs

    def get_result_label(self, item):
        return f"{item} [gnd_id: {item.gn_id}]"
