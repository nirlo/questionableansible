from django import forms 
from . import models

class GCPInfo(forms.ModelForm):
    class Meta:
        model = models.GCPInfo
        fields = [
            'auth'
        ]

class GCEInstance(forms.Form):
    states = (
        ('active', 'active'),
        ('present', 'present'),
        ('absent', 'deleted'), 
        ('started', 'started'),
        ('stopped', 'stopped'),
        ('terminated', 'terminated')
    )
    instance_name = forms.CharField()
    disk_auto_delete = forms.BooleanField(initial=True)
    disk_size = forms.IntegerField(initial=10)
    disks = forms.CharField(max_length=1000)
    external_ip = forms.CharField(initial="ephemeral", max_length=100)
    exernal_projects = forms.CharField(max_length=1000)
    image = forms.CharField(initial="debian-8", max_length=100)
    image_family = forms.CharField(max_length=100)
    instance_names = forms.CharField(max_length=1000, initial="example_name, example_name1")
    ip_forward = forms.BooleanField(initial=False)
    machine_type = forms.CharField(initial="n1-standard-1")
    metadata = forms.CharField(max_length=1000)
    name = forms.CharField(required=False)
    network = forms.CharField(initial="initial", max_length=100)
    num_instances = forms.IntegerField(initial=1)
    persistent_boot_disk = forms.BooleanField(initial=False)
    preemptible = forms.BooleanField(initial=False)
    project_id = forms.CharField(required=False, max_length=100)
    service_account_email = forms.CharField(required=False, max_length=100)
    service_account_permissions = forms.CharField(max_length=1000)
    state = forms.CharField(max_length=1000, initial='present')
    subnetwork = forms.CharField(required=False, max_length=100)
    zone = forms.CharField(initial='us-central1-a')
