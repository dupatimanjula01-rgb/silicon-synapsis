# Silicon Synapsis Platform

## Description
Admin-controlled, AI-enabled college club platform for "Silicon Synapsis".
- **Admin**: Creates competitions & forms, views ordered participant lists, exports CSV.
- **Student**: Submits forms for competitions.
- **AI**: Assigns `ai_score` and `ai_rank` to submissions based on rules (extensible).

## Tech Stack
- **Backend**: Django + Django REST Framework (SQLite for dev)
- **Frontend**: Static HTML/CSS/JS (Professional, Mobile-first)
- **AI**: Python script (`ai/score.py`) - Rule-based logic placeholder.
- **Database**: SQLite (default for development)

## Project Structure
- `backend/`: Django project root.
- `frontend/`: Static frontend files.
- `ai/`: AI logic module.
- `docs/`: Documentation.
- `tools/`: Utility scripts (e.g., export CSV).
- `sample_data/`: JSON fixtures for testing.

## How to Run (Development)

1.  **Setup Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Database Setup**
    ```bash
    cd backend
    python manage.py migrate
    ```

4.  **Seed Data (Optional but Recommended)**
    Populate the database with sample users, competitions, and submissions.
    ```bash
    python manage.py seed_data
    ```

5.  **Run Backend Server**
    ```bash
    python manage.py runserver
    # Server runs at http://127.0.0.1:8000/
    ```

6.  **Run Frontend**
    - You can serve the `frontend/` folder using any static server.
    - Example using Python:
      ```bash
      # From project root
      python -m http.server 5500 --directory frontend
      # Open http://127.0.0.1:5500 in your browser
      ```
    - Or simply open `frontend/index.html` in your browser (though APIs might need CORS handling if file protocol is used, keeping them on localhost http is better).

## Endpoints Summary
- **Auth**: `/api/auth/login/`, `/api/auth/register/`
- **Competitions**: `/api/competitions/` (GET list, POST create-admin)
- **Submissions**: `/api/submissions/` (POST submit), `/api/submissions/{comp_id}/` (GET admin)
- **Admin**: `/api/admin/participants/` (GET sorted list)
