# autodeploy



EG POST
curl -H "x-api-key: 3NI1RULu89vZX4dF0fbq46AUaKGltEe45P4djdP4" -H "Content-Type: application/json" -X POST -d '{"action":"createCodeDeploy","dict":{"app_app":"acme-app","app_group":"acme-app-dg"},"status":100}' https://jgtg6kxrxb.execute-api.us-east-1.amazonaws.com/dev/autodeploymanager


curl -H "x-api-key: 3NI1RULu89vZX4dF0fbq46AUaKGltEe45P4djdP4" -H "Content-Type: application/json" -X POST -d '{"action":"createCodeDeploy","dict":{"app_app":"acme-app","app_group":"acme-app-dg","group_asg": "awseb-e-smheg37gk9-stack-AWSEBAutoScalingGroup-1L0VID12PNKOQ","group_service_role_arn": "arn:aws:iam::192848410349:role/Al-CodeDeployDemo","group_deployment_config_name": "CodeDeployDefault.OneAtATime"},"status":100}' https://jgtg6kxrxb.execute-api.us-east-1.amazonaws.com/dev/autodeploymanager

