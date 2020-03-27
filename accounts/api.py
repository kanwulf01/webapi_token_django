from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, UserHerenciaSerializer, LoginSerializer

''' Register API
Esta clase hereda de genercis, generics APIView, se llama a la clase UserHerenciaSerializer, que es la clase 
encargada de devolver el usuario con todos sus campos, y de enlazar a usuario con el serializer de la clase medico creada
models, se define un metodo post, que recibe un request, y args y kargs, se llama al serializer que se instancio en 
serializer_class con el get_serializer, y se le pasan los datos llegados en formaton json por request.data
se valida que el serializador con los datos sea valido, se guarda en la base de datos , y se hace una respuesta
devolviendo al usuario que se creo inmediatamente, y se crea un token pasandole como parametro el usuario que se acabo de crear
tambien se retorna el token
'''
class RegisterAPI(generics.GenericAPIView):
    serializer_class = UserHerenciaSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":UserHerenciaSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })

'''
    loginAPI

se instancia un serializer Loginserializer, que contiene la validacion de los campos llegados por el request
se usa un metodo en serializer llamado autheticate
si la informacion llevada al serializador es valida, retorna al usuario y su token*(refresca el token lo crea de nuevo)
'''

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user":UserHerenciaSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })

'''
    UserAPi
valida si tiene permisos de usuario usando el token, si el token existe retorna todos los datos del usuario
'''
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserHerenciaSerializer

    def get_object(self):
        return self.request.user