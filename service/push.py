import os
from apns import APNs, Payload
import tempfile


class ApnsProvider():
    """
    Apple push notification service
    push_id is
    push_token is apple push token
    push type : 1 = notification
    raw_content is push content

    """

    TIMEOUT = 10

    def send(self, push_id, push_token, push_type, raw_content):

        # create temp certificate
        cert_file_fd, cert_file = tempfile.mkstemp()
        cert_file_fp = os.fdopen(cert_file_fd, 'w')
        cert_file_fp.write(self.app_pem)
        cert_file_fp.close()

        apns = APNs(
            use_sandbox=True,
            cert_file=cert_file
        )

        alert = raw_content.pop('alert', None)
        sound = raw_content.pop('sound', None)
        badge = raw_content.pop('badge', None)
        category = raw_content.pop('category', None)
        payload = Payload(
            alert=alert,
            sound=sound,
            badge=badge,
            category=category,
            custom={
                'id': push_id,
                'content': raw_content,
            },
            content_available=False if push_type == 1 else True
        )

        try:
            apns.gateway_server.send_notification(
                push_token, payload
            )
        finally:
            os.unlink(cert_file)
