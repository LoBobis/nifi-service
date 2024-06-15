import nipyapi
import os
# Define the base URLs for your NiFi cluster and registry
nifi_url = 'https://192.168.1.106:8443/nifi-api/'
registry_url = 'http://192.168.1.106:18080/nifi-registry-api'

nifi_url = nifi_url.rstrip('/')
registry_url = registry_url.rstrip('/')
# Connect to the NiFi cluster
nipyapi.config.nifi_config.host = nifi_url

# Optionally, if you need to set a username and password
# nipyapi.config.nifi_config.username = 'your-username'
# nipyapi.config.nifi_config.password = 'your-password'

# Connect to the NiFi Registry
nipyapi.config.registry_config.host = registry_url
nipyapi.config.nifi_config.verify_ssl = False
nipyapi.config.registry_config.verify_ssl = False

nipyapi.security.service_login(service="nifi",username="0f6c3bdb-4703-44af-8b43-0e14765c851a", password="ziPVTjSIWfpeeuK2NbIKFNcnhIf6g/K7")

os.environ['X_LOCATION'] = '0'
os.environ['Y_LOCATION'] = '0'