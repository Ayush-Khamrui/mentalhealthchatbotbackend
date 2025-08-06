from app.models.schemas import CheckupRequest, CheckupResponse
from app.services.gemini_service import get_gemini_score_and_response

def process_checkup(data: CheckupRequest, user):
    score, response = get_gemini_score_and_response(data.questions)
    return CheckupResponse(score=score, response=response)
