Frontend (Static HTML/JS)
       |
       v (HTTP JSON)
       |
Backend (Django REST Framework)
       |
       +--> Auth (Token)
       |
       +--> Database (SQLite)
       |
       +--> AI Module (ai/score.py)
              |
              +--> score_submission()
