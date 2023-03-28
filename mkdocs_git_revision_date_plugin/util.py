from git import Git

class Util:

    def __init__(self, repo_dir):
        self.g = Git(repo_dir)

    def get_revision_date_for_file(self, path: str):
        return self.g.log(path, n=1, date='short', format='%ad')