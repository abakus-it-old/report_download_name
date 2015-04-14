import pdb
from openerp.addons.web.http import Controller, route, request
from openerp.addons.report.controllers.main import ReportController
from openerp.osv import osv
from openerp import http
import simplejson
import logging

#_logger = logging.getLogger(__name__)

class PTReportController(ReportController):
    @route(['/report/download'], type='http', auth="user")
    def report_download(self, data, token):
        requestcontent = simplejson.loads(data)
        url, type = requestcontent[0], requestcontent[1]
        response = ReportController().report_download(data, token)

        if type == 'qweb-pdf':
            reportname = url.split('/report/pdf/')[1].split('?')[0]
            #_logger.info('Getting attachment name for {}'.format(reportname))

            docids = None
            if '/' in reportname:
                reportname, docids = reportname.split('/')

            if docids:
                report_obj = request.registry['report']
                cr, uid, context = request.cr, request.uid, request.context
                report = report_obj._get_report_from_name(cr, uid, reportname)

                if ',' in docids:
                    ids = [int(docids.split(',')[0])]
                else:
                    ids = [int(docids)]
                #_logger.info('Found document id: {}'.format(ids[0]))

                attachment = report_obj._get_attachment_name_dict(cr, uid, ids, report)

                try:
                    #_logger.info('ids[0]: {}'.format(str(ids[0])))
                    filename = attachment[ids[0]]
                    response.headers.set('Content-Disposition', 'attachment; filename=%s;' % filename)
                except KeyError:
                    pass
                    """
                    if ids[0] in attachment['loaded_documents']:
                        _logger.info('Report is loaded from attachment')
                    else:
                        _logger.warning('No report filename found, using default')
                    """

        return response