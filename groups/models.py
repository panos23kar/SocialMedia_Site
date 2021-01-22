from django.db import models.sl
from django.utils.text import slugify
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()


class Group(models.Model):
    pass
    


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
    



