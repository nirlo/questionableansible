from django.db import models

# Create your models here.
class GCPInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auth = models.TextField()

class gce_base(models.Model):
    instance_name = models.CharField()
    disk_auto_delete = BooleanField(default=True)
    disk_size = IntegerField(default=10)
    disks = ()
    external_ip = CharField(default="ephemeral", max_length=100)
    exernal_projects = ()
    image = CharField(default="debian-8", max_length=100)
    image_family = CharField(max_length=100)
    instance_name = ()
    ip_forward = BooleanField(default=False)
    machine_type = CharField(default="n1-standard-1")
    metadata = ()
    name = CharField(null=True)
    network = CharField(default="default", max_length=100)
    num_instances = IntegerField(default=1)
    persistent_boot_disk = BooleanField(default=False)
    preemptible = BooleanField(default=False)
    project_id = CharField(null=True, max_length=100)
    service_account_email = CharField(null=True, max_length=100)
    service_account_permissions = TextField()