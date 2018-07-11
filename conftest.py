def pytest_addoption(parser):
    parser.addoption('--type', default='chrome')
    parser.addoption('--env', default='local')