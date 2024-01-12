import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))

from src.pytfy import NtfyPublisher


def test_post(domain, topic, token):
    ntfy = NtfyPublisher(domain=domain, topic=topic, token=token)
    ntfy.post(
        "just a test from the pytfy library",
        "pytfy library test",
        click="https://github.com/diogovalentte/pytfy",
    )
