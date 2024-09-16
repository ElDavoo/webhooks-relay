# Do a very simple thing: When you get a request, you need to forward it to the
# appropriate container, determined by URL path.

from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    """
    Catch all requests and forward them to the appropriate container
    :param path: URL path
    :return: Response
    """
    # Get the container name from the URL path
    container_name = path.split('/')[0]
    # Get the URL path, it might be empty
    url_path = path[len(container_name):]
    # Get the request headers
    headers = dict(request.headers)
    # Get the request data
    data = request.get_data()
    # Get the request method
    method = request.method
    # Get the request URL
    url = 'http://'+container_name+url_path
    # Make the request
    response = requests.request(method, url, headers=headers, data=data)
    # Return the response
    return Response(response.content, response.status_code, dict(response.headers))

if __name__ == '__main__':
    # Listen on all interfaces and port 8080
    app.run(port=8080, host='0.0.0.0')