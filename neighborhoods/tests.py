from django.test import TestCase
from .models import Profile, Post, Business, Neighbourhood
from django.contrib.auth.models import User


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='skimanikings',
                         email='kimanisimon856@gmai.com', password='qwertyuioplkjh')
        self.user.save()

        self.neighbourhood = Neigbourhood(
            name='Simon', description='Party the night away!!', police_number=919, healthcenter_number=919)
        self.neighbourhood.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        profile = Profile.objects.all().delete()
        self.assertTrue(len(profile) > 0)

    def tearDown(self):
        Profile.objects.all().delete()


class TestNeigbourhood(TestCase):
    def setUp(self):
        self.neighbourhood = Neigbourhood(name='simon', description='Party the night away!!', location='Nairobi',
                                          admin='skimanikings', , police_number=919, healthcenter_number=919, occupants_count='1')
        self.neighbourhood.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neigbourhood))

    def test_save_heighbourhood(self):
        hood = Neigbourhood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_neighbourhood(self):
        hoods = Neigbourhood.objects.all().delete()
        self.assertTrue(len(hoods) > 0)


class TestBusiness(TestCase):
    def setUp(self):
        self.user = User(username='skimanikings',
                         email='kimanisimon856@@gmail.com', password='qwertyuioplkjh')
        self.user.save()

        self.neighbourhood = Neigbourhood(
            name='simon', description='Party the night away!!', police_number=919, health_number=919)
        self.hood.save()

        self.busins = Business(name='Club Genge', email='gengeclub@gmail.com',
                               description='Party the night away!!', neighbourhood=self.hood, user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.busins, Business))

    def test_save_hood(self):
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def test_delete_hood(self):
        business = Business.objects.all().delete()
        self.assertTrue(len(business) > 0)
