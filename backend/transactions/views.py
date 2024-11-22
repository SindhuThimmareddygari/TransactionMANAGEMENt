from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import status

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            return self.queryset.filter(user_id=user_id)
        return self.queryset

    @action(detail=True, methods=['put'])
    def update_status(self, request, pk=None):
        transaction = self.get_object()
        status = request.data.get('status', None)
        if status not in ['COMPLETED', 'FAILED']:
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
        transaction.status = status
        transaction.save()
        return Response(TransactionSerializer(transaction).data)

