from .dns import DNSChecker


def get_prepared_checkers():
    checkers = []
    dns_checker = DNSChecker()
    try:
        dns_checker.startup()
        checkers.append(dns_checker)
    except Exception as e:
        print("Unhandled exception")
        raise e

    return checkers
