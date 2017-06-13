from rest_framework.serializers import ModelSerializer

from .models import Company, Employee, Opening


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = [
            'name',
            'role',
            'age',
        ]


class OpeningSerializer(ModelSerializer):

    class Meta:
        model = Opening
        fields = [
            'role',
        ]


class CompanySerializer(ModelSerializer):
    employee_set = EmployeeSerializer(many=True)
    opening_set = OpeningSerializer(many=True)

    class Meta:
        model = Company
        fields = [
            'name',
            'location',
            'no_of_staff',
            'employee_set',
            'opening_set',
        ]