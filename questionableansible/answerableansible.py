from jinja2 import Template

class AnswerableAnsible():

    @staticmethod
    def runAnswer():
        run = "ansible-playbook /create.yml"
        import subprocess
        process = subprocess.Popen(run.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        return output

    _ANS = runAnswer.__func__()

    def answerableansible(data):
        credentials_file = "{{ information.credentials }}"

        playbook = """
- name: Create some GCE Instances
  hosts: localhost
  vars:
    service_account_email: "{{ information.service_account_email }}"
    credential_file: "credentials.json"
    project_id: "{{ information.project_id }}"
  tasks:
    - name: create instances
      gce:
        instance_names: {{ information.instance_names }}
        zone: {{ information.zone }}
        machine_type: {{ information.machine_type }}
        image: {{ information.image }}
        image_family: {{ information.image_family }}
        disk_auto_delete: {{ information.disk_auto_delete }}
        disk_size: {{ information.disk_size }}
        disks: {{ information.disks }}
        external_ip: {{ information.external_ip }}
        external_projects: {{ external_projects }}
        ip_forward: {{ information.ip_forward }}
        machine_type: {{ information.machine_type }}
        metainformation: {{ information.metainformation }}
        name: {{ information.name }}
        network: {{ information.network }}
        num_instances: {{ information.num_instances }}
        persistent_boot_disk: {{ information.persistent_boot_disk }}
        preemptible: {{ information.preemptible }}
        project_id: {{ information.project_id }}
        service_account_email: {{ service_account_email }}
        state: {{ information.state }}
        subnetwork: {{ information.subnetwork }}
        """



        cred_tm = Template(credentials_file)
        cred_file = cred_tm.render(information=data)
        playbook_tm = Template(playbook)
        playbook_file = playbook_tm.render(information=data)

        file1 = open("/credentials.json","w")
        file1.write(cred_file)
        file1.close()

        file2 = open("/create.yml","w")
        file2.write(playbook_file)
        file2.close()

        return answerableansible.runAnswer()

