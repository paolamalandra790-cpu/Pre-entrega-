import pytest

@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    rep = yield
    if rep.when == "call" and rep.outcome == "failed":
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot("foto_cuando_fallo.png")
            print("Se guardó la foto porque falló")
    return rep
