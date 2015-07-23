from infusionsoft.library import Infusionsoft
import datetime
from lyl9_bg.models import Contact,Invoice,Payment,Order,ItemOrder

class InfusionsoftApiConnector:

    infusionClient = Infusionsoft('loyal9rev', 'fa6eed2e131518baeee521f66e9e91fa')
    resultsPerPage = 1000

    def getContactDataByDate(self, date, page ):
        return self.infusionClient.DataService('query', 'Contact', self.resultsPerPage, page, {'LastUpdated': date},
                                                   ['Id', 'FirstName', 'LastName', 'Phone1', 'Company'])

    def syncContactData(self):
        page = 0

        date = datetime.datetime.now().strftime("%Y-%m-%d") + '%'

        contactData = self.getContactDataByDate(date, page)

        while contactData:
            for contact in contactData:
                tContact = Contact.objects.filter(CrmId=contact['Id'])
                if tContact.exists():
                    tContact.update(FirstName=contact['FirstName'], LastName=contact['LastName'],
                                        PhoneNumber=contact['Phone1'], Company=contact['Company'])
                else:
                    if 'LastName' not in contact:
                        contact['LastName'] = ""
                    if 'FirstName' not in contact:
                        contact['FirstName'] = ""
                    if 'Phone1' not in contact:
                        contact['Phone1'] = ""
                    if 'Company' not in contact:
                        contact['Company'] = ""
                    tContact = Contact(FirstName=contact['FirstName'], LastName=contact['LastName'],
                                            PhoneNumber=contact['Phone1'], Company=contact['Company'], CrmId=contact['Id'])
                    tContact.save()

            page = page + 1
            contactData = self.getContactDataByDate(date, page)
            print("Contact Synced\n")

    def getInvoiceDataByDate(self, date, page ):
        return self.infusionClient.DataService('query', 'Invoice', self.resultsPerPage, page, {'DateCreated': date},
                                                   ['Id', 'ContactId', 'InvoiceTotal', 'RefundStatus', 'TotalDue',
                                                       'TotalPaid', 'DateCreated'])


    def syncInvoiceData(self):
        page = 0

        date = datetime.datetime.now().strftime("%Y-%m-%d") + '%'

        invoiceData = self.getInvoiceDataByDate(date, page)

        while invoiceData:
            for invoice in invoiceData:
                tInvoice = Invoice.objects.filter(InvoiceId=invoice['Id'])
                if not tInvoice.exists():
                   tInvoice = Contact(ContactId=invoice['ContactId'], TotalPaid=invoice['TotalPaid'],
                                            TotalDue=invoice['TotalDue'], InvoiceId=invoice['Id'],
                                            InvoiceTotal=invoice['InvoiceTotal'], RefundStatus=invoice['RefundStatus'],
                                            DateCreated=invoice['DateCreated'])
                   tInvoice.save()
                   print("Invoice inserted\n")

            page = page + 1
            invoiceData = self.getInvoiceDataByDate(date, page)
        print("Invoice Synced\n")

    def getPaymentData(self, page):
        return self.infusionClient.DataService('query', 'Payment', self.resultsPerPage, page, {},
                                                   ['Id','UserId','PayAmt','InvoiceId'])
    def syncPaymentData(self):
        page = 0

        paymentData = self.getPaymentData(page)

        while paymentData:
            for payment in paymentData:
                tPayment= Payment.objects.filter(PaymentId=payment['Id'])
                if not tPayment.exists():
                   tPayment = Payment(PaymentId=payment['Id'], UserId=payment['UserId'],
                                            PayAmt=payment['PayAmt'],InvoiceId=payment['InvoiceId'])
                   tPayment.save()

            page = page + 1
            paymentData = self.getPaymentData(page)
        print("Payment Synced\n")

    def getItemData(self, page):
        return self.infusionClient.DataService('query', 'InvoiceItem', self.resultsPerPage, page, {},
                                                   ['Id','OrderItemId','InvoiceId'])
    def syncItemData(self):
        page = 0

        itemData = self.getItemData(page)

        while itemData:
            for item in itemData:
                tItem= ItemOrder.objects.filter(ItemOrderId=item['Id'])
                if not tItem.exists():
                   tItem = ItemOrder(ItemOrderId=item['Id'],OrderItemId=item['OrderItemId'],InvoiceId=item['InvoiceId'])
                   tItem.save()

            page = page + 1
            itemData = self.getItemData(page)
        print("ItemOrder Synced\n")

    def getOrderData(self, page):
        return self.infusionClient.DataService('query', 'OrderItem', self.resultsPerPage, page, {},
                                                   ['Id','ProductId'])
    def syncOrderData(self):
        page = 0

        orderData = self.getOrderData(page)

        while orderData:
            for order in orderData:
                tOrder= Order.objects.filter(OrderId=order['Id'])
                if not tOrder.exists():
                   tOrder = Order(OrderId=order['Id'], ProductId=order['ProductId'])
                   tOrder.save()

            page = page + 1
            orderData = self.getOrderData(page)
        print("Order Synced\n")


    def sync(self):

        self.syncContactData()
        self.syncInvoiceData()
        self.syncPaymentData()
        self.syncItemData()
        self.syncOrderData()
        return True
