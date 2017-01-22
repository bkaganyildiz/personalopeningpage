from dominate.tags import *
import urllib2
import json

class XkcdView(object):
    _description = "Fetches xkcd comics"
    _attributes = [
        ('currentComic', 'dict'),
        ('instance_id', 'string')
    ]
    _methods = [('fetch_comic', 'Fetches Current Comic')]

    def description(self):
        return self._description

    def attributes(self):
        return self._attributes

    def __getitem__(self, item):
        for attribute in self._attributes:
            if attribute[0] == item:
                return getattr(self, item)

        raise AttributeError(self.__class__.__name__ + " object has no attribute '" + str(item) + "'")

    def __setitem__(self, key, value):
        for attribute in self._attributes:
            if attribute[0] == key:
                setattr(self, key, value)
                return

        raise AttributeError(self.__class__.__name__ + " object has no attribute '" + key + "'")

    def methods(self):
        return self._methods

    def fetch_comic(self, num):
        response = urllib2.urlopen('https://xkcd.com/{}/info.0.json'.format(num))
        resp = json.loads(response.read())

        self.currentComic = resp
        return self.currentComic

    def execute(self):
        print self.currentComic
        xkcd = div(
            h3(self.currentComic['title'], cls="text-center"),
            img(src=self.currentComic['img']),
            div(
                div(
                    button("Prev", cls="btn btn-default", id="xkcd_prev"),
                    cls="col-sm-6",
                    align="left"
                ),
                div(
                    button("Next", cls="btn btn-default", id="xkcd_next"),
                    cls="col-sm-6",
                    align="right"
                )
            ),
            script("""
                $(document).ready(function fetch(){
                    var latestComic = """ + str(self.currentComic['num']) + """;
                    var currentComic = """ + str(self.currentComic['num']) + """;
                    $('#xkcd_prev').click(function () {
                        jQuery.ajax({
                            type: 'POST',
                            async: true,
                            data:  JSON.stringify({ 'key' : '""" + self.instance_id + """', 'num': currentComic-1}),
                            contentType: 'application/json; charset=utf-8',
                            url: '/{{ user.username }}/fetchcomic',
                            success: function (response) {
                                $('#xkcd_""" + self.instance_id + """ h3').text(response['comic']['title']);
                                $('#xkcd_""" + self.instance_id + """ img').attr('src', response['comic']['img']);
                                currentComic--;
                            },
                            error: function (err){
                                alert(err.responseText);
                            }
                        });
                    });
                    $('#xkcd_next').click(function () {
                        jQuery.ajax({
                            type: 'POST',
                            async: true,
                            data:  JSON.stringify({ 'key' : '""" + self.instance_id + """', 'num': currentComic+1}),
                            contentType: 'application/json; charset=utf-8',
                            url: '/{{ user.username }}/fetchcomic',
                            success: function (response) {
                                $('#xkcd_""" + self.instance_id + """ h3').text(response['comic']['title']);
                                $('#xkcd_""" + self.instance_id + """ img').attr('src', response['comic']['img']);
                                currentComic++;
                            },
                            error: function (err){
                                alert(err.responseText);
                            }
                        });
                    });
                });
            """),
            cls="panel panel-defualt",
            align="center",
            id="xkcd_" + self.instance_id
        )

        return xkcd

    def __str__(self):
        return self.description()

    def __init__(self, instance_id):
        self.instance_id = instance_id

        response = urllib2.urlopen('https://xkcd.com/info.0.json')
        resp = json.loads(response.read())

        self.currentComic = resp

