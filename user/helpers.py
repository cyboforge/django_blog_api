import uuid

def generate_random_username():
    """Generate a username using UUID."""
    generated_uuid = str(uuid.uuid4())  # Generate a UUID and convert to string
    