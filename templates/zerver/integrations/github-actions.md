# Zulip GitHub Actions integration

Get Zulip notifications from GitHub Actions workflow runs!

{start_tabs}

{tab|send-channel-message}

1.  {!create-a-generic-bot.md!}

1.  Add the `zulip/github-actions-zulip/send-message@v1` action to your GitHub
    Actions [workflow file][workflows]. The `content` template parameter supports Markdown
    and [GitHub Actions expressions][expressions].

      ```
      {% raw %}- name: Send a channel message
      if: steps.backup.outcome == 'failure'
      uses: zulip/github-actions-zulip/send-message@v1
      with:
         api-key: ${{ secrets.ZULIP_API_KEY }} # Your bot's API key
         email: "github-actions-generic-bot@example.com" # Your bot's email
         organization-url: "https://your-org.zulipchat.com"
         to: "github-actions updates" # Notification channel
         type: "stream"
         topic: "scheduled backups" # Notification topic
         # Example: Notify if a previous GitHub Actions step with the ID "backup" fails.
         content: "Backup failed at ${{ github.event.schedule }}.\n>${{ steps.backup.outputs.error }}"{% endraw %}
      ```

{tab|send-dm}

1.  {!create-a-generic-bot.md!}

1.  Look up the ID of the recipient for DM notifications in their
    [profile](https://zulip.com/help/view-someones-profile).

1. Add the `zulip/github-actions-zulip/send-message@v1` action to your GitHub
    Actions [workflow file][workflows]. The `content` template parameter
    supports Markdown and [GitHub Actions expressions][expressions].

      ```
      {% raw %}- name: Send a channel message
      if: steps.backup.outcome == 'failure'
      uses: zulip/github-actions-zulip/send-message@v1
      with:
         api-key: ${{ secrets.ZULIP_API_KEY }} # Your bot's API key
         email: "github-actions-generic-bot@example.com" # Your bot's email
         organization-url: "https://your-org.zulipchat.com"
         to: "295" # Recipient's user ID
         type: "private"
         # Example: Notify if a previous GitHub Actions step with the ID "backup" fails.
         content: "Backup failed at ${{ github.event.schedule }}.\n>${{ steps.backup.outputs.error }}"{% endraw %}
      ```

{end_tabs}

{!congrats.md!}

![](/static/images/integrations/github-actions/001.png)

### Related documentation

* [Configuring the Send Message Action][README]

* [Zulip GitHub Actions repository][repo]

* [GitHub integration](/integrations/doc/github)

[README]: https://github.com/zulip/github-actions-zulip/blob/main/send-message/README.md
[repo]: https://github.com/zulip/github-actions-zulip
[expressions]: https://docs.github.com/en/actions/reference/evaluate-expressions-in-workflows-and-actions
[workflows]: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
