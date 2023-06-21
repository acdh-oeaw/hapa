from django import template

register = template.Library()


@register.inclusion_tag("bib/tags/zotitem.html")
def bib_quote(item):
    values = {}
    values["quote"] = f"{item.zot_bibtex}"
    values["object"] = item
    return values
