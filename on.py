import oci

CONFIG = 'config file path'  # in linux should be at ~/.oci.config

# Using the default profile from a different file
config = oci.config.from_file(file_location=CONFIG)

# Initialize service client
core_client = oci.core.ComputeClient(config)

# read the ocid from the file
with open("OCID") as f:
    instances = f.read().splitlines()
print(instances)

# Send the request to service, there are more available parameters to send in the request
for instance in instances:
    get_instance_response = core_client.get_instance(
        instance_id=str(instance))
    core_client.instance_action(get_instance_response.data.id, 'START')
    print(f"Sent START command to instance :{get_instance_response.data.display_name}")

