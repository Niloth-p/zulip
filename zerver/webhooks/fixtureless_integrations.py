from typing import TypedDict

# For integrations that don't have example webhook fixtures/payloads,
# we create an Zulip notification message content and topic here in
# order to generate an example screenshot to include in the documentation
# page for those integrations.

# To keep these screenshots consistent and easy to review, there are
# shared string constants to use for common content in these integration
# notification messages/templates.

THREE_DIGIT_NUMBER = "492"

# Example user content
BO_NAME = "Bo Williams"
BO_EMAIL = "Bo-Williams@example.com"
BO_GIT_NAME = "bo-williams"

KEVIN_NAME = "Kevin Lin"
KEVIN_EMAIL = "Kevin-Lin@example.com"

# Example project content
PROJECT_NAME = "Examplr"
PROJECT_PATH = "//depot/zerver/examplr/*"

REVISION_NUMBER = THREE_DIGIT_NUMBER

# Example branch content
BRANCH = "main"
BRANCH_MERCURIAL = "default"
BRANCH_SVN = "trunk"

# Example commit content
COMMIT_MESSAGE_A = "Optimize image loading in paints catalog."
COMMIT_MESSAGE_B = 'Suppress "comment edited" events when body is unchanged.'

COMMIT_HASH_A = "a2e84e86ddf7e7f8a9b0c1d2e3f4a5b6c7d8e9f0"
COMMIT_HASH_B = "9fceb02c0c4b8e4c1e7b43hd4e5f6a7b8c9d0e1f"
DEPLOYMENT_HASH = "e494a5be3393"


class ScreenshotContent(TypedDict):
    topic: str
    content: str


CODEBASE = ScreenshotContent(
    topic=f"Push to {BRANCH} on {PROJECT_NAME}",
    content=f"""{BO_NAME} pushed 2 commit(s) to `{BRANCH}` in project {PROJECT_NAME}:

* [{COMMIT_HASH_A[:10]}](): {COMMIT_MESSAGE_A}
* [{COMMIT_HASH_B[:10]}](): {COMMIT_MESSAGE_B}
""",
)

GIT = ScreenshotContent(
    topic=BRANCH,
    content=f"""`{DEPLOYMENT_HASH[:12]}` was deployed to `{BRANCH}` with:
* {KEVIN_EMAIL} - {COMMIT_HASH_A[:7]}: {COMMIT_MESSAGE_A}
* {BO_EMAIL} - {COMMIT_HASH_B[:7]}: {COMMIT_MESSAGE_B}
""",
)

MERCURIAL = ScreenshotContent(
    topic=BRANCH_MERCURIAL,
    content=f"""**{BO_NAME}** pushed [2 commits]() to **{BRANCH_MERCURIAL}** (`{REVISION_NUMBER}:{DEPLOYMENT_HASH[:12]}`):
* [{COMMIT_MESSAGE_A}]()
* [{COMMIT_MESSAGE_B}]()
""",
)

PERFORCE = ScreenshotContent(
    topic=PROJECT_PATH,
    content=f"""
**{BO_NAME}** committed revision @[{REVISION_NUMBER}]() to `{PROJECT_PATH}`.

```quote
{COMMIT_MESSAGE_A}
```
""",
)

SVN = ScreenshotContent(
    topic=PROJECT_NAME,
    content=f"""**{BO_GIT_NAME}** committed revision r{REVISION_NUMBER} to `{BRANCH_SVN}`.
> {COMMIT_MESSAGE_A}
""",
)
