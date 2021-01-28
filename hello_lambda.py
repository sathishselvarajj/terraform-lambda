import os


def lambda_handler(event, context):
    return "{} from Sathish K, This is lambda deployment using Terraform, Cool isnt it???!".format(os.environ['greeting'])
