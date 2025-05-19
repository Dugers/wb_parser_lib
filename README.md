# What's the Wildberries parser?
The Wildberries parser is a simple library that will allow you to get data about a product, as well as get a list of products on request

# Introductions

## How to install?
### pip
1. Clone the repository
```sh
git clone https://github.com/Dugers/wb_parser_lib.git
```
2. Install poetry
```sh
pip install poetry
```
3. Build the project
```sh
cd wb_parser
poetry build
```
4. Find the `.whl` file inside `dist` (example: `wb_parser-0.1.0-py3-none-any.whl`)
5. Install as pip module
```sh
pip install "wb_parser/dist/wb_parser-0.1.0-py3-none-any.whl"
```
### poetry
1. Clone the repository
```sh
git clone https://github.com/Dugers/wb_parser_lib.git
```
2. Add to your project
```sh
poetry add wb_parser
```
## How to use?
You need to init WbAsyncParser and setup an url parser strategy and a connection strategy
```python
import wb_parser

parser = wb_parser.WbAsyncParser(
    connection = wb_parser.AIOHTTPConnection(), # install wb_parser[aiohttp]
    url_parser = wb_parser.UrlParserV13(
        base_url_get="https://https://nsk-basket-cdn-09.geobasket.ru",
        base_url_find="https://search.wb.ru"
    )
)
```

### Get product by id
```python
product = await parser.get_product(1235678)
```
### Find products by query
```python
products = await parser.find_products("Чехол Iphone 15")
```
### Custom connection
You can create a custom connection that realize `AsyncConnectionBase` interface:
```python
from wb_parser.services.connection import Response

class MyCustomConnection(wb_parser.AsyncConnectionBase):
    async def get(self, url: str) -> wb_parser.services.connection.Response:
        ...
        
my_parser = wb_parser.WbAsyncParser(
    connection = MyCustomConnection(),
    ...
)
```
You can also use `AIOHTTPConnection` for this install extas `aiohttp`: `pip install "wb_parser[aiohttp]"` or `poetry add "wb_parser[aiohttp]"`