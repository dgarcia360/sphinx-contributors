from docutils import nodes


class Contributor:
    def __init__(self, login, url, contributions=0, avatar_url="", name="", email="", anonymous = True):
        self.contributions = contributions
        self.login = login
        self.url = url
        self.avatar_url = avatar_url
        self.name = name
        self.email = email
        self.anonymous = anonymous

    @property
    def display_name(self):
        return self.name or self.login

    def update(self, data):
        if isinstance(data, Contributor) and self.login == data.login:
            self.contributions += data.contributions
            self.url = data.url if data.url else self.url
            self.avatar_url = data.avatar_url if data.avatar_url else self.avatar_url
            self.name = data.name if data.name else self.name
            self.email = data.email if data.email else self.email
            self.anonymous = data.anonymous if data.anonymous else self.anonymous

    def build(self, class_name, options = {}):
        container_class = class_name + "_contributor"
        image_class = container_class + "__image"
        username_class = container_class + "__username"
        contributions_class = container_class + "__contributions"
        show_login = options.get('show_login', False)
        show_contributions = options.get('show_contributions', False)

        node_container = nodes.container(classes=[container_class])

        if options.get('show_avatars', False):
            if self.avatar_url:
                node_image = nodes.image(
                    uri=self.avatar_url,
                    alt=self.display_name if not show_login else self.login,
                    classes=[image_class],
                )
                node_image_link = nodes.reference("", refuri=self.url)
                node_image_link += node_image
                node_container += node_image_link

            if options.get('avatars_only', False):
                return node_container

        node_username = nodes.paragraph(classes=[username_class])

        login = self.login.replace('@', ' [at] ')  # replace @ by [at]

        if self.url or self.email:
            url = self.url if self.url else f"mailto:{self.email}"
            node_username += nodes.reference(text=self.display_name if not show_login else login,
                                         refuri=url)
        else:
            node_username += nodes.Text(self.display_name if not show_login else login)

        node_container += node_username

        if show_contributions and self.contributions:
            node_contributions = nodes.paragraph(classes=[contributions_class])
            node_contributions += nodes.Text(
                str(self.contributions)
                + (" contributions" if self.contributions != 1 else " contribution"),
            )
            node_container += node_contributions
        return node_container


class ContributorsRepository:
    def __init__(
        self,
        contributors,
        options = {},
        config = {}
    ):
        reverse = options.get("reverse", False)
        exclude = options.get('exclude', [])
        sorted_contributors = sorted(
            [c for c in contributors if c.login not in exclude],
            key=lambda c: c.contributions,
            reverse=reverse,
        )
        limit = options.get("limit", None)
        self.contributors = (
            sorted_contributors[:limit] if limit else sorted_contributors
        )
        self.options = options


    def build(self, class_name):
        list_class = class_name + "_list"
        item_class = list_class + "__item"

        node_container = nodes.container(classes=[class_name])

        if self.options.get('show_avatars', False):
            node_container["classes"].append(class_name + "--avatars")

        node_list = nodes.bullet_list(classes=[list_class])

        for contributor in self.contributors:
            node_item = nodes.list_item(classes=[item_class])
            node_item += contributor.build(class_name, self.options)
            node_list += node_item
        node_container += node_list

        return node_container


