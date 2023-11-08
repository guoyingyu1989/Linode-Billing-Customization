# Linode-Billing-Customization

I received a request to relate VM detailed information (i.e. tags) to linode billing invoices.
Though I cannot make any changes to linode standard invoices directly, I can use Linode API (https://developers-linode.netlify.app/api/v4/account-invoices-invoice-id) to get the invoice data.
Since the logic is quite simply when considering only monthly invoice data(do not ask me why not T-2 but monthly, as of now linode is not capable to provide daily detailed billing info). We just simply run this task every month so that the latest invoices can be collected with specified VM info.

In my example I used only tag info. 
