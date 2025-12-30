from parser import parse_auth_log
from pathlib import Path


FIXTURE_PATH = Path(__file__).parent / "fixtures_auth.log"
def test_failed_logins():
    results = parse_auth_log("tests/fixtures_auth.log")
    failed = results["failed_logins"]

    assert failed[("admin", "10.0.0.5")] == 2

def test_accepted_logins():
    results = parse_auth_log("tests/fixtures_auth.log")
    accepted = results["accepted_logins"]

    assert accepted[("david", "127.0.0.1")] == 1

def test_sudo_usage():
    results = parse_auth_log("tests/fixtures_auth.log")
    sudo = results["sudo_usage"]

    assert sudo["david"] == 1