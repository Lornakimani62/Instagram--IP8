from django.test import TestCase

from .models import *
# Test for Profile

class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User.objects.create_user('testuser','password')
        self.profile = Profile(bio='I am a testcase',photo='', user='')
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profiel) == 0)

# Test for Image class
class ImageTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.profile = Profile(bio='I am a testcase',photo='',user='')
        self.proile.save_profile()


        self.image = Image(name='image test', picture='my test',caption='a caption test', profile='', posted=self.profile)
        self.image.save_image()




    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.profile.delete_profile()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)


    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

