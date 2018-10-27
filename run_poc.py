from checkers.manager import get_prepared_checkers


for checker in get_prepared_checkers():
    result = checker.check("tr.wikipedia.com")
