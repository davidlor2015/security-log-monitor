from collections import Counter
from typing import List, Dict
from events import SecurityEvent

FAILED = "FAILED_LOGIN"

def detect_bruteforce(
        events: List[SecurityEvent],
        threshold: int = 5,
) -> List[Dict]:
    """
    Docstring for detect_bruteforce
    
    :param events: Description
    :type events: List[SecurityEvent]
    :param threshold: Description
    :type threshold: int
    :return: Description
    :rtype: List[Dict]
    """
    failed_events = [e for e in events if e.event_type == FAILED]

    by_ip = Counter(e.ip for e in failed_events if e.ip)
    by_user = Counter(e.user for e in failed_events if e.user)

    alerts = []

    for ip, count in by_ip.items():
        if count >= threshold:
            alerts.append({
                "type": "BRUTE_FORCE_IP",
                "ip": ip,
                "count": count,
                "severity": "high",
            })
    
    for user, count in by_user.items():
        if count >= threshold:
            alerts.append({
                "type": "BRUTE_FORCE_USER",
                "user": user,
                "count": count,
                "severity": "high",
            })
    
    return alerts