from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer,CatSerializer,SubSerializer
from .models import Cat,Sub,File
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


@login_required
@csrf_exempt
@api_view(['GET', 'POST'])
def add_to_wishlist(request,slug):

   item = get_object_or_404(Item,slug=slug)

   wished_item,created = Wishlist.objects.get_or_create(wished_item=item,
   slug = item.slug,
   user = request.user,
   )

   messages.info(request,'The item was added to your wishlist')
   return redirect('core:product_detail',slug=slug)