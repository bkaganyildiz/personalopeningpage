from dominate.tags import *
import json
import datetime


class Post(object):
    _description = "Create blog posts "
    _attributes = [
        ('blog_id', 'string'),
        ('content', 'string')
    ]
    _methods = [
        ('setContent', 'Set Content'),
        ('setBlogid', 'Set Blog ID'),
        ('changeContent', 'Change Content'),
        ('changeBlogid', 'Change Blog ID'),
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

    def __init__(self,blog_id="",content=""):
        self.blog_id = blog_id
        self.content = content

    def setBlogid(self, blog_id="") :
        self.blog_id = blog_id

    def changeBlogid(self, blog_id="") :
        self.blog_id = blog_id

    def setContent(self, content="") :
        self.content = content
        print "Content: " , self.content
        return self.content

    def changeContent(self, content="") :
        self.content = content

    def execute(self):
        h = div(
            h1("POST"),
            div(
                textarea(
                    id="post_content",
                    rows=4, cols=50
                ),
                button("POST", name="Post", id="post_method"),
            ),
            script("""$('#post_method').click(function () {
                jQuery.ajax({
                    type: 'POST',
                    async: true,
                    url: '/{{ user.username }}/postblog',
                    data:  JSON.stringify({ 'key' : '""" + self.blog_id + """', 'content': $('#post_content').val()}),
                    contentType: 'application/json; charset=utf-8',
                    success: function (response) {
                        $('#blog_"""+self.blog_id+"""').text(response['content']);
                    },
                    error: function (err){
                        alert(err.responseText);
                    }
                });
            });"""))
        return h
