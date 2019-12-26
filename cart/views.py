from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


from .models import Cart, CartItem

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def get(self, request, *args, **kwargs):
    if request.method == 'GET':
        snippets = File.objects.all()
        serializer = FileSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'GET':
      prod=request.GET['product']
      cli=request.GET['client']
      snippets = CartItem.objects.filter(product=prod,client=cli)
      serializer = cartItemSerializer(snippets, many=True)
      return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
      serializer = cartItemSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
      return JsonResponse(serializer.errors, status=400)