import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile
from competitions.models import Competition
from submissions.models import Submission
from ai.score import score_submission, assign_ranks
from django.conf import settings

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        base_path = settings.BASE_DIR.parent / 'sample_data'
        
        # 1. Users
        with open(base_path / 'sample_users.json', 'r') as f:
            users_data = json.load(f)
        
        created_users = []
        for u_data in users_data:
            if not User.objects.filter(username=u_data['username']).exists():
                user = User.objects.create_user(
                    username=u_data['username'],
                    email=u_data['email'],
                    password=u_data['password']
                )
                user.profile.is_admin = u_data['is_admin']
                user.profile.cgpa = u_data['cgpa']
                user.profile.department = u_data['department']
                user.profile.save()
                created_users.append(user)
                self.stdout.write(f"Created user: {user.username}")
            else:
                created_users.append(User.objects.get(username=u_data['username']))

        # 2. Competitions
        with open(base_path / 'sample_competitions.json', 'r') as f:
            comps_data = json.load(f)
        
        created_comps = []
        for c_data in comps_data:
            comp, created = Competition.objects.get_or_create(
                title=c_data['title'],
                defaults={
                    'description': c_data['description'],
                    'deadline': c_data['deadline']
                }
            )
            created_comps.append(comp)
            if created:
                self.stdout.write(f"Created competition: {comp.title}")

        # 3. Submissions
        with open(base_path / 'sample_submissions.json', 'r') as f:
            subs_data = json.load(f)

        for s_data in subs_data:
            user = created_users[s_data['user_index']]
            comp = created_comps[s_data['competition_index']]
            
            # Check if submission exists
            if not Submission.objects.filter(user=user, competition=comp).exists():
                sub = Submission.objects.create(
                    user=user,
                    competition=comp,
                    answers=s_data['answers']
                )
                
                # Score
                score_input = {
                    "answers": sub.answers,
                    "cgpa": user.profile.cgpa
                }
                result = score_submission(score_input)
                sub.ai_score = result['ai_score']
                sub.save()
                
                self.stdout.write(f"Created submission for {user.username} in {comp.title}")

        # 4. Update Ranks
        self.stdout.write("Assigning ranks...")
        assign_ranks(Submission.objects.all())

        self.stdout.write(self.style.SUCCESS('Successfully seeded data'))
