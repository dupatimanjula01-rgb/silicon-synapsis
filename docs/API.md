# API Documentation

## Authentication
Token-based authentication.
Header: `Authorization: Token <token_key>`

### POST /api/auth/register/
Body:
```json
{
    "username": "...",
    "email": "...",
    "password": "...",
    "cgpa": 8.5,        // optional
    "department": "CSE" // optional
}
```

### POST /api/auth/login/
Body:
```json
{
    "username": "...",
    "password": "..."
}
```
Returns: `{"token": "...", "is_admin": true/false}`

## Competitions

### GET /api/competitions/
List all competitions.

## Submissions

### POST /api/submissions/
Submit an entry.
Header: `Authorization: Token ...`
Body:
```json
{
    "competition_id": 1,
    "answers": "My innovative solution...",
    "cgpa": 9.0,         // updates profile if provided
    "department": "ECE"  // updates profile if provided
}
```
Returns: Submission object with `ai_score`.

### GET /api/submissions/?competition_id=1
(Admin) List submissions for a competition.

## Admin

### GET /api/admin/participants/
List all participants with ranking.
Params:
- `order_by`: `ai_score` (default), `ai_rank`, `cgpa`, `submitted_at`
- `order`: `desc` (default), `asc`

Returns:
```json
[
    {
        "rank": 1,
        "name": "user1",
        "dept": "CSE",
        "cgpa": 9.0,
        "score": 85.5,
        "submitted_at": "..."
    }
]
```
