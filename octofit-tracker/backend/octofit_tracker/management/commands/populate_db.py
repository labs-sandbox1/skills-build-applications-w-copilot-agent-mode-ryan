from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating Teams...')
        # Create Teams
        marvel = Team.objects.create(name='Marvel Avengers', description='Earth\'s Mightiest Heroes')
        dc = Team.objects.create(name='Justice League', description='DC\'s Finest Superheroes')
        xmen = Team.objects.create(name='X-Men', description='Mutant Heroes')

        self.stdout.write('Creating Users...')
        # Create Users (Superheroes)
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='captain@marvel.com', team=marvel)
        
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)
        
        wolverine = User.objects.create(name='Wolverine', email='wolverine@xmen.com', team=xmen)
        storm = User.objects.create(name='Storm', email='storm@xmen.com', team=xmen)

        self.stdout.write('Creating Activities...')
        # Create Activities
        today = date.today()
        Activity.objects.create(
            user=ironman, 
            activity_type='Flying', 
            duration=45, 
            distance=150.0,
            calories_burned=450, 
            date=today
        )
        Activity.objects.create(
            user=ironman, 
            activity_type='Weight Training', 
            duration=60, 
            distance=0.0,
            calories_burned=500, 
            date=today - timedelta(days=1)
        )
        
        Activity.objects.create(
            user=spiderman, 
            activity_type='Web Swinging', 
            duration=30, 
            distance=50.0,
            calories_burned=400, 
            date=today
        )
        Activity.objects.create(
            user=spiderman, 
            activity_type='Running', 
            duration=45, 
            distance=10.0,
            calories_burned=500, 
            date=today - timedelta(days=2)
        )
        
        Activity.objects.create(
            user=captain, 
            activity_type='Running', 
            duration=120, 
            distance=25.0,
            calories_burned=1200, 
            date=today
        )
        
        Activity.objects.create(
            user=batman, 
            activity_type='Martial Arts', 
            duration=90, 
            distance=0.0,
            calories_burned=800, 
            date=today
        )
        Activity.objects.create(
            user=batman, 
            activity_type='Cycling', 
            duration=60, 
            distance=30.0,
            calories_burned=600, 
            date=today - timedelta(days=1)
        )
        
        Activity.objects.create(
            user=superman, 
            activity_type='Flying', 
            duration=120, 
            distance=500.0,
            calories_burned=1500, 
            date=today
        )
        Activity.objects.create(
            user=superman, 
            activity_type='Weight Lifting', 
            duration=30, 
            distance=0.0,
            calories_burned=400, 
            date=today - timedelta(days=1)
        )
        
        Activity.objects.create(
            user=wonderwoman, 
            activity_type='Combat Training', 
            duration=75, 
            distance=0.0,
            calories_burned=700, 
            date=today
        )
        
        Activity.objects.create(
            user=wolverine, 
            activity_type='Running', 
            duration=60, 
            distance=15.0,
            calories_burned=650, 
            date=today
        )
        
        Activity.objects.create(
            user=storm, 
            activity_type='Flying', 
            duration=45, 
            distance=80.0,
            calories_burned=500, 
            date=today
        )

        self.stdout.write('Creating Workouts...')
        # Create Workouts
        Workout.objects.create(
            name='Super Soldier Training',
            description='Full body workout inspired by Captain America',
            difficulty='Hard',
            duration=60,
            category='Strength'
        )
        Workout.objects.create(
            name='Web Warrior Cardio',
            description='High-intensity cardio workout',
            difficulty='Medium',
            duration=30,
            category='Cardio'
        )
        Workout.objects.create(
            name='Bat-Cave Calisthenics',
            description='Bodyweight exercises for peak performance',
            difficulty='Hard',
            duration=45,
            category='Calisthenics'
        )
        Workout.objects.create(
            name='Amazonian Warrior Training',
            description='Combat and strength training combined',
            difficulty='Hard',
            duration=90,
            category='Combat'
        )
        Workout.objects.create(
            name='Mutant Power Yoga',
            description='Flexibility and mental focus workout',
            difficulty='Easy',
            duration=45,
            category='Flexibility'
        )
        Workout.objects.create(
            name='Speed Force Sprint',
            description='High-speed interval training',
            difficulty='Medium',
            duration=30,
            category='HIIT'
        )

        self.stdout.write('Creating Leaderboard...')
        # Create Leaderboard entries for users
        Leaderboard.objects.create(user=superman, total_points=1900, activity_count=2)
        Leaderboard.objects.create(user=batman, total_points=1400, activity_count=2)
        Leaderboard.objects.create(user=captain, total_points=1200, activity_count=1)
        Leaderboard.objects.create(user=ironman, total_points=950, activity_count=2)
        Leaderboard.objects.create(user=spiderman, total_points=900, activity_count=2)
        Leaderboard.objects.create(user=wonderwoman, total_points=700, activity_count=1)
        Leaderboard.objects.create(user=wolverine, total_points=650, activity_count=1)
        Leaderboard.objects.create(user=storm, total_points=500, activity_count=1)

        self.stdout.write(self.style.SUCCESS('✅ octofit_db database populated with test data!'))
        self.stdout.write(self.style.SUCCESS(f'   - Created {Team.objects.count()} teams'))
        self.stdout.write(self.style.SUCCESS(f'   - Created {User.objects.count()} users'))
        self.stdout.write(self.style.SUCCESS(f'   - Created {Activity.objects.count()} activities'))
        self.stdout.write(self.style.SUCCESS(f'   - Created {Workout.objects.count()} workouts'))
        self.stdout.write(self.style.SUCCESS(f'   - Created {Leaderboard.objects.count()} leaderboard entries'))
