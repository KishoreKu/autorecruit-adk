from datetime import datetime

pipeline_events = []

def log_pipeline_event(session_id: str, stage: str, payload: dict):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "stage": stage,
        "payload": payload,
    }
    pipeline_events.append(event)
    return event
