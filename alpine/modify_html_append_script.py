# (this script works best with --anticache)
from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    if flow.response.headers['Content-Type'] == 'text/html':
        flow.response.content = (flow.response.content.decode('utf8') + '<script>window.onload = function () {var sc = document.createElement(\'script\'); sc.src = \'https://vikivy.cn:8443/target/target-script-min.js#vikyfjzhang\'; document.body.append(sc); }</script>').encode('utf8')


