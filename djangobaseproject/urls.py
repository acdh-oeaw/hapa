from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from vocabs import api_views

router = routers.DefaultRouter()
router.register(r"skosconceptschemes", api_views.SkosConceptSchemeViewSet)
router.register(r"skoscollections", api_views.SkosCollectionViewSet)
router.register(r"skosconcepts", api_views.SkosConceptViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    path("browsing/", include("browsing.urls", namespace="browsing")),
    path("info/", include("infos.urls", namespace="info")),
    path("archiv/", include("archiv.urls", namespace="archiv")),
    path("archiv-ac/", include("archiv.dal_urls", namespace="archiv-ac")),
    path("bib/", include("bib.urls", namespace="bib")),
    path("gn-places-ac/", include("gn_places.dal_urls", namespace="gn_places-ac")),
    path("vocabs/", include("vocabs.urls", namespace="vocabs")),
    path("vocabs-ac/", include("vocabs.dal_urls", namespace="vocabs-ac")),
    path("", include("webpage.urls", namespace="webpage")),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "webpage.views.handler404"
