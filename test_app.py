def test_positive_case():
    assert calculate_quote(100, 20) == 120



def test_invalid_input():
    try:
        calculate_quote(-100, 10)
        assert False
    except ValueError:
        assert True
