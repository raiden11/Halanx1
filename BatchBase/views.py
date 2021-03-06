

from .models import Batches
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BatchesSerializer
from rest_framework.response import Response
from OrderBase.models import Order
from OrderBase .serializers import OrderSerializer


@api_view(['GET', 'POST'])
def batch_list(request):

    if request.method == 'GET':
        batches = Batches.objects.all()
        serializer = BatchesSerializer(batches, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BatchesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# To get product according to its pk
@api_view(['GET', 'PUT', 'DELETE'])
def batch_id(request, pk):

    try:
        part = Batches.objects.get(pk=pk)
    except Batches.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BatchesSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BatchesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET' 'DELETE'])
def batch_id_orders(request, pk):

    # returns json of all orders which have his particular batch number
    # now to retrieve items, you can go to Order.Items and call itemslist_id for all orders

    try:
        part = Order.objects.get(BatchId=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(part, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







