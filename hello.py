def application(env, resp):
	status = "200 OK"
	headers = [("Content-type", "text/plain")]
	resp(status, headers)
	return env["QUERY_STRING"].replace("&", "\n")
