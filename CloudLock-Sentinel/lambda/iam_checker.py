import boto3

iam = boto3.client('iam')

for user in iam.list_users()['Users']:
    policies = iam.list_attached_user_policies(UserName=user['UserName'])
    for p in policies['AttachedPolicies']:
        if p['PolicyName'] == 'AdministratorAccess':
            print(f"[ALERT] {user['UserName']} has AdministratorAccess!")
