from flask import Flask, jsonify
import boto3
from datetime import datetime, timedelta

app = Flask(__name__)

aws_access_key_id = '...................'
aws_secret_access_key = '.......................'
region_name = 'us-east-1'

cloudwatch = boto3.client('cloudwatch',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)

instance_id = 'i-04759b3b041b001b1'

@app.route('/metrics', methods=['GET'])
def get_metrics():
    current_time_utc = datetime.utcnow()

    start_time_utc = current_time_utc - timedelta(hours=24)

    start_time_str = start_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_time_str = current_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ')

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUCreditBalance',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time_str,
        EndTime=end_time_str,
        Period=3600,  # 1 hour
        Statistics=['Average']
    )

    if 'Datapoints' in response and len(response['Datapoints']) > 0:
        average_value = response['Datapoints'][0]['Average']
        metric = {'CPUCreditBalance': average_value}
    else:
        metric = {'CPUCreditBalance': None}

    return jsonify(metric)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)