# How to access keys from ec2 using the instance profile

```python
from botocore.credentials import InstanceMetadataProvider, InstanceMetadataFetcher

provider = InstanceMetadataProvider(iam_role_fetcher=InstanceMetadataFetcher(timeout=1000, num_attempts=2))
creds = provider.load().get_frozen_credentials()
client = boto3.client('ssm', region_name='us-east-1', aws_access_key_id=creds.access_key, aws_secret_access_key=creds.secret_key, aws_session_token=creds.token)
```
