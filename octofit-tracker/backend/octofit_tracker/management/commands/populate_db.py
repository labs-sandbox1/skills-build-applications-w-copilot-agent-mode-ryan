from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create Users (Superheroes)
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date='2025-11-26')
        Activity.objects.create(user=spiderman, type='Cycling', duration=45, calories=400, date='2025-11-25')
        Activity.objects.create(user=batman, type='Swimming', duration=60, calories=500, date='2025-11-24')
        Activity.objects.create(user=superman, type='Flying', duration=120, calories=1000, date='2025-11-23')

        # Create Workouts
        Workout.objects.create(name='Push Ups', description='Upper body strength', difficulty='Easy')
        Workout.objects.create(name='Pull Ups', description='Upper body strength', difficulty='Medium')
        Workout.objects.create(name='Squats', description='Lower body strength', difficulty='Easy')
        Workout.objects.create(name='Deadlift', description='Full body strength', difficulty='Hard')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=700)
        Leaderboard.objects.create(team=dc, points=1500)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
