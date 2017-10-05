from django_propeller.navbar import NavBar, NavBarLinkItem, NavBarDropDownItem, NavBarDropDownDivider


class CustomItem(object):
    html = ""

    def __init__(self, html):
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


class MainNavBar(NavBar):
    brandname = "MediaCatalogue"
    # brandurl = reverse('index')
    items = [
        NavBarLinkItem("Home", "index"),
        NavBarLinkItem("Images", "images"),
        NavBarLinkItem("Videos", "videos"),
        NavBarLinkItem("Audio", "audio"),
        NavBarLinkItem("Settings", "settings"),
        CustomItem(search_box),
    ]