import http.server
import socketserver
import subprocess
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	def _set_response(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
	def do_GET(self):
		if self.path == '/':
			self.path = 'index.html'
		return http.server.SimpleHTTPRequestHandler.do_GET(self)
	def do_POST(self):
		post_data = self.rfile.read(int(self.headers['Content-Length']))
		print(post_data)
		self._set_response()
		if "1" in str(post_data):
			self.wfile.write('<!DOCTYPE html><p>The scan will take a while\n</p></html>'.encode('utf-8'))
			rec=subprocess.call('./basic_nmap.sh')
			file=open('BasicScan.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		if "2" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./tcp_syn_nmap.sh')
			file=open('TCPSYNScan.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		if "3" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./tcp_ack_nmap.sh')
			file=open('TCPACKScan.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		if "4" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./aggressive_nmap.sh')
			file=open('AggressiveScan.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))

		if "5" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./service_nmap.sh')
			file=open('ServiceScan.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))

		if "6" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./uniscans.sh')
			file=open('Uni_Scan.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		if "7" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./niktoscans.sh')
			file=open('niktoScan.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		if "8" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./VulnerableJSDependency.sh')
			file=open('BurpJSDep.txt','r')
			ok=file.read()
			ok=ok.replace('<',' ')
			ok=ok.replace('>',' ')
			ok=ok.replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		if "9" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./HTTPParamPollute.sh')
			file=open('HTTPPollute.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		if "0" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./transportSecurity.sh')
			file=open('TransportSec.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>'))
		if "p" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./SourceCode.sh')
			file=open('Source.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		if "q" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./cacheable.sh')
			file=open('cache.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))
		if "r" in str(post_data):
			self.wfile.write("The scan will take a while\n".encode('utf-8'))
			rc=subprocess.call('./robots.sh')
			file=open('robots.txt','r')
			ok=file.read().replace('\n','<br />')
			self.wfile.write(('<!DOCTYPE html><p>'+str(ok)+'</p></html>').encode('utf-8'))

handler_object = MyHttpRequestHandler

PORT = 80
my_server = socketserver.TCPServer(("",PORT),handler_object)

my_server.serve_forever()
