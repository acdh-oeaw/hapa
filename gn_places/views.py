# generated by appcreator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from . filters import *
from . forms import *
from . tables import *
from . models import (
    GeoNamesPlace
)
from browsing.browsing_utils import (
    GenericListView, BaseCreateView, BaseUpdateView, BaseDetailView
)


class GeoNamesPlaceListView(GenericListView):

    model = GeoNamesPlace
    filter_class = GeoNamesPlaceListFilter
    formhelper_class = GeoNamesPlaceFilterFormHelper
    table_class = GeoNamesPlaceTable
    init_columns = [
        'id', 'gn_name',
    ]
    enable_merge = True


class GeoNamesPlaceDetailView(BaseDetailView):

    model = GeoNamesPlace
    template_name = 'browsing/generic_detail.html'


class GeoNamesPlaceCreate(BaseCreateView):

    model = GeoNamesPlace
    form_class = GeoNamesPlaceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GeoNamesPlaceCreate, self).dispatch(*args, **kwargs)


class GeoNamesPlaceUpdate(BaseUpdateView):

    model = GeoNamesPlace
    form_class = GeoNamesPlaceForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GeoNamesPlaceUpdate, self).dispatch(*args, **kwargs)


class GeoNamesPlaceDelete(DeleteView):
    model = GeoNamesPlace
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('gn_places:geonamesplace_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GeoNamesPlaceDelete, self).dispatch(*args, **kwargs)


