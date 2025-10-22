from importlib.metadata import version

__version__ = version("uv-demo")


def main() -> None:  # noqa: D103
    print("Hello from uv-demo!\nVersion:", __version__)
