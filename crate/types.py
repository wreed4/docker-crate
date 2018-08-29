"""
Important types
"""
import sh


class Crate:

    """Representation of a runnable container configuration"""

    def __init__(self, name, image, command=None, interactive=False, **kwargs):
        """
        Create a Crate
        """
        self.name = name
        self.image = image
        self.command = command
        self.kwargs = kwargs

        env = self.kwargs.get('env')
        if env:
            self.kwargs['env'] = Env(env)

    def run(self):
        run = sh.docker.run.bake(**self.kwargs, _fg=True, _tty_in=True)
        run = run.bake(self.image)
        if self.command:
            run = run.bake(self.command)
        print(run)
        run()

class Env(dict):
    def __str__(self):
        return ' '.join(f'--env {k}={v}' for k, v in self.items())

class Mount:

    def __init__(self, src, dst, mnt_type='bind'):
        self.src = src
        self.dst = dst
        self.mnt_type

    @property
    def cli(self):
        return f'--mount type={self.mnt_type},src={self.src},dst={self.dst}'

class Port:

    def __init__(self, spec):
        self.spec = spec

    @property
    def cli(self):
        return f'--expose {self.spec}'
