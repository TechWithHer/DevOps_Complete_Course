# nettoolbox/cloud_devops/s3_test.py
import time
from datetime import datetime

try:
    import boto3
    from botocore.exceptions import NoCredentialsError, ClientError
    _HAS_BOTO = True
except Exception:
    _HAS_BOTO = False

def test_s3(bucket_name: str = None, timeout: float = 5.0) -> dict:
    """
    Minimal S3 test:
    - If boto3 available and credentials configured, list buckets and check for `bucket_name`.
    - If boto3 missing or credentials absent, return informative error.
    """
    start = time.time()
    out = {"test": "cloud_devops.s3", "target": bucket_name, "timestamp": datetime.utcnow().isoformat() + "Z"}

    if not _HAS_BOTO:
        out.update({"success": False, "error": "boto3 not installed", "duration": time.time() - start})
        return out

    try:
        s3 = boto3.client("s3")
        resp = s3.list_buckets()
        buckets = [b["Name"] for b in resp.get("Buckets", [])]
        out["buckets"] = buckets
        out["found"] = bucket_name in buckets if bucket_name else None
        out["success"] = True
        out["duration"] = time.time() - start
    except NoCredentialsError:
        out.update({"success": False, "error": "AWS credentials not found", "duration": time.time() - start})
    except ClientError as ce:
        out.update({"success": False, "error": str(ce), "duration": time.time() - start})
    except Exception as e:
        out.update({"success": False, "error": str(e), "duration": time.time() - start})

    return out
