from django.test import TestCase
from .models import Image, Comment, Profile
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.new_user = User(first_name = 'John', last_name = 'Doe', username = 'test', email = 'test@gmail.com', password = 'nana')
        self.new_user.save()
        self.profile = Profile(profile_pic = 'lamborghini.jpg' ,bio = "Living free", user = self.new_user)

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    # Testing the save method
    def test_save_method(self):
        self.profile.save_profile()
        details = Profile.objects.all()
        self.assertTrue(len(details) > 0)

    # Testing the delete method
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)==0)

    # Testing the update method 
    def test_update_method(self):
        self.profile.save_profile()
        self.profile.update_profile()
        updated_profile = Profile.objects.filter(bio = "Living free").update(bio = "Live free indeed")
        self.assertTrue(self.profile.bio != updated_profile)
        self.assertNotEqual(self.profile, updated_profile)