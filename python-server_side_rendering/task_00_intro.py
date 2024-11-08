import logging
import os


def generate_invitations(template, attendees):
    """Generates Invitations"""

    # Check if template is a string
    if not isinstance(template, str):
        logging.error("Template must be a string")
        return

    # Check if attendees is a list of dictiories
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Attendees must be a list of dictionaries")
        return

    # Check if template is empty
    if not template:
        logging.error("Template cannot be empty")
        return

    # Check if attendees is empty
    if not attendees:
        logging.error("Attendees cannot be empty")
        return

    invitations = []

    # Iterate over each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace Placeholders with attendee's details or "N/A"
        name = attendee.get("name", "N/A")
        email = attendee.get("email", "N/A")
        date = attendee.get("date", "N/A")

        # Create the invitation by replacing placeholders
        invitation = template.replace("{name}", name).replace("{email}", email).replace("{date}", date)

        # Append the invitation to the list of invitations
        invitations.append(invitation)

        # Define the output file name
        output_file = f'output_{index}.txt'

        # Check if the file already exists
        if os.path.exists(output_file):
            logging.error(f"File {output_file} already exists")
        else:
            # Write the invitation to an output file
            with open(output_file, 'w') as file:
                file.write(invitation)

    return invitations