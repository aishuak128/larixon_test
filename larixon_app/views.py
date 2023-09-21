from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from larixon_app.models import Advert
from larixon_app.serializers import AdvertSerializer



@api_view(['GET',])
def advert_list_view(request):
    if request.method == 'GET':
        ads = Advert.objects.all()
        serializer = AdvertSerializer(ads, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def advert_view(request, pk=None):
    try:
        ad = Advert.objects.get(pk=pk)
    except Advert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ad.visited += 1
        ad.save()
        serializer = AdvertSerializer(ad)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdvertSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        confirmation = {'msg': f'{ad.title} is deleted'}
        ad.delete()
        return Response(confirmation, status=status.HTTP_204_NO_CONTENT)

