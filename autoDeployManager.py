from __future__ import print_function

import json,boto3, datetime
import codeDeployManager.createCodeDeploy

def autoDeployManager_handler(event, context):


    # Default variables

    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M.%S")
    fun_name = "autoDeployManager"
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
    httpMethod = event['http-method']
    print("####################################")
    print("HTTP Method: "+httpMethod)
    print("####################################")


    action = event['action']
    if httpMethod == 'POST':
        print("####################################")
        print("Running POST Operation!")
        messageBody = {
            'action' :  event['action'],
            'dict': event['dict'],
            'status': event['status']
        }
        print("####################################")
        print(messageBody)
        print("####################################")

        if action == "createCodeDeploy":
            print("action = ",action)
            codeDeployManager.createCodeDeploy.createCodeDeploy_handler(event,context)
        else:
            print("No Action")
        print("####################################")
    elif httpMethod == 'GET':
        print("####################################")
        print("Running GET Operation!")
        print("Ao Action")
        print("####################################")
    else:
        print("No http method passed! Nothing was done to the message!")

    # Log the end of the Lambda function
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M.%S")
    print('END - END TIME - {0}'.format(end_time))
    print('END - LAMBDA - {}'.format(fun_name))

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
    # curl -H "x-api-key: 3NI1RULu89vZX4dF0fbq46AUaKGltEe45P4djdP4" -H "Content-Type: application/json" -X POST -d '{"action":"createCodeDeploy","dict":{"app_app":"acme-app","app_group":"acme-app-dg","group_asg": "awseb-e-smheg37gk9-stack-AWSEBAutoScalingGroup-1L0VID12PNKOQ","group_service_role_arn": "arn:aws:iam::192848410349:role/Al-CodeDeployDemo","group_deployment_config_name": "CodeDeployDefault.OneAtATime"},"status":100}' https://jgtg6kxrxb.execute-api.us-east-1.amazonaws.com/dev/autodeploymanager
    autoDeployManager_handler(event, "test")
else:
    print("Not running __mina__")

