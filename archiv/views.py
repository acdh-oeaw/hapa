# generated by appcreator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from archiv.filters import (
    HapaBelegListFilter,
    HapaPlaceNameListFilter
)
from archiv.forms import (
    HapaBelegFilterFormHelper,
    HapaBelegForm,
    HapaPlaceNameFilterFormHelper,
    HapaPlaceNameForm
)
from archiv.tables import (
    HapaBelegTable,
    HapaPlaceNameTable
)
from archiv.models import (
    HapaBeleg,
    HapaPlaceName
)
from browsing.browsing_utils import (
    GenericListView, BaseCreateView, BaseUpdateView, BaseDetailView
)


class HapaBelegListView(GenericListView):

    model = HapaBeleg
    filter_class = HapaBelegListFilter
    formhelper_class = HapaBelegFilterFormHelper
    table_class = HapaBelegTable
    init_columns = [
        'id', 'short_quote',
    ]
    enable_merge = True


class HapaBelegDetailView(BaseDetailView):

    model = HapaBeleg
    template_name = 'archiv/generic_detail.html'


class HapaBelegCreate(BaseCreateView):

    model = HapaBeleg
    form_class = HapaBelegForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HapaBelegCreate, self).dispatch(*args, **kwargs)


class HapaBelegUpdate(BaseUpdateView):

    model = HapaBeleg
    form_class = HapaBelegForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HapaBelegUpdate, self).dispatch(*args, **kwargs)


class HapaBelegDelete(DeleteView):
    model = HapaBeleg
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:hapabeleg_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HapaBelegDelete, self).dispatch(*args, **kwargs)


class HapaPlaceNameListView(GenericListView):

    model = HapaPlaceName
    filter_class = HapaPlaceNameListFilter
    formhelper_class = HapaPlaceNameFilterFormHelper
    table_class = HapaPlaceNameTable
    init_columns = [
        'id', 'name',
    ]
    enable_merge = True


class HapaPlaceNameDetailView(BaseDetailView):

    model = HapaPlaceName
    template_name = 'archiv/generic_detail.html'


class HapaPlaceNameCreate(BaseCreateView):

    model = HapaPlaceName
    form_class = HapaPlaceNameForm
    template_name = 'archiv/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HapaPlaceNameCreate, self).dispatch(*args, **kwargs)


class HapaPlaceNameUpdate(BaseUpdateView):

    model = HapaPlaceName
    form_class = HapaPlaceNameForm
    template_name = 'archiv/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HapaPlaceNameUpdate, self).dispatch(*args, **kwargs)


class HapaPlaceNameDelete(DeleteView):
    model = HapaPlaceName
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:hapaplacename_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HapaPlaceNameDelete, self).dispatch(*args, **kwargs)
