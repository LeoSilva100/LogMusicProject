from django.shortcuts import render, HttpResponse, redirect, Http404, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from .models import Music, ImageData, Message
from django.views.decorators.csrf import csrf_exempt
import json
import random

frases = ["Os músicos não se retiram; param quando não há mais música neles. – Louis Armstrong.",
		  "Os músicos têm a música, porque a música os têm a eles. – Virgil Thomson.",
		  "A música é a posse de todos. Apenas os anunciantes pensam que as pessoas possuem. – John Lennon.",
		  "A música é o mais forte ato social da comunicação entre as pessoas, um gesto de amizade o mais forte que há. – Malcolm Arnold.",
		  "Os músicos não deveriam tocar música. A música deveria tocar os músicos. – Henry Rollins.",
		  "A musica é uma revelação maior do que qualquer filosofia. – Ludwig van Beethoven.",
		  "A música pode nomear o inominável e comunicar o desconhecido. – Leonard Bernstein.",
		  "A música é a vida emocional da maioria das pessoas. – Leonard Cohen.",
		  "Triste e grande no entanto, é o destino do artista. – Franz Liszt.",
		  "A única história de amor que eu tive foi a música. – Maurice Ravel.",
		  "A verdadeira beleza da música é que ela conecta as pessoas. Ela leva uma mensagem e nós os músicos, somos os mensageiros. – Roy Ayers.",
		  "Os sábios são aqueles músicos que tocam o que eles podem dominar. – Duke Ellington.",
		  "A música é a minha religião. – Jimi Hendrix.",
		  "A música é sinônimo de liberdade, tocar o que quiser e como quiser, quando é bom e tem paixão, que a música é o alimento do amor. – Kurt D. Cobain.",
		  "A música não a tem de traduzir. Apenas afeta você e você não sabe o porquê. – David Byrne.",
		  "Tudo é música para o chato músico. – Romain Rolland.",
		  "Para conseguir grandes coisas, duas coisas são necessárias; um plano e não muito tempo. – Leonard Bernstein.",
		  "A música é um mundo em si mesmo, é uma linguagem que todos nós entendemos. – Stevie Wonder.",
		  "Os músicos tendem a ficar entediado tocando a mesma coisa uma e outra vez, então eu acho que é natural experimentar. – Dimebag Darrell.",
		  "Os artistas menores tomam emprestado, os grandes artistas roubam. – Igor Stravinsky."]

@login_required(login_url='/login')
def index(request):
	try:
		promusic = get_object_or_404(Music, user=request.user)
	except Exception as e:
		promusic = False

	instanciaMessage = Message()
	#quantidade de pessoas que mandaram mensagens
	quantidade_mensagens = instanciaMessage.count_messages(request.user)
	return render(request, 'index.html',{'promusic':promusic, 'quantidade':quantidade_mensagens, 'frase':random.choice(frases)})

def login_page(request):
	if request.user.is_authenticated(): return index(request)
	return render(request, 'login.html')

def entrar(request):
	if request.method == 'POST' and request.is_ajax():
		user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps(True), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404


