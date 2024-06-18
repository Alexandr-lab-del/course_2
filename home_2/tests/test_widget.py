# import pytest
#
# from home_2.src.widget import mask_account_card, get_data
#
#
# @pytest.mark.parametrize("input_data, expected_output", [
#     ("Счет 73654108430135874305", "Счет **4305"),
#     ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
#     ("Maestro 7000 7922 8960 6361", "Maestro 7000 79** **** 6361"),
# ])
# def test_mask_account_card(input_data: str, expected_output: str):
#     assert mask_account_card(input_data) == expected_output
#
#
# @pytest.mark.parametrize("input_data, expected_output", [
#     ("2018-07-11T02:26:18.671407", "11.07.2018"),
# ])
# def test_get_data(input_data, expected_output):
#     assert get_data(input_data) == expected_output
