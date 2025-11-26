from djongo import models
from bson import ObjectId

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name
    
    @property
    def id(self):
        return str(self._id)

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members', db_column='team_id')
    date_joined = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.email
    
    @property
    def id(self):
        return str(self._id)
    
    @property
    def username(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities', db_column='user_id')
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    distance = models.FloatField(default=0.0)  # km
    calories_burned = models.IntegerField()
    date = models.DateField()
    
    class Meta:
        db_table = 'activities'
    
    def __str__(self):
        return f"{self.activity_type} - {self.user.email}"
    
    @property
    def id(self):
        return str(self._id)

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField(default=30)  # minutes
    category = models.CharField(max_length=50, default='General')
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.name
    
    @property
    def id(self):
        return str(self._id)

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries', db_column='user_id', null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard', db_column='team_id', null=True)
    total_points = models.IntegerField(default=0)
    activity_count = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'leaderboard'
    
    def __str__(self):
        if self.user:
            return f"{self.user.name}: {self.total_points}"
        return f"{self.team.name}: {self.total_points}"
    
    @property
    def id(self):
        return str(self._id)
    
    @property
    def user_name(self):
        return self.user.name if self.user else None
