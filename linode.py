from linode_api4 import LinodeClient, Instance
import requests
import re

api_token = '<YOUR API TOKEN>'  # replace it with your own API token
client = LinodeClient(api_token)

def get_invoices():
    invoices = sorted(client.account.invoices(), key=lambda invoice: invoice.date, reverse=True)
    return invoices

def get_latest_invoice_items(invoices):
    latest_invoice = invoices[0]
    items = latest_invoice.items
    return items

def get_linode_ids(items):
    bracket_id = [re.findall(r'\((\d{8})\)', item.label) for item in items]
    bracket_id = [detail for detail in bracket_id if detail]
    linode_ids = [int(detail[0]) for detail in bracket_id if detail[0].isdigit()]
    return linode_ids

def get_linode_result(linode_ids):
    linode_result = []
    for linode_id in linode_ids:
        url = f'https://api.linode.com/v4/linode/instances/{linode_id}'
        headers = {'Authorization':'Bearer ' + api_token}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            id = int(data.get('id'))  
            tags = data.get('tags', [])
            linode_result.append([id, tags])  
    return linode_result
