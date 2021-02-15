# generated by appcreator
import django_filters

from dal import autocomplete

from vocabs.models import SkosConcept
from bib.models import ZotItem
from gn_places.models import GeoNamesPlace
from . models import (
    HapaBeleg,
    HapaPlaceName
)


class HapaBelegListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=HapaBeleg._meta.get_field('legacy_id').help_text,
        label=HapaBeleg._meta.get_field('legacy_id').verbose_name
    )
    zotero_id = django_filters.ModelMultipleChoiceFilter(
        queryset=ZotItem.objects.all(),
        help_text=HapaBeleg._meta.get_field('zotero_id').help_text,
        label=HapaBeleg._meta.get_field('zotero_id').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="bib:zotitem-autocomplete",
        )
    )
    text = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=HapaBeleg._meta.get_field('text').help_text,
        label=HapaBeleg._meta.get_field('text').verbose_name
    )
    page = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=HapaBeleg._meta.get_field('page').help_text,
        label=HapaBeleg._meta.get_field('page').verbose_name
    )
    short_quote = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=HapaBeleg._meta.get_field('short_quote').help_text,
        label=HapaBeleg._meta.get_field('short_quote').verbose_name
    )
    full_quote = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=HapaBeleg._meta.get_field('full_quote').help_text,
        label=HapaBeleg._meta.get_field('full_quote').verbose_name
    )

    class Meta:
        model = HapaBeleg
        fields = [
            'id',
            'legacy_id',
            'zotero_id',
            'text',
            'page',
            'short_quote',
            'full_quote',
            'time_of_origin_start',
            'time_of_origin_end',
            ]


class HapaPlaceNameListFilter(django_filters.FilterSet):
    legacy_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=HapaPlaceName._meta.get_field('legacy_id').help_text,
        label=HapaPlaceName._meta.get_field('legacy_id').verbose_name
    )
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=HapaPlaceName._meta.get_field('name').help_text,
        label=HapaPlaceName._meta.get_field('name').verbose_name
    )
    geonames = django_filters.ModelMultipleChoiceFilter(
        queryset=GeoNamesPlace.objects.all(),
        help_text=HapaPlaceName._meta.get_field('geonames').help_text,
        label=HapaPlaceName._meta.get_field('geonames').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="gn_places-ac:geonamesplace-autocomplete",
        )
    )
    beleg = django_filters.ModelMultipleChoiceFilter(
        queryset=HapaBeleg.objects.all(),
        help_text=HapaPlaceName._meta.get_field('beleg').help_text,
        label=HapaPlaceName._meta.get_field('beleg').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="archiv-ac:hapabeleg-autocomplete",
        )
    )
    orig_sprache = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__name="orig_sprache"
        ),
        help_text=HapaPlaceName._meta.get_field('orig_sprache').help_text,
        label=HapaPlaceName._meta.get_field('orig_sprache').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/orig_sprache",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
                },
        )
    )
    adm_unit = django_filters.ModelMultipleChoiceFilter(
        queryset=SkosConcept.objects.filter(
            collection__name="adm_unit"
        ),
        help_text=HapaPlaceName._meta.get_field('adm_unit').help_text,
        label=HapaPlaceName._meta.get_field('adm_unit').verbose_name,
        widget=autocomplete.Select2Multiple(
            url="/vocabs-ac/specific-concept-ac/adm_unit",
            attrs={
                'data-placeholder': 'Autocomplete ...',
                'data-minimum-input-length': 2,
                },
        )
    )

    class Meta:
        model = HapaPlaceName
        fields = [
            'id',
            'legacy_id',
            'name',
            'geonames',
            'beleg',
            'orig_sprache',
            'lat',
            'long',
            'adm_unit',
        ]
