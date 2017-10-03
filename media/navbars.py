from django_propeller.navbar import NavBar, NavBarLinkItem, NavBarDropDownItem, NavBarDropDownDivider


class MainNavBar(NavBar):
    brandname = "MediaCatalogue"
    # brandurl = reverse('index')
    items = [
        NavBarLinkItem("Home", "index"),
        NavBarLinkItem("Images", "images"),
        NavBarLinkItem("Videos", "videos"),
    ]
