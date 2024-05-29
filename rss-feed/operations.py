"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import feedparser
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('rss-feed')


class RSSFeed(object):
    def __init__(self, config):
        pass


def get_indicators(config, params):
    try:
        feed = feedparser.parse(params.get('url'))
        if feed.get("bozo"):
            feed.pop("bozo_exception")
        return feed
    except Exception as err:
        raise ConnectorError(str(err))


def check_health(config):
    return True


operations = {
    'get_indicators': get_indicators
}