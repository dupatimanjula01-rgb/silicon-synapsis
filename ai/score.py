
import json

def score_submission(submission):
    """
    Score a submission based on rules.
    submission dict should contain: 'answers' (str), 'cgpa' (float, optional).
    Returns: { "ai_score": float, "remarks": str }
    """
    answers = submission.get('answers', '')
    cgpa = submission.get('cgpa')
    
    score = 50.0 # Base score
    remarks = ["Base score: 50"]

    # Rule 1: Length > 200
    if len(answers) > 200:
        score += 10
        remarks.append("+10 (Detailed answer)")
    
    # Rule 2: Keywords
    keywords = ['innovation', 'scalability', 'efficiency', 'ai', 'user']
    found_keywords = [k for k in keywords if k in answers.lower()]
    if found_keywords:
        score += 10
        remarks.append(f"+10 (Keywords found: {', '.join(found_keywords)})")
    
    # Rule 3: CGPA > 6.0
    if cgpa:
        try:
            cgpa_val = float(cgpa)
            if cgpa_val > 6.0:
                bonus = (cgpa_val - 6.0) * 5
                score += bonus
                remarks.append(f"+{bonus:.1f} (CGPA Bonus)")
        except ValueError:
            pass

    # Clamp
    score = max(0, min(100, score))
    
    return {
        "ai_score": round(score, 2),
        "remarks": "; ".join(remarks)
    }

def assign_ranks(submissions_queryset):
    """
    Takes a QuerySet or list of Submission objects.
    Sorts them by score (desc) and assigns rank.
    Returns the modified list (objects are saved if they are Django models).
    """
    # Sort by score desc, then submitted_at asc
    sorted_subs = sorted(list(submissions_queryset), key=lambda x: (-x.ai_score if x.ai_score is not None else 0, x.submitted_at))
    
    rank = 1
    for sub in sorted_subs:
        if sub.ai_score is not None:
             sub.ai_rank = rank
             rank += 1
        else:
            sub.ai_rank = None # Should not happen if scored
        sub.save()
    
    return sorted_subs
