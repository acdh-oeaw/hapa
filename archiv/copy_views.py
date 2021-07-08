from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from archiv.models import HapaBeleg


@login_required
def copy_beleg(request):
    try:
        current_id = request.GET['current-id']
    except KeyError:
        return redirect('/')
    try:
        item = HapaBeleg.objects.get(id=current_id)
    except (ObjectDoesNotExist, ValueError):
        return redirect('/')
    item.id = None
    item.text = None
    item.page = "KOPIE"
    item.save()
    return redirect(item.get_edit_url())
