# Zulip Errbot integration

Run your favorite chatbot in Zulip!

{start_tabs}

1. [Install errbot][install-errbot], and follow the instructions to set up a
   `config.py`.

1. Clone the [Errbot integration package for Zulip][errbot-package]
   repository somewhere convenient, and install the requirements listed in
   `errbot-backend-zulip/requirements.txt`.

1. {!create-a-generic-bot.md!}

1. Edit your ErrBot's `config.py`. Use the following template for a minimal
   configuration:

        import logging

        BACKEND = 'Zulip'

        BOT_EXTRA_BACKEND_DIR = r'/home/user/errbot-backend-zulip'
        BOT_DATA_DIR = r'/var/lib/err'
        BOT_EXTRA_PLUGIN_DIR = r'/opt/extraplugins'

        BOT_LOG_FILE = r'/var/lib/err/err.log'
        BOT_LOG_LEVEL = logging.INFO

        BOT_IDENTITY = {
          'email': 'your-zulip-bot-name@yourZulipDomain.zulipchat.com',
          'key': '0123456789abcdef0123456789abcdef',
          'site': '{{ zulip_url }}'
        }
        BOT_ADMINS = ('user@example.com',)
        CHATROOM_PRESENCE = ()
        BOT_PREFIX = '@**errbot-bot**'

    Configure the settings suffixed with `DIR` with the paths to your
    errbot directories, and set `BOT_LOG_FILE` to your errbot's logfile.
    Use the details of the Zulip bot created above for the `BOT_IDENTITY`
    and `BOT_PREFIX` sections, and add your email in `BOT_ADMINS`.

1. [Start ErrBot][start-errbot].

!!! tip ""

    ErrBot uses the term "Rooms" for Zulip channels.

{end_tabs}

{!congrats.md!}

![Errbot message](/static/images/integrations/errbot/000.png)

### Related documentation

- [Errbot Documentation](https://errbot.readthedocs.io/en/latest/)
- [Errbot integration package for Zulip][errbot-package]
- [Python bindings Configuration][config-python-bindings]

[install-errbot]: https://errbot.readthedocs.io/en/latest/user_guide/setup.html
[errbot-package]: https://github.com/zulip/errbot-backend-zulip
[start-errbot]: https://errbot.readthedocs.io/en/latest/user_guide/setup.html#starting-the-daemon
[config-python-bindings]: https://zulip.com/api/configuring-python-bindings
