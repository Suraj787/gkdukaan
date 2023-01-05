import frappe

def after_insert(doc,methode):
    if(doc.supplier_user):
        up = frappe.get_doc({
            "doctype": "User Permission",
            "user": doc.supplier_user,
            "allow": "Supplier",
            "for_value":doc.name
        })
        up.insert()
    
