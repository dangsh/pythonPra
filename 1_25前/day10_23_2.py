def application(environ , start_response):
    method = environ['REQUEST_METHOD']
    path =environ['PATH_INFO']
    if method == 'GET' and path == '/':
        return handle_home(environ , start_response)

    if method == 'POST' and path == '/signin':
        return handle_signin(environ , start_response)
