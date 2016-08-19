{
    'name': 'Report Download Name',
    'version': '9.0.1.0',
    'depends': ['report'],
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Report',
    'description': 
    """
    It sets the PDF name correctly when downloading report.
    It generate the name by evaluating the attachment field of a report declaration.
    Don't forget the string '.pdf' at the end of attachment.
    Available variables for the attachment field: 
        - object (reports model)
        - time (Python library)
    
    Example: 
    "Timesheet report - "+object.name+" ("+time.strftime("%Y%m%d%H%M%S")+").pdf" 
    =>
    "Timesheet report - Contract NAME (20150414130953).pdf"

    Need to install 'simplejson'
    - apt-get install python-simplejson

    
    This module has been developed by Bernard Delhez, intern @ AbAKUS it-solutions, under the control of Valentin Thirion.    
    This module is inspired by the module from Nicolas Brisac: https://github.com/oasiswork/odoo-report-download-name/
    """,
    'data': [],
}
