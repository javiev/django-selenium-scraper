from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScrapedData
from .serializer import ScrapedDataSerializer


@api_view(['GET'])
def scraped_data_list(request):
    queryset = ScrapedData.objects.all().order_by('-id')
    serializer = ScrapedDataSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def scraped_data_detail(request, pk):
    try:
        scraped_data = ScrapedData.objects.get(pk=pk)
    except ScrapedData.DoesNotExist:
        return Response(status=404)

    serializer = ScrapedDataSerializer(scraped_data)
    return Response(serializer.data)
