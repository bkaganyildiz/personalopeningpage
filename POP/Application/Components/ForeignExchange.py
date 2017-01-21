from dominate.tags import *
import json
import datetime


class ForeignExchange(object):
    _description = "Fetch Current Exchange Rates"
    _attributes = [
        ('fetch_url', 'string'),
        ('rate', 'int')
    ]
    _methods = [
        ('set_url', 'Set API URL (default http://api.fixer.io/latest)'),
        ('get_url', 'Get API URL'),
        ('set_rate', 'Set Refresh Rate'),
        ('get_rate', 'Get Refresh Rate'),
    ]

    def description(self):
        return self._description

    def attributes(self):
        return self._attributes

    def __getitem__(self, item):
        for attribute in self._attributes:
            if attribute[0] == item:
                return getattr(self, item)

        raise AttributeError(self.__class__.__name__ + " object has no attribute '" + item + "'")

    def __setitem__(self, key, value):
        for attribute in self._attributes:
            if attribute[0] == key:
                setattr(self, key, value)
                return

        raise AttributeError(self.__class__.__name__ + " object has no attribute '" + key + "'")

    def methods(self):
        return self._methods

    def __str__(self):
        return self.description()

    def __init__(self, url="http://api.fixer.io/latest", rate=10):
        self.url = url
        self.rate = rate

    def set_url(self, url):
        self.fetch_url = url

    def get_url(self):
        return self.fetch_url

    def set_rate(self, rate):
        self.rate = rate

    def get_rate(self):
        return self.rate

    def execute(self):
        for_exc = div(
            h1("Foreign Exchange Rate"),
            table(
                thead(tr(th("USD"), th("EUR"))),
                tbody(tr(td("", id="usd"), td("", id="eur"))),
                id="for_exc"
            ),
            script("""
                $(document).ready(function fetch(){
                    $.ajax({
                        type: 'GET',
                        async: true,
                        url: 'http://api.fixer.io/latest?base=TRY',
                        success: function(response){
                            $('#for_exc #usd').text((1/response['rates']['USD']).toFixed(3)),
                            $('#for_exc #eur').text((1/response['rates']['EUR']).toFixed(3)),
                            setTimeout(fetch, 5000);
                        },
                        error: function(err){
                            alert(err.responseText);
                        }
                    });
                });
            """))

        return for_exc
