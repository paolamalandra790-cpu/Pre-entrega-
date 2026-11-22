import subprocess

def run_behave(feature_file):
    result = subprocess.run(
        ["python", "-m", "behave", feature_file, "--no-capture"],
        capture_output=True,
        text=True
    )
    return result

def test_login_feature():
    result = run_behave("features/login.feature")
    assert result.returncode == 0, f"Login falló:\n{result.stdout}\n{result.stderr}"

def test_cart_feature():
    result = run_behave("features/cart.feature")
    assert result.returncode == 0, f"Cart falló:\n{result.stdout}\n{result.stderr}"
