# Weighted Round Robin Load Balancing with Flask and AWS CloudWatch Metrics

This project implements a weighted round-robin load balancing algorithm to distribute requests among multiple servers. It utilizes Flask for creating APIs that fetch CPU credit balance metrics from AWS CloudWatch for EC2 instances.

## APIs

### API 1
- URL: http://34.204.84.206:8080/metrics
- Description: This API fetches CPU credit balance metrics from an EC2 instance.
- Server Weight: 1

### API 2
- URL: http://54.174.5.92:8080/metrics
- Description: This API fetches CPU credit balance metrics from another EC2 instance.
- Server Weight: 2

## Flask API Code (app.py)

The Flask application code is used to create APIs for fetching CPU credit balance metrics from AWS CloudWatch. It includes the following features:
- Fetches CPU credit balance metrics for a specific EC2 instance.
- Returns the fetched metrics in JSON format.

## Weighted Round Robin Load Balancer (load_balancer.py)

The `load_balancer.py` script implements a weighted round-robin load balancing algorithm to distribute requests among the specified servers. It includes the following components:
- Server configuration with URLs and corresponding weights.
- Weighted round-robin selection of server URLs.
- Function to fetch data from the selected server.
- Main loop for making periodic requests to servers based on the load balancing algorithm.

## Usage

1. Ensure that the necessary AWS credentials and permissions are set up to access CloudWatch metrics.
2. Run the Flask API using the provided Dockerfile to containerize the application.
3. Run the `load_balancer.py` script to simulate a client making periodic requests to the servers.
4. Monitor the console output to observe the load balancing in action.

## Requirements

- Python 3.8
- Flask
- Boto3
- Requests

## Author

DIVYA PRAKASH SRIVASTAVA

## License

This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.
