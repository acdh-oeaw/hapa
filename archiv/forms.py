# generated by appcreator
from crispy_forms.bootstrap import AccordionGroup
from crispy_bootstrap5.bootstrap5 import BS5Accordion

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from dal import autocomplete
from django import forms
from leaflet.forms.widgets import LeafletWidget
from mptt.forms import TreeNodeChoiceField

from vocabs.models import SkosConcept

from .models import HapaBeleg, HapaPlaceName


class HapaBelegFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(HapaBelegFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic search options",
                    "id",
                    "short_quote",
                    css_id="basic_search_fields",
                ),
                AccordionGroup(
                    "Advanced search",
                    "zotero_id",
                    "text",
                    "full_quote",
                    "time_of_origin_start",
                    "time_of_origin_end",
                    "comment",
                    css_id="more",
                ),
                AccordionGroup(
                    "Admin",
                    "internal_comment",
                    css_id="admin_search",
                ),
                always_open=True,
            ),
        )


class HapaBelegForm(forms.ModelForm):
    place = forms.ModelMultipleChoiceField(
        required=False,
        queryset=HapaPlaceName.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url="archiv-ac:hapaplacename-autocomplete"
        ),
    )

    class Meta:
        model = HapaBeleg
        exclude = ()
        widgets = {
            "zotero_id": autocomplete.ModelSelect2(url="bib:zotitem-autocomplete")
        }

    def __init__(self, *args, **kwargs):
        super(HapaBelegForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )

        if self.instance.pk:
            self.fields["place"].initial = (
                self.instance.rvn_hapaplacename_beleg_beleg.all()
            )

    def save(self, *args, **kwargs):
        instance = super(HapaBelegForm, self).save(*args, **kwargs)
        hapa_places = HapaPlaceName.objects.filter(beleg=instance)
        for x in hapa_places:
            x.beleg.remove(instance)
        if self.cleaned_data["place"]:
            instance.rvn_hapaplacename_beleg_beleg.add(*self.cleaned_data["place"])
        return self.instance


class HapaPlaceNameFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(HapaPlaceNameFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = "genericFilterForm"
        self.form_method = "GET"
        self.form_tag = False
        self.layout = Layout(
            BS5Accordion(
                AccordionGroup(
                    "Basic search options",
                    Field(
                        "name",
                        css_class="js-kioskboard-input",
                        data_kioskboard_type="keyboard",
                        data_kioskboard_specialcharacters="false",
                    ),
                    "alternative_names",
                    "historic_names",
                    "historic",
                    css_id="basic_search_fields",
                ),
                AccordionGroup("Geography", "geonames", "adm_unit", css_id="more"),
                AccordionGroup(
                    "Details",
                    "orig_sprache",
                    "wortbildung",
                    "etymology",
                    "syntax",
                    "comment",
                    "beleg",
                    "beleg__zotero_id",
                    css_id="etym",
                ),
                AccordionGroup(
                    "admin",
                    "id",
                    "internal_comment",
                    "unclear",
                    css_id="admin_search",
                ),
                always_open=True,
            ),
        )


class HapaPlaceNameForm(forms.ModelForm):
    orig_sprache = TreeNodeChoiceField(
        required=False,
        label="Sprache",
        queryset=SkosConcept.objects.filter(collection__name="orig_sprache"),
    )
    adm_unit = forms.ModelChoiceField(
        required=False,
        label="Administrative Einheit",
        queryset=SkosConcept.objects.filter(collection__name="adm_unit"),
        widget=autocomplete.ModelSelect2(url="archiv-ac:adm-units"),
    )

    class Meta:
        model = HapaPlaceName
        exclude = ("beleg",)
        widgets = {
            "geonames": autocomplete.ModelSelect2(
                url="gn_places-ac:geonamesplace-autocomplete"
            ),
            "fuzzy_geom": LeafletWidget(),
            "point": LeafletWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(HapaPlaceNameForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3"
        self.helper.field_class = "col-md-9"
        self.helper.add_input(
            Submit("submit", "save"),
        )
