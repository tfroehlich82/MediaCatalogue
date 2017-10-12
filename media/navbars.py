from django_propeller.navbar import NavBar, NavBarLinkItem, NavBarDropDownItem, NavBarDropDownDivider
from django_propeller.utils import render_tag, add_css_class
from django_propeller.text import text_concat
from django.utils.safestring import mark_safe


class CustomItem(object):
    html = ""

    def __init__(self, html=""):
        self.html = html

    def as_html(self):
        return self.html


search_box = """
<form class="navbar-form navbar-left">
    <div class="form-group">
        <input id="searchBox" type="text" class="form-control" placeholder="Search">
    </div>
    <button type="submit" class="btn btn-default" onclick="doSearch($('#searchBox').val());">Submit</button>
</form>
"""


class ContextNavBar(NavBar):
    style_context = True

    def as_html(self):
        """Returns navbar as html"""
        tag = 'nav'
        classes = 'navbar'
        if self.style_inverse:
            classes = add_css_class(classes, 'navbar-inverse')
        if self.style_context:
            classes = add_css_class(classes, 'context-navbar')
        if self.style_static:
            classes = add_css_class(classes, 'navbar-static')
        else:
            classes = add_css_class(classes, 'navbar-top')
        classes = add_css_class(classes, 'pmd-navbar')
        classes = add_css_class(classes, 'pmd-z-depth')
        attrs = {'class': classes}
        content = self.render_content()
        content = text_concat(content, '<div class="pmd-sidebar-overlay"></div>')
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )

    def render_header(self):
        """Returns navbar header as html"""
        tag = 'div'
        attrs = {'class': 'navbar-header'}
        content = self.render_toggle()
        content = text_concat(content, self.brandname)
        return render_tag(tag, attrs=attrs, content=mark_safe(content), )


class MainNavBar(NavBar):
    brandname = "MediaCatalogue"
    items = [
        NavBarLinkItem("Home", "index"),
        NavBarLinkItem("Images", "images"),
        NavBarLinkItem("Videos", "videos"),
        NavBarLinkItem("Audio", "audio"),
        NavBarLinkItem("Settings", "settings"),
        CustomItem(search_box),
    ]


class ImageContextNavBar(ContextNavBar):
    brandname = "<div class='navbar-brand'><i class='material-icons' style='margin-top: 10px;'>insert_photo</i></div>" \
                "<div class='navbar-brand'>&nbsp;<span>Images</span></div>"
    style_inverse = False
    items = [
        NavBarDropDownItem(name="Organize", items=[
            NavBarLinkItem("Reorganize Structure", "images-reorganize"),
        ]),
        NavBarLinkItem("Find similar", "index"),
        NavBarLinkItem("Edit", "index"),
    ]


class VideoContextBar(ContextNavBar):
    brandname = "<div class='navbar-brand'><i class='material-icons' style='margin-top: 10px;'>movie</i></div>" \
                "<div class='navbar-brand'>&nbsp;<span>Videos</span></div>"
    style_inverse = False
    items = [
        NavBarDropDownItem(name="Organize", items=[
            NavBarLinkItem("Reorganize Structure", "videos-reorganize"),
        ]),
        NavBarLinkItem("Find similar", "index"),
        NavBarLinkItem("Edit", "index"),
    ]


class AudioContextBar(ContextNavBar):
    brandname = "<div class='navbar-brand'><i class='material-icons' style='margin-top: 10px;'>music_video</i></div>" \
                "<div class='navbar-brand'>&nbsp;<span>Audio</span></div>"
    style_inverse = False
    items = [
        NavBarDropDownItem(name="Organize", items=[
            NavBarLinkItem("Reorganize Structure", "audio-reorganize"),
        ]),
        NavBarLinkItem("Find similar", "index"),
        NavBarLinkItem("Edit", "index"),
    ]


class EmptyContextBar(ContextNavBar):
    pass


class ReorganizeContextBar(ContextNavBar):
    brandname = ""
    style_inverse = False
    items = [
        # NavBarLinkItem("Edit Patterns", "index"),
    ]

    def __init__(self, page_context):
        self.brandname = "<div class='navbar-brand'>&nbsp;<span>Reorganize %s</span></div>" % page_context
