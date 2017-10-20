def application(environ , start_response):
    start_response("200 ok" , [("Content-Type" , "text/html")]);
    body = '<h1>hello , %s' % (environ["PATH_INFO"][1:] or 'web---web');
    return [body.encode("utf-8")];