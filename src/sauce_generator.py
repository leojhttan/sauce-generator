import random
import webbrowser
from dataclasses import dataclass


@dataclass(frozen=True)
class SauceConfig:
    max_id_exclusive: int = 478372
    order_count: int = 2


class SauceGenerator:
    def __init__(self, config: SauceConfig, rng=None):
        self.config = config
        self.rng = rng if rng is not None else random.Random()

    def generate_id(self) -> int:
        return self.rng.randrange(self.config.max_id_exclusive)

    def build_url(self, sauce_id: int) -> str:
        return f"https://nhentai.net/g/{sauce_id}"


class SauceOpener:
    def __init__(self, browser=None):
        self.browser = browser if browser is not None else webbrowser

    def open(self, url: str) -> None:
        self.browser.open(url, 0, True)


class SauceApp:
    def __init__(self, generator: SauceGenerator, opener: SauceOpener):
        self.generator = generator
        self.opener = opener

    def run(self) -> None:
        for _ in range(self.generator.config.order_count):
            sauce_id = self.generator.generate_id()
            print(sauce_id)
            self.opener.open(self.generator.build_url(sauce_id))


def main() -> None:
    config = SauceConfig()
    app = SauceApp(
        generator=SauceGenerator(config),
        opener=SauceOpener(),
    )
    app.run()


if __name__ == "__main__":
    main()
