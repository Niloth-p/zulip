from django.http import HttpRequest, HttpResponse

from zerver.decorator import webhook_view
from zerver.lib.response import json_success
from zerver.lib.typed_endpoint import JsonBodyPayload, typed_endpoint
from zerver.lib.validator import WildValue, check_int, check_string
from zerver.lib.webhooks.common import check_send_webhook_message
from zerver.models import UserProfile

RUNDECK_MESSAGE_TEMPLATE = "[{job_name}]({job_link}) execution [#{execution_id}]({execution_link}) for {project_name} {status}. {emoji}"
STATUS_MAP = {
    "failed": ("has failed", ":cross_mark:"),
    "succeeded": ("has succeeded", ":check:"),
    "running": ("has started", ":running:"),
    "scheduled": ("has started", ":running:"),
}


@webhook_view("Rundeck")
@typed_endpoint
def api_rundeck_webhook(
    request: HttpRequest,
    user_profile: UserProfile,
    *,
    payload: JsonBodyPayload[WildValue],
) -> HttpResponse:
    execution = payload["execution"]
    job_name = execution["job"]["name"].tame(check_string)

    topic_name = job_name
    body = get_body(payload, execution, job_name)

    check_send_webhook_message(request, user_profile, topic_name, body)
    return json_success(request)


def get_body(payload: WildValue, execution: WildValue, job_name: str) -> str:
    status_raw = execution["status"].tame(check_string)
    status_text, emoji = STATUS_MAP.get(status_raw, (f"is {status_raw}", ""))

    if status_raw == "running" and payload["trigger"].tame(check_string) == "avgduration":
        status_text = "is running long"
        emoji = ":time_ticking:"

    return RUNDECK_MESSAGE_TEMPLATE.format(
        job_name=job_name,
        job_link=execution["job"]["permalink"].tame(check_string),
        execution_id=execution["id"].tame(check_int),
        execution_link=execution["href"].tame(check_string),
        project_name=execution["project"].tame(check_string),
        status=status_text,
        emoji=emoji,
    )
