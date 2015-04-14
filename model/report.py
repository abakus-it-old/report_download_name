from openerp.osv import osv
import time
from openerp.tools.safe_eval import safe_eval as eval

class Report(osv.Model):
    _inherit = ["report"]
    _description = "Report"

    def _get_attachment_name_dict(self, cr, uid, ids, report):
        attachment = {}
        attachment['model'] = report.model

        if report.attachment:
            for record_id in ids:
                obj = self.pool[report.model].browse(cr, uid, record_id)
                try:
                    filename = eval(report.attachment, {'object': obj, 'time': time})
                    if filename:
                        attachment[record_id] = filename
                except:
                    pass

        return attachment
