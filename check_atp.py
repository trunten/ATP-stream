#!/usr/bin/env python3
"""Check ATP's publicly documented live-status JSON endpoint once.

Exit: 0=offline, 10=live, 2=unknown/error.
Useful for local testing; no GitHub Actions scheduling is configured.
"""
import json
import sys
from html.parser import HTMLParser
from urllib.request import Request, urlopen

URL = "https://atp.fm/livestream_status"

class AudioSource(HTMLParser):
    def __init__(self):
        super().__init__()
        self.audio = False
        self.found = False

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if tag == "audio":
            self.audio = True
            self.found |= bool(props.get("src"))
        if tag == "source" and self.audio:
            self.found |= bool(props.get("src"))

    def handle_endtag(self, tag):
        if tag == "audio":
            self.audio = False

def check():
    request = Request(URL, headers={"User-Agent": "ATP-Stream-Checker/1.0",
                                    "Cache-Control": "no-cache"})
    try:
        with urlopen(request, timeout=12) as response:
            data = json.load(response)
        if not isinstance(data, dict) or type(data.get("live")) is not bool:
            raise ValueError("live field is missing or not a boolean")
        if not data["live"]:
            print("OFFLINE")
            return 0
        player = data.get("player")
        if not isinstance(player, str):
            raise ValueError("live=true without player HTML")
        parser = AudioSource()
        parser.feed(player)
        if not parser.found:
            raise ValueError("live=true without an audio source")
        print("LIVE: an audio source is present")
        return 10
    except Exception as error:
        print("UNKNOWN:", type(error).__name__, str(error), file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(check())
