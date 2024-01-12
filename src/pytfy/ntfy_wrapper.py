import requests


class NtfyPublisher:
    def __init__(self, domain, topic, token) -> None:
        self.domain = domain
        self.topic = topic
        self.token = token

    def post(
        self,
        message,
        title: str | None = None,
        priority=None,
        tags: list | None = None,
        click: str | None = None,
    ):
        headers = {}
        headers["Authorization"] = f"Bearer {self.token}"

        if title:
            headers["Title"] = title
        if priority:
            headers["Priority"] = priority
        if tags:
            headers["Tags"] = ",".join(tags)
        if click:
            headers["Click"] = click

        url = f"{self.domain}/{self.topic}"
        requests.post(
            url,
            data=message,
            headers=headers,
        )
