from openerp.osv import osv
import time
import datetime
from pytz import timezone

class Report(osv.Model):
    _inherit = ["report"]
    _description = "Report"

    def _get_attachment_name_dict(self, cr, uid, ids, report):
        attachment = {}
        attachment['model'] = report.model
        local_tz = timezone('Europe/Brussels')
        now = datetime.datetime.now(local_tz).strftime("%Y%m%d%H%M%S")
        
        if report.attachment:
            for record_id in ids:
                obj = self.pool[report.model].browse(cr, uid, record_id)
                try:
                    filename = eval(report.attachment, {'object': obj, 'time': time, 'now': now})
                    attachment[record_id] = filename
                except:
                    pass

        return attachment
