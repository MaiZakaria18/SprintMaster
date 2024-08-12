from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission


def create_groups(sender, **kwargs):
    admin_group, created = Group.objects.get_or_create(name='Admin')
    project_manager_group, created = Group.objects.get_or_create(
        name='Project Manager')
    team_member_group, created = Group.objects.get_or_create(
        name='Team Member')


def assign_permissions(sender, **kwargs):
    project_manager_group = Group.objects.get(name='Project Manager')
    add_task_permission = Permission.objects.get(codename='add_task')
    project_manager_group.permissions.add(add_task_permission)

    admin_group = Group.objects.get(name='Admin')
    admin_group.permissions.set(Permission.objects.all())


class UserAppConfig(AppConfig):
    name = 'user'

    def ready(self):
        create_groups(self)
        assign_permissions(self)
