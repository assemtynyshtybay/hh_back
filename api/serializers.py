from rest_framework import serializers

from api.models import Vacancy, Company


class CompanySerializer(serializers.Serializer):
    # Nested Serializers
    # category = CategorySerializer2(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city','address')

class VacancySerializer(serializers.Serializer):
    # name = serializers.CharField(max_length=200)

    class Meta:
        model = Vacancy
        fields = ('id', 'name','description','salary')
class VacancyWithCompanySerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # products = serializers.StringRelatedField(many=True, read_only=True)
    companies = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'companies')