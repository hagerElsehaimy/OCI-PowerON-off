# response = analytics.start_analytics_instance(analytics_instance_id=self.ID)
# This is an automatically generated code sample.
# To make this code sample work in your Oracle Cloud tenancy,
# please replace the values for any parameters whose current values do not fit
# your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
# boolean, number, and enum parameters with values not fitting your use case).

import oci

# Create a default config using DEFAULT profile in default location
# Refer to
# https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File
# for more info
CONFIG = '~/.oci.config'
config = oci.config.from_file(file_location=CONFIG)


# Initialize service client with default config file
analytics_client = oci.analytics.AnalyticsClient(config)


# Send the request to service, some parameters are not required, see API
# doc for more info
stop_analytics_instance_response = analytics_client.stop_analytics_instance(
    analytics_instance_id="ocid1.analyticsinstance.oc1.me-jeddah-1.aaaaaaaaym2gjwjrk3ndzuwwqmjugmcwcge5sxblsi4yrwvztor7aaj5twxq",
    )

# Get the data from response
print(stop_analytics_instance_response.headers)