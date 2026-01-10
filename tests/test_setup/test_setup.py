"""_summary_
This module contains tests to test if the setup is correct.
"""


def test_setup(driver, frontend_base_url):
  """Test if the setup is correct by navigating to the base URL."""
  driver.get(frontend_base_url)
  assert driver.title == "UTEPs", "Setup test failed: Title does not match."
