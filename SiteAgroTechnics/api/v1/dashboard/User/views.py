from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound, AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.category.services import format_ctg, paginated_ctg
from api.v1.dashboard.User.serializer import UserSerializer
from base.helper import BearerToken
from sayt_dashboard.models import User


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    # permission_classes = (IsAuthenticated, )
    # authentication_classes = (BearerToken, )

    def post(self, requests, *args, **kwargs):
        data = requests.data
        try:
            user = User()
            user.name = data['name']
            user.username = data['username']
            user.set_password(data['password'])
            user.is_staff = True
            user.save()
        except Exception as e:
            return Response({"ERROR": f'{e}'})

        token = Token.objects.create(user=user)

        return Response({"success": token.key})


class LoginView(GenericAPIView):
    def post(self, requests, *args, **kwargs):
        data = requests.data
        try:
            user = User.objects.get(username=data.get('username'))
        except:
            raise NotFound("User not found!")

        if not user.check_password(data.get('password')):
            raise AuthenticationFailed("Password not found!")

        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.create(user=user)

        return Response({"success": token.key})


class LogoutView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BearerToken,)

    def post(self, requests, *args, **kwargs):
        token = Token.objects.get(user=requests.user)
        token.delete()

        return Response({"success": "Token is delete!"})
