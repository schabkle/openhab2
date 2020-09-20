########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'd022d3fdd55a4110b5d816851cf0dfc0',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ilg1ZVhrNHh5b2pORnVtMWtsMll0djhkbE5QNC1jNTdkTzZRR1RWQndhTmsifQ.eyJleHAiOjE1OTA2ODUxMDgsIm5iZiI6MTU5MDY4MTUwOCwidmVyIjoiMS4wIiwiaXNzIjoiaHR0cHM6Ly9sb2dpbi5taWNyb3NvZnRvbmxpbmUuY29tLzBkODgxNmQ1LTNlN2YtNGM4Ni04MjI5LTY0NTEzN2UwZjIyMi92Mi4wLyIsInN1YiI6IjVjMzZkNjNjLWY0YWEtNDhjMS1iMzEzLThiY2UyZDAyOTI4MSIsImF1ZCI6Ijg5Y2NkZTQ1LTRhZWUtNDZjZC1hY2I4LTJiNDU1ZmNhNWQyOCIsImlhdCI6MTU5MDY4MTUwOCwiYXV0aF90aW1lIjoxNTkwNjgxNTA4LCJvaWQiOiI1YzM2ZDYzYy1mNGFhLTQ4YzEtYjMxMy04YmNlMmQwMjkyODEiLCJmYW1pbHlfbmFtZSI6IlNjaGFiIiwiZ2l2ZW5fbmFtZSI6IktsZSIsIm5hbWUiOiJLbGUgU2NoYWIiLCJlbWFpbHMiOlsic2NoYWJrbGVAZ21haWwuY29tIl0sInRmcCI6IkIyQ18xX0VsaW90LVNpZ25VcE9yU2lnbkluLVdXTCJ9.D0mStayKv01vz8smUrofpLkHLi66JxFhMivsL-B-5YtEalcF6XdFOUJ5Fw8ck0gowJpeUgxNXEHXAwg_z0oTwc3uRLqTB2FYLyJdqay38UfBr9HujsK5Ay9kvbwMPwRixTOwSzIXI7JoR6Xd1vTsOFlNUK--GnlPVYPqXcxCzfdsa9drZMg8meNmWeXoZPaPv83iUvIFwdMce5mLtgfWi7TLrC_POmnKowb3bwoEcajsl1LSFBBXPEd8K5TW-f4ZcOqWSo8h2rpmiPWfq9fByhwJzFMrkXPSS7-bNuDxE1cvmXbC5qFkH4KnKmtVMzPx6srmKAYiuLW313X8b5rvPA',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('api.developer.legrand.com')
    conn.request("GET", "/myhomeup/v1.0/plants?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################