from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from .models import Ingredient, Health, Category,Meal,Device,UserMealIngredient  # Import necessary models
from account.models import User

class IngredientTestCase(TestCase):
    def setUp(self):
        # Create a Health instance if needed for the ForeignKey
        health_status = Health.objects.create(health_detail='Good')
        
        # Create Category instances if needed for the ManyToManyField
        category1 = Category.objects.create(name='Vegetable')
        category2 = Category.objects.create(name='Fruit')
        
        # Create an Ingredient instance
        self.ingredient = Ingredient.objects.create(
            name='Tomato',
            health_status=health_status,
            category_type='Healthy',
            type='Breakfast',
            meal_type='Popular',
            image=SimpleUploadedFile(name='test_ingredient.jpg', content=b'', content_type='image/jpeg'),
            notes='Rich in vitamins'
        )
        
        # Add categories
        self.ingredient.categories.add(category1, category2)

    def test_ingredient_creation(self):
        # Test that the ingredient instance has been created
        self.assertEqual(self.ingredient.name, 'Tomato')

    def test_ingredient_fields(self):
        # Test the fields of the ingredient instance
        self.assertEqual(self.ingredient.category_type, 'Healthy')
        self.assertEqual(self.ingredient.type, 'Breakfast')
        self.assertEqual(self.ingredient.meal_type, 'Popular')
        self.assertEqual(self.ingredient.notes, 'Rich in vitamins')

        # Test image field
        self.assertIsNotNone(self.ingredient.image)

        # Test health_status ForeignKey
        self.assertEqual(self.ingredient.health_status.health_detail, 'Good')

        # Test categories ManyToManyField
        categories = self.ingredient.categories.all()
        self.assertIn(self.category1, categories)
        self.assertIn(self.category2, categories)

class MealTestCase(TestCase):
    def setUp(self):
        # Create instances for ForeignKey and ManyToManyFields
        health_status = Health.objects.create(health_detail='Excellent')
        category = Category.objects.create(name='Main Course')
        device = Device.objects.create(device_detail='Oven')
        ingredient = Ingredient.objects.create(name='Chicken Breast')
        
        # Create a Meal instance
        self.meal = Meal.objects.create(
            name='Grilled Chicken',
            health_status=health_status,
            meal_type='Popular',
            category_type='Healthy',
            type='Dinner',
            healthy_type='DIET',
            video=ContentFile(b'Mock video content', name='test_video.mp4'),
            image=SimpleUploadedFile(name='test_meal.jpg', content=b'', content_type='image/jpeg'),
            description='A delicious grilled chicken meal',
            notes='Low in carbs'
        )
        
        # Add categories, devices, and ingredients
        self.meal.categories.add(category)
        self.meal.devices.add(device)
        self.meal.ingredients.add(ingredient)

    def test_meal_creation(self):
        # Test that the meal instance has been created
        self.assertEqual(self.meal.name, 'Grilled Chicken')

    def test_meal_fields(self):
        # Test the fields of the meal instance
        self.assertEqual(self.meal.meal_type, 'Popular')
        self.assertEqual(self.meal.category_type, 'Healthy')
        self.assertEqual(self.meal.type, 'Dinner')
        self.assertEqual(self.meal.healthy_type, 'DIET')
        self.assertEqual(self.meal.description, 'A delicious grilled chicken meal')
        self.assertEqual(self.meal.notes, 'Low in carbs')

        # Test video and image fields
        self.assertIsNotNone(self.meal.video)
        self.assertIsNotNone(self.meal.image)

        # Test ForeignKey and ManyToManyFields
        self.assertEqual(self.meal.health_status.health_detail, 'Excellent')
        self.assertIn(self.category, self.meal.categories.all())
        self.assertIn(self.device, self.meal.devices.all())
        self.assertIn(self.ingredient, self.meal.ingredients.all())
        
        
class UserMealIngredientTestCase(TestCase):
    def setUp(self):
        # Create instances of User, Category, and Ingredient for ForeignKey and ManyToManyFields
        user = User.objects.create(username='testuser')
        category = Category.objects.create(name='Grains')
        ingredient = Ingredient.objects.create(name='Rice')
        
        # Create a UserMealIngredient instance
        self.user_meal_ingredient = UserMealIngredient.objects.create(
            user=user,
            meal_type='Popular',
            category_type='Healthy',
            type='Dinner',
            healthy_type='DIET'
        )
        
        # Add categories and ingredients
        self.user_meal_ingredient.categories.add(category)
        self.user_meal_ingredient.ingredients.add(ingredient)

    def test_user_meal_ingredient_creation(self):
        # Test that the UserMealIngredient instance has been created
        self.assertEqual(self.user_meal_ingredient.user.username, 'testuser')

    def test_user_meal_ingredient_fields(self):
        # Test the fields of the UserMealIngredient instance
        self.assertEqual(self.user_meal_ingredient.meal_type, 'Popular')
        self.assertEqual(self.user_meal_ingredient.category_type, 'Healthy')
        self.assertEqual(self.user_meal_ingredient.type, 'Dinner')
        self.assertEqual(self.user_meal_ingredient.healthy_type, 'DIET')

        # Test ManyToManyFields
        self.assertIn(self.category, self.user_meal_ingredient.categories.all())
        self.assertIn(self.ingredient, self.user_meal_ingredient.ingredients.all())