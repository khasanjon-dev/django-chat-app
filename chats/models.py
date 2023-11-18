from django.contrib.auth.models import User
from django.db.models import Model, CharField, ManyToManyField


class Room(Model):
    name = CharField(max_length=250)
    online = ManyToManyField(User, blank=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'


