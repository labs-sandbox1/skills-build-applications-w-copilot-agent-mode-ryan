from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'member_count']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_member_count(self, obj):
        return obj.members.count()

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    username = serializers.CharField(source='name', read_only=True)
    team_id = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'team_id', 'date_joined']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_team_id(self, obj):
        return str(obj.team._id) if obj.team else None

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'activity_type', 'duration', 'distance', 'calories_burned', 'date']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_id(self, obj):
        return str(obj.user._id) if obj.user else None

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration', 'category']
    
    def get_id(self, obj):
        return str(obj._id)

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user_name = serializers.CharField(source='user.name', read_only=True)
    user_id = serializers.SerializerMethodField()
    team_id = serializers.SerializerMethodField()
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'user_name', 'team_id', 'total_points', 'activity_count']
    
    def get_id(self, obj):
        return str(obj._id)
    
    def get_user_id(self, obj):
        return str(obj.user._id) if obj.user else None
    
    def get_team_id(self, obj):
        return str(obj.team._id) if obj.team else None
