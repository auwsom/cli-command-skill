from mycroft import MycroftSkill, intent_file_handler


class CliCommand(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('command.cli.intent')
    def handle_command_cli(self, message):
        self.speak_dialog('command.cli')


def create_skill():
    return CliCommand()

