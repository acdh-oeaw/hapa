# generated by appcreator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Layout, Fieldset
from crispy_forms.bootstrap import Accordion, AccordionGroup

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
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'zotero_id',
                    'text',
                    'page',
                    'short_quote',
                    'full_quote',
                    'time_of_origin_start',
                    'time_of_origin_end',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class HapaBelegForm(forms.ModelForm):

    class Meta:
        model = HapaBeleg
        fields = "__all__"

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
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'name',
                    'geonames',
                    'beleg',
                    'description',
                    'orig_sprache',
                    'lat',
                    'long',
                    'adm_unit',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class HapaPlaceNameForm(forms.ModelForm):
    orig_sprache = forms.ModelChoiceField(
        required=False,
        label="Sprache",
        queryset=SkosConcept.objects.filter(collection__name="orig_sprache")
    )
    adm_unit = forms.ModelChoiceField(
        required=False,
        label="Administrative Einheit",
        queryset=SkosConcept.objects.filter(collection__name="adm_unit")
    )

    class Meta:
        model = HapaPlaceName
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(HapaPlaceNameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
        self.fields['description'].initial = """
<h2>I. Sprache</h2>

<p>lorem ipsum</p>

<h2>II. Etymologie</h2>

<p>lorem ipsum</p>

<h2>III. Wortbildung</h2>

<p>lorem ipsum</p>
"""
