import subprocess
import datetime
import importlib
import os
import tempfile
import ansible_runner

modules = {'flow': 'framework.service.flow',}


class adapter:

    def __init__(self, **constants):
        self.config = constants.get('config', {})

    @flow.asynchronous(outputs='transaction')
    async def load(self, *services, **constants):
        return await self.actuate(**constants | {'method': 'PUT'})

    async def actuate(self, **constants):
        # api_key removed for security
        endpoint = "https://your-api-endpoint.com/your-function"

        playbook_content = f"""---
- name: Configura cron job per eseguire funzione solo di sabato
  hosts: localhost
  tasks:
    - name: Aggiungi cron job per eseguire la funzione tramite chiamata HTTP
      ansible.builtin.cron:
        name: "Esegui funzione ogni sabato"
        minute: "0"
        hour: "0"
        day: "*"
        month: "*"
        weekday: "6"
        job: >-
          curl -X POST https://
          -H "Authorization: Bearer "
          -H "Content-Type: application/json"
"""
        

        # Usa una directory temporanea in RAM (tipicamente /tmp)
        with tempfile.TemporaryDirectory() as temp_dir:
            project_dir = os.path.join(temp_dir, 'project')
            inventory_dir = os.path.join(temp_dir, 'inventory')
            os.makedirs(project_dir, exist_ok=True)
            os.makedirs(inventory_dir, exist_ok=True)

            # Scrive il playbook
            playbook_path = os.path.join(project_dir, 'playbook.yml')
            with open(playbook_path, 'w') as f:
                f.write(playbook_content)

            # Scrive l'inventory localhost
            inventory_path = os.path.join(inventory_dir, 'hosts')
            with open(inventory_path, 'w') as f:
                f.write('[local]\nlocalhost ansible_connection=local\n')

            # Esegue Ansible Runner
            r = ansible_runner.run(
                private_data_dir=temp_dir,
                playbook='playbook.yml'
            )

            # Verifica risultato
            if r.status == 'successful':
                print("✅ Cron job creato con successo.")
            else:
                print("❌ Errore nella creazione del cron job.")
                #print(r.stdout.read() if r.stdout else "Nessun output")

    @flow.asynchronous(outputs='transaction')
    async def activate(self, *services, **constants):
        return await self.actuate(**constants | {'method': 'PUT'})

    @flow.asynchronous(outputs='transaction')
    async def deactivate(self, *services, **constants):
        pass

    @flow.asynchronous(outputs='transaction')
    async def calibrate(self, *services, **constants):
        pass

    @flow.asynchronous(outputs='transaction')
    async def status(self, *services, **constants):
        pass

    @flow.asynchronous(outputs='transaction')
    async def reset(self, *services, **constants):
        pass

