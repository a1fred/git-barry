from .abstract import AbstractReason
from gitbarry.config import settings
from gitbarry.utils import git
tasks = settings['TASKS'].keys()


class Reason(AbstractReason):
    def usage(self):
        print("git barry switch options:")
        print("  git barry switch <task> <feature_name>")

    def validate(self):
        if len(self.args) != 2:
            return ['use "git barry switch help" to see options.']
        task, tagname = self.args
        branch = "%s/%s" % (task, tagname)
        if git.get_current_branch() == branch:
            return [
                'Already at %s' % branch
            ]
        errors = []
        return errors

    def run(self):
        task, tagname = self.args
        branch = "%s/%s" % (task, tagname)

        git.swith_to_branch(branch)
        print("Done")
