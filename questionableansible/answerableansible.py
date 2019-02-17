from jinja2 import Template

class AnswerableAnsible():

    credentials_file = "{{ data.credentials }}"

    playbook = """
- name: Create some GCE Instances
  hosts: localhost
  vars:
    service_account_email: "{{ data.service_account_email }}"
    credential_file: "credentials.json"
    project_id: "{{ data.project_id }}"
  tasks:
    - name: create instances
      gce:
        instance_names: {{ data.instance_names }}
        zone: {{ data.zone }}
        machine_type: {{ data.machine_type }}
        image: {{ data.image }}
        image_family: {{ data.image_family }}
        disk_auto_delete: {{ data.disk_auto_delete }}
        disk_size: {{ data.disk_size }}
        disks: {{ data.disks }}
        external_ip: {{ data.external_ip }}
        external_projects: {{ external_projects }}
        ip_forward: {{ data.ip_forward }}
        machine_type: {{ data.machine_type }}
        metadata: {{ data.metadata }}
        name: {{ data.name }}
        network: {{ data.network }}
        num_instances: {{ data.num_instances }}
        persistent_boot_disk: {{ data.persistent_boot_disk }}
        preemptible: {{ data.preemptible }}
        project_id: {{ data.project_id }}
        service_account_email: {{ service_account_email }}
        state: {{ data.state }}
        subnetwork: {{ data.subnetwork }}
    """

    

    def answerableansible(data):
        cred_tm = Template(credentials_file)
        cred_file = cred_tm.render(data)
        playbook_tm = Template(playbook)
        playbook_file = playbook_tm.render(data)

        file1 = open("/main/temp/credentials.json","w")
        file1.write(cred_file)
        file1.close()

        file2 = open("/main/temp/create.yml","w")
        file2.write(playbook_file)
        file2.close()

        return runAnswer()

    def runAnswer():
        run = "docker exec -it questionableansible_ansible_1 ansible-playbook /main/temp/create.yml"
        import subprocess
        process = subprocess.Popen(run.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

        return {'success': False, 'output': output}
