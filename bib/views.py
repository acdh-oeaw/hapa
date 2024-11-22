from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tqdm import tqdm

from archiv.models import HapaBeleg

from bib.models import ZotItem
from bib.zot_utils import create_zotitem, items_to_dict

library_id = settings.Z_ID
library_type = settings.Z_LIBRARY_TYPE
api_key = settings.Z_API_KEY


def sync_zotero(request):
    """renders a simple template with a button to trigger sync_zotero_action function"""
    context = {}
    return render(request, "bib/synczotero.html", context)


@login_required
def update_zotitems(request):
    """fetches all items with higher version number then the highest stored in db"""
    context = {}
    context["saved"] = []
    limit = None
    since = None
    context["books_before"] = ZotItem.objects.all().count()
    first_object = ZotItem.objects.all()[:1].get()
    since = first_object.zot_version
    items = items_to_dict(
        library_id, library_type, api_key, limit=limit, since_version=since
    )
    for x in items["bibs"]:
        temp_item = create_zotitem(x)
        context["saved"].append(temp_item)
    belege_to_update = HapaBeleg.objects.filter(zotero_id__in=context["saved"])
    for x in tqdm(belege_to_update, total=belege_to_update.count()):
        x.save()
    context["updated_belege"] = belege_to_update
    context["books_after"] = ZotItem.objects.all().count()

    return render(request, "bib/synczotero_action.html", context)
