"""
SOAP (Simple Object Access Protocol): This is a protocol that uses XML as a format to transfer data. Its main function is to define the structure of the messages and methods of communication. It also uses WSDL, or Web Services Definition Language, in a machine-readable document to publish a definition of its interface.
"""



import requests
url = "https://httpbin.org/post"

headers = {"content-type" : "application/soap+xml"}
body = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:req="https://httpbin.org/post">
<soapenv:Header/>
   <soapenv:Body/>
</soapenv:Envelope>
"""

response = requests.post(url, data = body, headers = headers)
print(response)