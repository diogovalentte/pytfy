import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../"))


@pytest.fixture()
def domain():
    return os.environ.get("NTFY_DOMAIN")


@pytest.fixture()
def topic():
    return os.environ.get("NTFY_TEST_TOPIC")


@pytest.fixture()
def token():
    return os.environ.get("NTFY_TOKEN")
