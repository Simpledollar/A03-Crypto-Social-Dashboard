from dashboard import app

def test_flask_app_exists():
    # Kiểm tra Flask app có tồn tại
    assert app is not None

def test_math_example():
    # Kiểm thử logic nhỏ
    assert 2 + 2 == 4
