from django.db import models


class Module(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'


class ActionPermission(models.Model):
    module = models.ForeignKey(Module, blank=False, null=False, on_delete=models.CASCADE)
    method = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.module.name}.{self.method}"

    class Meta:
        verbose_name = 'Action Permission'
        verbose_name_plural = 'Action Permissions'
        constraints = [
            models.UniqueConstraint(fields=['module', 'method'], name='actionpermission_module_method')
        ]


class GroupActionPermission(models.Model):
    group = models.ForeignKey("auth.Group", null=True, blank=False, on_delete=models.CASCADE)
    permission = models.ForeignKey(ActionPermission, blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Group Action Permission'
        verbose_name_plural = 'Group Action Permissions'


class UserActionPermission(models.Model):
    user = models.ForeignKey("auth.User", null=True, blank=False, on_delete=models.CASCADE)
    permission = models.ForeignKey(ActionPermission, blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User Action Permission'
        verbose_name_plural = 'User Action Permissions'
