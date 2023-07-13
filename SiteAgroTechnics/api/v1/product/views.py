from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.product.seralazer import ProductSerializer
from api.v1.product.services import format_pro, paginated_pro
from appAgro.models import Product
from base.helper import BearerToken


class ProductView(GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def get_object(self, pk=None):
        try:
            root = Product.objects.get(pk=pk)
        except:
            raise NotFound(f"{pk} idsidagi product yo'q!")
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            pro = Product.objects.filter(pk=pk).first()
            if not pro:
                result = {"Error": "Bunday product yo'q!"}
            else:
                result = format_pro(pro)
        else:
            result = paginated_pro(requests)
        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serialazer = self.get_serializer(data=data)
        serialazer.is_valid(raise_exception=True)
        result = serialazer.save()

        return Response(format_pro(result))

    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        root = self.get_object(pk)
        serialazer = self.get_serializer(data=data, partial=True, instance=root)
        serialazer.is_valid(raise_exception=True)
        result = serialazer.save()

        return Response(format_pro(result))

    def delete(self, requests, pk, *args, **kwargs, ):
        pro = Product.objects.filter(pk=pk).first()
        if not pro:
            result = {"ERROR": "Bunday product mavjud emas!"}
        else:
            pro.delete()
            result = {"Success": f"{pro.name} o'chirib tashlandi!"}

        return Response(result)


