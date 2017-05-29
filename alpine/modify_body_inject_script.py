# (this script works best with --anticache)
from bs4 import BeautifulSoup
from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    if flow.response.headers["Content-Type"] == "text/html":
        html = BeautifulSoup(flow.response.content, "html.parser")
        script = html.new_tag(
            "script",
            src='https://vikivy.cn:8443/target/target-script-min.js#vikyfjzhang')
        html.body.insert(0, script)
        flow.response.content = str(html).encode("utf8")
