from django.test import TestCase
from ..models import Menu
from ..serializers import MenuSerializer
from rest_framework.permissions import IsAuthenticated

class MenuViewTest(TestCase):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]     

    def setUp(self):
        Menu.objects.create(title="Jerky", price=.10, inventory=100)
        Menu.objects.create(title="ElephantEar", price=5, inventory=20)

    def test_get_all(self):
        item = Menu.objects.get(title="Jerky")
        self.assertEqual(str(item), "Jerky : 0.10")
        item = Menu.objects.get(title="ElephantEar")
        self.assertEqual(str(item), "ElephantEar : 5.00")