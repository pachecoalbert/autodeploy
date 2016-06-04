from __future__ import print_function

import json,boto3, datetime

def createCodeDeploy_handler(event, context):


    # Default variables

    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M.%S")
    fun_name = "createCodeDeploy"
    try:
        if env == 'local':
            print('BEGIN - LAMBDA - {}'.format(fun_name))
            print('BEGIN - START TIME - {0}'.format(start_time))
            print('Running locally')
            boto3.setup_default_session(profile_name='huitclouddev')
    except NameError:
        print('BEGIN - LAMBDA - {}'.format(fun_name))
        print('BEGIN - START TIME - {0}'.format(start_time))
        print('Running AWS')

    # Get the client from the resource
    client = boto3.client('codedeploy',region_name='us-east-1')

    print("####################################")
    print("Print Event")
    print("####################################")
    print(event)
    print("####################################")
    print("####################################")
    print("Print Context")
    print("####################################")
    print(context)
    print("####################################")

    app_name = event['dict']['app_name']
    print(app_name)

    group_name = event['dict']['group_name']
    print(group_name)

    group_asg = event['dict']['group_asg']
    print(group_asg)

    group_service_role_arn = event['dict']['group_service_role_arn']
    print(group_service_role_arn)

    group_deployment_config_name = event['dict']['group_deployment_config_name']
    print(group_deployment_config_name)

    app_response = client.create_application(
    applicationName=app_name
    )
    #ApplicationAlreadyExistsException


    group_response = client.create_deployment_group(
    applicationName=app_name,
    deploymentGroupName=group_name,
    deploymentConfigName=group_deployment_config_name,
    autoScalingGroups=[
        group_asg,
    ],
    serviceRoleArn=group_service_role_arn
    )



    print(group_response)

    return event
# Used to dbug

# --------------------------------------
# Main
# --------------------------------------
# Allow you to run on local sandbox for testing
if __name__ == "__main__":
    #print("running __mina__")
    # Connection settings.  Win NOT be used with lambda function
    global env
    env = 'local'

    event={
            "http-method": "POST",
            "action":"createCodeDeploy",
            "dict": {"app_name":"acme-app","group_name": "acme-app-dg","group_asg": "awseb-e-smheg37gk9-stack-AWSEBAutoScalingGroup-1L0VID12PNKOQ","group_service_role_arn": "arn:aws:iam::192848410349:role/Al-CodeDeployDemo","group_deployment_config_name": "CodeDeployDefault.OneAtATime"},
            "status":100
    }
    # curl -H "Content-Type: application/json" -X POST -d '{"action":"createCodeDeploy","dict":{"acme-app","app_group":"acme-app-dg"},"status":100}' https://jgtg6kxrxb.execute-api.us-east-1.amazonaws.com/dev/autodeploymanager
    createCodeDeploy_handler(event, "test")
else:
    print("Not running __mina__")