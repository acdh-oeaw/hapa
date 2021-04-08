# generated by appcreator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Layout, Fieldset
from crispy_forms.bootstrap import Accordion, AccordionGroup
from dal import autocomplete

from leaflet.forms.widgets import LeafletWidget
from mptt.forms import TreeNodeChoiceField

from vocabs.models import SkosConcept
from . models import (
    HapaBeleg,
    HapaPlaceName
)


class HapaBelegFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(HapaBelegFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'short_quote',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'zotero_id',
                    'text',
                    'tags',
                    'page',
                    'full_quote',
                    'time_of_origin_start',
                    'time_of_origin_end',
                    'comment',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'tags',
                    'internal_comment',
                    'unclear',
                    css_id="admin_search"
                    ),
                )
            )


class HapaBelegForm(forms.ModelForm):

    class Meta:
        model = HapaBeleg
        exclude = ()
        widgets = {
            'zotero_id': autocomplete.ModelSelect2(
                url='bib:zotitem-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(HapaBelegForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class HapaPlaceNameFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(HapaPlaceNameFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'name',
                'alternative_names',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Geographie',
                    'geonames',
                    'adm_unit',
                    css_id="more"
                    ),
                AccordionGroup(
                    'Etymologisches',
                    'orig_sprache',
                    'wortbildung',
                    'etymology',
                    'syntax',
                    'comment',
                    'beleg',
                    # 'beleg__zotero_id',
                    css_id="etym"
                    ),
                AccordionGroup(
                    'admin',
                    'tags',
                    'internal_comment',
                    'unclear',
                    css_id="admin_search"
                    ),
                )
            )


class HapaPlaceNameForm(forms.ModelForm):
    orig_sprache = TreeNodeChoiceField(
        required=False,
        label="Sprache",
        queryset=SkosConcept.objects.filter(collection__name="orig_sprache")
    )
    adm_unit = forms.ModelChoiceField(
        required=False,
        label="Administrative Einheit",
        queryset=SkosConcept.objects.filter(collection__name="adm_unit"),
        widget=autocomplete.ModelSelect2(
                url='archiv-ac:adm-units'
            ),
    )

    class Meta:
        model = HapaPlaceName
        exclude = ()
        widgets = {
            'beleg': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:hapabeleg-autocomplete'
            ),
            'geonames': autocomplete.ModelSelect2(
                url='gn_places-ac:geonamesplace-autocomplete'
            ),
            'fuzzy_geom': LeafletWidget(),
            'point': LeafletWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(HapaPlaceNameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
