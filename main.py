import linode
import excel

invoices = linode.get_invoices()
items = linode.get_latest_invoice_items(invoices)
df = excel.create_bill_details_df(items)
excel.write_df_to_excel(df, 'cache_bill.xlsx')
linode_ids = linode.get_linode_ids(items)
linode_result = linode.get_linode_result(linode_ids)
df = excel.read_excel_file('cache_bill.xlsx')
df = excel.update_df_with_tags(df, linode_result)
filename = excel.get_current_datetime_as_str()
excel.write_df_to_excel(df, filename)
excel.remove_file('cache_bill.xlsx')
