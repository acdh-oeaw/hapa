# generated by appcreator

from browsing.browsing_utils import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from gn_places.config import GN_HTML_URL
from vocabs.models import SkosConcept


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class GeoNamesPlace(models.Model):
    """A Geonames Place Instance"""

    legacy_id = models.CharField(max_length=300, blank=True, verbose_name="Legacy ID")
    gn_id = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="GeoNames ID",
        help_text="GeoNames ID",
    ).set_extra(
        is_public=True,
        data_lookup="geonameid",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="GeoNames ID: <value>",
    )
    gn_name = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Name",
        help_text="Name",
    ).set_extra(
        is_public=True,
        data_lookup="name",
        arche_prop="hasTitle",
    )
    gn_lat = models.FloatField(
        blank=True,
        null=True,
        verbose_name="latitude",
        help_text="Latitude",
    ).set_extra(
        is_public=True,
        data_lookup="latitude",
    )
    gn_long = models.FloatField(
        blank=True,
        null=True,
        verbose_name="longitude",
        help_text="Longitude",
    ).set_extra(
        is_public=True,
        data_lookup="longitude",
    )
    # gn_point = PointField(
    #     blank=True, null=True,
    #     verbose_name="centroid",
    #     help_text="Centroid of the place",
    # ).set_extra(
    #     is_public=True,
    #     arche_prop="hasWkt",
    # )
    gn_feature_class = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Feature Class",
        help_text="Feature Class",
    ).set_extra(
        is_public=True,
        data_lookup="feature class",
    )
    gn_feature_code = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Feature Code",
        help_text="Feature Code",
    ).set_extra(
        is_public=True,
        data_lookup="feature code",
    )
    gn_feature = models.ForeignKey(
        SkosConcept,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Feature Code as SKOS",
        help_text="The Place's Feature Code as SKOS",
    ).set_extra(is_public=True)
    gn_country_code = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Country Code",
        help_text="Country Code",
    ).set_extra(
        is_public=True,
        data_lookup="country code",
    )
    gn_cc2 = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Alternate Country Codes",
        help_text="Alternate Country Codes",
    ).set_extra(
        is_public=True,
        data_lookup="cc2",
    )
    gn_population = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Population",
        help_text="Population",
    ).set_extra(
        is_public=True,
        data_lookup="population",
    )
    gn_elevation = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Elevation (m)",
        help_text="Elevation (m)",
    ).set_extra(
        is_public=True,
        data_lookup="elevation",
    )
    gn_modification_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Modifcation Date",
        help_text="Modification Date",
    ).set_extra(
        is_public=True,
        data_lookup="modification date",
    )
    orig_data_csv = models.TextField(
        blank=True, null=True, verbose_name="The original data"
    ).set_extra(is_public=True)

    class Meta:
        ordering = [
            "gn_name",
        ]
        verbose_name = "GeoNamesPlace"

    def __str__(self):
        if self.gn_name:
            if self.gn_country_code and self.gn_feature_code:
                return (
                    f"{self.gn_name} ({self.gn_country_code}; {self.gn_feature_code})"
                )
            else:
                return f"{self.gn_name}"
        else:
            return "{}".format(self.legacy_id)

    def save(self, *args, **kwargs):
        # if self.gn_lat:
        #     point = Point(self.gn_long, self.gn_lat, srid=4326)
        #     self.gn_point = point
        if not self.legacy_id:
            self.legacy_id = self.gn_id
        if not self.gn_feature:
            if self.gn_feature_class and self.gn_feature_code:
                ft = ".".join((self.gn_feature_class, self.gn_feature_code))
                try:
                    self.gn_feature = SkosConcept.objects.get(notation=ft)
                except ObjectDoesNotExist:
                    pass
        super(GeoNamesPlace, self).save(*args, **kwargs)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_natural_primary_key(self):
        return "gn_id"

    def get_geonames_url(self):
        return f"{GN_HTML_URL}{self.gn_id}"

    def get_geonames_rdf(self):
        return f"{GN_HTML_URL}{self.gn_id}/about.rdf"
