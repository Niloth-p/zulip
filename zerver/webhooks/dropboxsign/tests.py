from typing_extensions import override

from zerver.lib.test_classes import WebhookTestCase


class DropboxSignHookTests(WebhookTestCase):
    CHANNEL_NAME = "dropbox sign"
    URL_TEMPLATE = "/api/v1/external/dropboxsign?stream={stream}&api_key={api_key}"
    LEGACY_URL_TEMPLATES = ["/api/v1/external/hellosign?stream={stream}&api_key={api_key}"]
    WEBHOOK_DIR_NAME = "dropboxsign"

    def test_signatures_message(self) -> None:
        expected_topic_name = "NDA with Acme Co."
        expected_message = (
            "The `NDA with Acme Co.` document is awaiting the signature of "
            "Jack, and was just signed by Jill."
        )
        self.check_webhook("signatures", expected_topic_name, expected_message, content_type=None)

    def test_signatures_message_signed_by_one(self) -> None:
        expected_topic_name = "NDA with Acme Co."
        expected_message = "The `NDA with Acme Co.` document was just signed by Jill."
        self.check_webhook(
            "signatures_signed_by_one_signatory",
            expected_topic_name,
            expected_message,
            content_type=None,
        )

    def test_signatures_message_with_four_signatories(self) -> None:
        expected_topic_name = "Signature doc"
        expected_message = (
            "The `Signature doc` document is awaiting the signature of "
            "Eeshan Garg, John Smith, Jane Doe, and Stephen Strange."
        )
        self.check_webhook(
            "signatures_with_four_signatories",
            expected_topic_name,
            expected_message,
            content_type=None,
        )

    def test_signatures_message_with_own_subject(self) -> None:
        expected_topic_name = "Our own subject."
        self.url = self.build_webhook_url(topic=expected_topic_name)
        expected_message = (
            "The `NDA with Acme Co.` document is awaiting the signature of "
            "Jack, and was just signed by Jill."
        )
        self.check_webhook(
            "signatures_with_own_subject",
            expected_topic_name,
            expected_message,
            content_type=None,
            topic=expected_topic_name,
        )

    def test_callback_test(self) -> None:
        expected_topic_name = "Dropbox Sign"
        expected_message = "Dropbox Sign webhook has been successfully configured."
        self.check_webhook(
            "callback_test", expected_topic_name, expected_message, content_type=None
        )

    @override
    def get_payload(self, fixture_name: str) -> dict[str, str]:
        return {"json": self.webhook_fixture_data("dropboxsign", fixture_name, file_type="json")}