def register(request):
	if request.method == 'POST' and request.is_ajax():
		userInstance = User()
		userInstance.username = request.POST.get('username')
		userInstance.email = request.POST.get('email')
		passw = request.POST.get('password')
		userInstance.set_password(passw)
		userInstance.save()
		print("user: "+ userInstance.username)
		print("senha: "+ passw)
		new_image_data = ImageData()
		new_image_data.user = userInstance
		new_image_data.save()
		user = authenticate(username=userInstance.username, password=passw)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse(json.dumps(True), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

@csrf_exempt
def create_profile(request):
	if request.POST.get('age') ==  request.POST.get('city') == request.POST.get('style') == request.POST.get('instrument') == request.POST.get('state') == "":
		return HttpResponse(json.dumps(False), content_type="application/json")	
	if request.method == 'POST':
		try:
			promusic = get_object_or_404(Music, user=request.user)
			promusic.age = request.POST.get('age')
			promusic.city = request.POST.get('city')
			promusic.style = request.POST.get('style')
			promusic.instrument = request.POST.get('instrument')
			promusic.state = request.POST.get('state')
			promusic.adress = request.POST.get('adress')
			promusic.phone = request.POST.get('phone')
			promusic.face = request.POST.get('face')
			promusic.insta = request.POST.get('insta')
			promusic.twitter = request.POST.get('twitter')
			promusic.video = request.POST.get('video')
			promusic.user = request.user
			promusic.save()
			return HttpResponse(json.dumps(True), content_type="application/json")
		except Exception as e:
			print(e)
			try:
				promusic = Music()
				promusic.age = request.POST.get('age')
				promusic.city = request.POST.get('city')
				promusic.style = request.POST.get('style')
				promusic.instrument = request.POST.get('instrument')
				promusic.state = request.POST.get('state')
				promusic.adress = request.POST.get('adress')
				promusic.phone = request.POST.get('phone')
				promusic.face = request.POST.get('face')
				promusic.insta = request.POST.get('insta')
				promusic.twitter = request.POST.get('twitter')
				promusic.video = request.POST.get('video')
				promusic.user = request.user
				promusic.save()
				return HttpResponse(json.dumps(True), content_type="application/json")
			except Exception as e:
				print(e)
				return HttpResponse(json.dumps(False), content_type="application/json")		
	raise Http404

def make_logout(request):	
	logout(request)
	return redirect("/")

def delete_profile(request):	
	get_object_or_404(Music, user=request.user).delete()
	return redirect("/")

def profile(request, username):
	user = get_object_or_404(User, username=username)	
	puser = get_object_or_404(Music, user=user)
	return render(request, 'profile.html',{'puser':puser,'frase':random.choice(frases)})

def deletaconta(request):
	if request.is_ajax():
		get_object_or_404(ImageData, user=request.user).delete()
		request.user.delete()
		return HttpResponse(json.dumps(True), content_type="application/json")
	raise Http404

def search_users(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('message') != "":
				argument = request.POST.get('message')
				users = User.objects.filter(username__icontains=argument)
				print(users)
				return HttpResponse(json.dumps(list(users.values('username','pk', 'email'))), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def edit_profile(request):
	if request.method == 'POST' and request.is_ajax():
		try:
			if request.POST.get('username') != "" and request.POST.get('email') != "":
				#print(request.POST.get('name') + request.POST.get('server') + request.POST.get('user') + request.POST.get('password') + request.POST.get('portws'))

				request.user.username = request.POST.get('username')
				request.user.email = request.POST.get('email')
				request.user.save()
				dataimage = get_object_or_404(ImageData, user=request.user)
				dataimage.profile = request.FILES.get('profile')
				dataimage.cover = request.FILES.get('cover')
				dataimage.save()
				#houseInstance.save()
				return HttpResponse(json.dumps(True), content_type="application/json")
			return HttpResponse(json.dumps(False), content_type="application/json")
		except Exception as e:
			print(e)
			return HttpResponse(json.dumps(False), content_type="application/json")
	raise Http404

def sala(request, pkreceptor):
	eu = get_object_or_404(Music, user=request.user)
	instanciaMessage = Message()
	userVisitado = get_object_or_404(User, pk=pkreceptor)
	profileVisitado = get_object_or_404(Music, user=userVisitado)
	if request.user == userVisitado:
		raise Http404
	mensagens = instanciaMessage.get_20_messages(request.user, userVisitado)


	return render(request, 'conversa.html', {'mensagens':mensagens, 'profileVisitado':profileVisitado, 'puser':eu, 'frase':random.choice(frases)})


def send_message(request, pkreceptor):
	if request.method == 'POST':
		mensagem = request.POST.get('id')
		print(mensagem)
		instanciaMessage = Message()
		userVisitado = get_object_or_404(User, pk=pkreceptor)
		get_object_or_404(Music, user=userVisitado)
		if request.user == userVisitado:
			raise Http404
		resultado = instanciaMessage.send_message(request.user, userVisitado, mensagem)
		return HttpResponse(json.dumps(resultado), content_type="application/json")
	return HttpResponse(json.dumps(False), content_type="application/json")

def deleta_conversa(request):
	if not request.user.is_authenticated():
		return render(request, 'core/login.html')
	else:
		if request.method == 'POST':
			idvi = request.POST.get('id')
			instanciaMessage = Message()
			userVisitado = get_object_or_404(User, pk=idvi)
			if request.user == userVisitado:
				raise Http404
			resultado = instanciaMessage.delete_messages(request.user, userVisitado)
			return HttpResponse(json.dumps(resultado), content_type="application/json")
		return HttpResponse(json.dumps(False), content_type="application/json")

def my_contacts(request):
	eu = get_object_or_404(Music, user=request.user)

	instanciaMessage = Message()
	quantidade_mensagens = instanciaMessage.count_messages(request.user)
	contatos_recentes = instanciaMessage.get_users_recently(request.user)
	return render(request, 'mycontacts.html', {'puseu':eu, 'quantidade_mensagens':quantidade_mensagens, 'contatos_recentes':contatos_recentes, 'frase':random.choice(frases)})