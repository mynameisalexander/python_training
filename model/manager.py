class Manager:

    def __init__(self, app, session, group, contact):
        self.session = session(app)
        self.group = group(app)
        self.contact = contact(app)

# это будет удалено