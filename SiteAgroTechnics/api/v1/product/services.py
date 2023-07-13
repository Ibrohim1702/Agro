from collections import OrderedDict

from SiteAgroTechnics.settings import PER_PAGE
from appAgro.models import Product
from sqlpaginator import SqlPaginator


def format_pro(data):

    return OrderedDict([
        ('rasm', data.img.url),
        ('vil', data.vil),
        ('date', data.date),
        ('compain', data.compain),
        ('short_description', data.short_description),
        ('quvvati', data.quvvati),
        ("silindr", data.silindr),
        ("karobka", data.karobka),
        ("tezlik", data.tezlik),
        ("gildirak", data.gildirak),
        ("yoqilgi", data.yoqilgi),
        ("uzunlik", data.uzunlik),
        ("kenglik", data.kenglik),
        ("tepalik", data.tepalik),
        ("akumlyator", data.akumlyator),
        ("telefon", data.telefon),
        ("ctg", data.ctg.content),

    ])


def paginated_pro(requests):
    page = int(requests.GET.get('page', 1))
    ctg = Product.objects.all().order_by('-pk')

    limit = PER_PAGE
    offset = (page - 1) * limit

    result = []
    for x in range(offset, offset + limit):
        result.append(format_pro(ctg[x]))

    pag = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=len(ctg))
    meta = pag.get_paginated_response()

    return OrderedDict([
        ('result', result),
        ('meta', meta)
    ])
