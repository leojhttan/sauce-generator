import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import webbrowser


class SauceGenerator:
    def __init__(self, order_count: int = 1, browser=None):
        self.order_count = order_count
        self.browser = browser if browser is not None else webbrowser

    def get_random_gallery_id(self, api_url: str) -> int:
        request = Request(
            api_url,
            headers={
                "User-Agent": (
                    "SauceGenerator/1.0 "
                    "(https://github.com/leojhttan/sauce-generator)"
                )
            },
        )
        with urlopen(request, timeout=10) as response:
            if response.status != 200:
                raise RuntimeError(f"API returned HTTP {response.status}: {api_url}")

            gallery = json.loads(response.read().decode("utf-8"))
            return int(gallery["id"])

    def open(self) -> None:
        api_url = "https://nhentai.net/api/v2/galleries/random"

        try:
            gallery_id = self.get_random_gallery_id(api_url)
        except HTTPError as error:
            print(f"Could not retrieve a random gallery: {error}")
            return
        except URLError as error:
            print(f"Could not retrieve a random gallery: {error}")
            return
        except TimeoutError as error:
            print(f"Could not retrieve a random gallery: {error}")
            return
        except (KeyError, TypeError, ValueError) as error:
            print(f"The API response did not contain a valid gallery: {error}")
            return
        except RuntimeError as error:
            print(error)
            return

        gallery_url = f"https://nhentai.net/g/{gallery_id}"
        print("w response")
        print(f"Gallery ID: {gallery_id}")
        print(gallery_url)
        self.browser.open(gallery_url, 0, True)


class SauceApp:
    def __init__(self, generate: SauceGenerator):
        self.generate = generate

    def run(self) -> None:
        for _ in range(self.generate.order_count):
            self.generate.open()


def main() -> None:
    generate = SauceGenerator()
    app = SauceApp(generate=generate)
    app.run()


if __name__ == "__main__":
    main()
