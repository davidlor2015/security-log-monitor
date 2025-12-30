import re
from collections import Counter

FAILED_LOGIN_RE = re.compile(
    r"Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>[\d.]+)"
)

ACCEPTED_LOGIN_RE = re.compile(
    r"Accepted password for (?P<user>\S+) from (?P<ip>[\d.]+)"
)

SUDO_RE = re.compile(
    r"sudo: +(?P<user>\S+)"
)

def parse_auth_log(path):
    failed = Counter()
    accepted = Counter()
    sudo = Counter()

    with open(str(path), "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if match := FAILED_LOGIN_RE.search(line):
                failed[(match["user"], match["ip"])] += 1
            
            elif match := ACCEPTED_LOGIN_RE.search(line):
                accepted[(match["user"], match["ip"])] += 1
            
            elif match := SUDO_RE.search(line):
                sudo[(match["user"])] += 1
    
    return {
        "failed_logins": failed,
        "accepted_logins": accepted,
        "sudo_usage": sudo,
    }