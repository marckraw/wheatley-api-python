from rest_framework.serializers import ModelSerializer
from .models import FinancialCommitment

class FinancialCommitmentSerializer(ModelSerializer):
    class Meta:
        model = FinancialCommitment
        fields = '__all__' # ['body', 'updated']

