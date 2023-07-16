from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    return render(request, 'setu/consent.html')

def getConsent(request):

    if request.method == "POST":
        cid = request.POST['cid']
        cs = request.POST['cs']

        url = "https://fiu-uat.setu.co/consents"

        payload = {
            "Detail": {
                "consentStart": "2024-02-14T11:28:06.983Z",
                "consentExpiry": "2025-04-23T05:44:53.822Z",
                "Customer": {"id": "9999999999@onemoney"},
                "FIDataRange": {
                    "from": "2020-04-01T00:00:00Z",
                    "to": "2023-01-01T00:00:00Z"
                },
                "consentMode": "STORE",
                "consentTypes": ["TRANSACTIONS", "PROFILE", "SUMMARY"],
                "fetchType": "PERIODIC",
                "Frequency": {
                    "value": 30,
                    "unit": "MONTH"
                },
                "DataFilter": [
                    {
                        "type": "TRANSACTIONAMOUNT",
                        "value": "5000",
                        "operator": ">="
                    }
                ],
                "DataLife": {
                    "value": 1,
                    "unit": "MONTH"
                },
                "DataConsumer": {"id": "setu-fiu-id"},
                "Purpose": {
                    "Category": {"type": "string"},
                    "code": "101",
                    "text": "Loan underwriting",
                    "refUri": "https://api.rebit.org.in/aa/purpose/101.xml"
                },
                "fiTypes": ["DEPOSIT", "EQUITIES"]
            },
            "redirectUrl": "https://setu.co",
            "context": [
                {
                    "key": "accounttype",
                    "value": "somevalue"
                }
            ]
        }
        headers = {
            "x-client-id": cid,
            "x-client-secret": cs
        }

        response = requests.request("post", url, json=payload, headers=headers)

        response = response.json()
        print(response)

        id = response['id']
        url = response['url']

        return render(request, 'setu/consent.html', {
            'id': id,
            'url': url,
            'res': response
        })

    return render(request, 'setu/form.html')