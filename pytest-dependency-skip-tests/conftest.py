import pytest
from pytest_dependency import DependencyManager


#
# def pytest_addoption(parser):
#     # parser.addoption("--dvi", action="store", default="all", required=False, help="description")
#     parser.addoption("--config", action="store", default="gibprod", help="Name of the config file to pass to test functions")
#     parser.addoption("--games", action="store", default="1", help="Number of games to pass to test functions")


def pytest_collection_modifyitems(session, config, items):
    modules = (item.getparent(pytest.Module) for item in items)
    marked_modules = {m for m in modules if m.get_closest_marker('depend_on_failures')}
    for module in marked_modules:
        module.dependencyManager = FailureDepManager(scope="module")


class FailureDepManager(DependencyManager):

    def checkDepend(self, depends, item):
        for i in depends:
            if i in self.results:
                if self.results[i].isSuccess():
                    pytest.skip('%s depends on failures in %s' % (item.name, i))
                    break