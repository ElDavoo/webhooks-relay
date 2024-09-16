# Do a very simple thing: When you get a request, you need to forward it to the
# appropriate container, determined by URL path.

from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/webhooks/<path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    """
    Catch all requests and forward them to the appropriate container
    :param path: URL path
    :return: Response
    """
    print(path)
    # Get the request headers
    headers = dict(request.headers)
    # Get the request method
    method = request.method
    # Make a list of 4 possible urls
    urls = [
        'http://' + path,
        'http://' + path + ':8080',
        'http://' + path + '/webhooks/' + path,
        'http://' + path + ':8080/webhooks/' + path
    ]
    # Try all of the urls, if one of them works, break the loop
    for url in urls:
        try:
            # Pass the request json as it is, without touching it
            response = requests.request(
                method,
                url,
                headers=headers,
                data=jsonify(request.json),
            )
            break
        except requests.exceptions.ConnectionError:
            continue
    # Return the response
    return Response(response.content, response.status_code, dict(response.headers))

if __name__ == '__main__':
    # Listen on all interfaces and port 8080
    app.run(port=8080, host='0.0.0.0')