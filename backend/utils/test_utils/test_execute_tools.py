
from backend.utils.execute_tools import ExecuteTools


class TestExecuteTools:
    def test_get_jobs(self):
        print(ExecuteTools.get_jobs())

    def test_invoke(self):
        ExecuteTools.invoke()
        print(ExecuteTools.invoke())