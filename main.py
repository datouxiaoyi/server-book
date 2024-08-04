import uuid
import tornado.ioloop
import tornado.web
from alipay import AliPay
        
class NotifyHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')     
    async def post(self):
        price = self.get_argument('price')
        title = self.get_argument('title')

        alipay = self.alipay_obj()

        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=str(uuid.uuid4()), 
            total_amount=price,  
            subject=title,  
            return_url=None, 
            notify_url=None
        )
        url = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do' + '?' + order_string
        print(id, price, title)   
        self.write({"status": 1, "url": url})
        

    def alipay_obj(self):
        alipay = AliPay(
            appid="9021000137696045",
            app_notify_url=None,  
            app_private_key_string=open("private.txt").read(),
            alipay_public_key_string=open("public").read(),
            sign_type='RSA2',
            debug=False,
            verbose=False
        )
        return alipay
       

def main():
    app =  tornado.web.Application([
        (r"/create", NotifyHandler)        
    ], debug=True)
    app.listen(8888)    
    print("服务启动成功")
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()

    
