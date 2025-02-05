from django.test import TestCase
from .models import User, Health  # Import the Health model if it's in the same app
from django.core.files.uploadedfile import SimpleUploadedFile

class UserTestCase(TestCase):
    def setUp(self):
        # Create a Health instance if needed for the ForeignKey
        health_status = Health.objects.create(health_detail='Healthy')
        
        # Create a User instance
        self.user = User.objects.create(
            username='testuser',
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            gender='male',
            health_status=health_status,
            address='123 Test St',
            phone='1234567890',
            notes='Test notes'
        )
        
        # Add devices if needed
        # device = Device.objects.create(device_detail='Test Device')
        # self.user.devices.add(device)

    def test_user_creation(self):
        # Test that the user instance has been created
        self.assertEqual(self.user.username, 'testuser')

    def test_user_fields(self):
        # Test the fields of the user instance
        self.assertEqual(self.user.gender, 'male')
        self.assertEqual(self.user.address, '123 Test St')
        self.assertEqual(self.user.phone, '1234567890')
        self.assertEqual(self.user.notes, 'Test notes')

        # Test image field
        self.assertIsNotNone(self.user.image)

        # Test health_status ForeignKey
        self.assertEqual(self.user.health_status.health_detail, 'Healthy')

        # Test devices ManyToManyField
        # self.assertIn(device, self.user.devices.all())

# More tests can be added as needed
