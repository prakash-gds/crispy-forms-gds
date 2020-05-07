"""
Tests to verify date inputs are rendered correctly.

"""
import datetime
import os

from tests.forms import DateInputForm
from tests.utils import TEST_DIR, parse_contents, parse_form


RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "date_input")

# IMPORTANT: The test results are totally dependent on the require_all_fields
# attribute on the DateInputField. Test tests here use require_all_fields = False
# so there is a clear separation between field level errors and errors from the
# day, month and year fields.


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = DateInputForm(initial={"date": datetime.date(year=2007, month=11, day=12)})
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_field_error_attributes():
    """Verify the parent field level error messages are displayed correctly."""
    form = DateInputForm(data={"date_0": "", "date_1": "", "date_2": ""})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(RESULT_DIR, "field_errors.html")


def test_subfield_error_attributes():
    """Verify the error messages for the individual fields are displayed correctly."""
    form = DateInputForm(data={"date_0": "a", "date_1": "11", "date_2": ""})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(RESULT_DIR, "subfield_errors.html")
