from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from .models import Ad
from .serializers import AdSerializer


@api_view(['GET'])
def ad_detail(request, ad_id):
    try:
        ad = Ad.objects.get(ad_id=ad_id)
        serializer = AdSerializer(ad)
        return Response(serializer.data, status=HTTP_200_OK)
    except Ad.DoesNotExist:
        return Response({'error': 'Ad not found'}, status=HTTP_404_NOT_FOUND)


@api_view(['GET'])
def ad_list(request):
    ad = Ad.objects.all()
    serializer = AdSerializer(ad, many=True)
    return Response(serializer.data, status=HTTP_200_OK)
