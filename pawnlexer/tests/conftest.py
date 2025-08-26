import pytest
import datetime

from .context import *


class InternalError(Exception):
    pass


@pytest.fixture(scope='session')
def context(request):
    context = Context()
    yield context


def pytest_runtest_makereport(item, call) -> str | None:
    test_report = pytest.TestReport.from_item_and_call(item, call)
    if not call.when == 'call' or not test_report.outcome == 'failed':
        return

    longrepr = create_longrepr_fail(item, call)
    test_report.longrepr = longrepr
    return test_report


def clean_string(st: str) -> str:
    st = st.replace('\t', '').replace('\n', '').replace('   ', '')
    return st

def create_longrepr_fail(item, call) -> str:
    longrepr: list[str] = [f'Test failed {item.name}']
    longrepr.append(f'File {item.fspath}')
    longrepr.append(f'Assert message: {call.excinfo.value}')
    test_instance = item.instance
    if hasattr(test_instance, 'content'):
        longrepr.append(f'Test line: \n\t{test_instance.content.strip()}')
    if hasattr(test_instance, 'correct'):
        longrepr.append(f'Correct tokens: {clean_string(test_instance.correct.strip())}')
    if hasattr(test_instance, 'correct'):
        longrepr.append(f'Current tokens: {clean_string(' '.join(test_instance.tokenized))}')
    start = datetime.datetime.fromtimestamp(call.start).time().isoformat(timespec='milliseconds')
    longrepr.append(f'Start: {start}')
    stop = datetime.datetime.fromtimestamp(call.stop).time().isoformat(timespec='milliseconds')
    longrepr.append(f'Stop : {stop}')
    return '\n'.join(longrepr)