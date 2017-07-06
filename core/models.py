from django.db import models
from django.contrib.auth.models import Permission, User
from django.utils import timezone


class Music(models.Model):
	user = models.ForeignKey(User, null=False, blank=False, related_name='+')
	age = models.IntegerField(verbose_name='Idade', null=False, blank=False)
	city = models.CharField(max_length=80, verbose_name='Cidade', null=False, blank=False)
	style = models.CharField(max_length=80, verbose_name='Estilo musical', null=False, blank=False)
	instrument = models.CharField(max_length=80, verbose_name='Instrumento', null=False, blank=False)
	state = models.CharField(max_length=80, verbose_name='Estado', null=False, blank=False)
	adress = models.CharField(max_length=100, verbose_name='Endereço', null=False, blank=False)
	phone = models.CharField(max_length=12, verbose_name='Telefone', null=True, blank=True)
	face = models.CharField(max_length=20, verbose_name='Facebook', null=True, blank=True)
	twitter = models.CharField(max_length=20, verbose_name='Twitter', null=True, blank=True)
	insta = models.CharField(max_length=20, verbose_name='Instagram', null=True, blank=True)
	video = models.CharField(max_length=20, verbose_name='Video', null=True, blank=True)

	def __str__(self):
		return 'Dados de ' + self.user.username

class ImageData(models.Model):
	user = models.ForeignKey(User, null=False, blank=False, related_name='+')
	profile = models.FileField(upload_to='profile/', null=True, blank=True)
	cover = models.FileField(upload_to='cover/', null=True, blank=True)
	
	def __str__(self):
		return 'Dados de ' + self.user.username

class Message(models.Model):
	emissor = models.ForeignKey(User, related_name='+')
	receptor = models.ForeignKey(User)
	data = models.DateTimeField(default=timezone.now)
	texto = models.TextField(verbose_name='Mensagem')
	visualisada = models.BooleanField(default=False)

	def __str__(self):
		return 'Mensagem de ' + self.emissor.username+' para '+self.receptor.username

	def count_messages(self, user_loged):
		print("Contando mensagens")
		tam = 0
		for message in self.get_users_recently(user_loged):
			if message[2] == False:
				tam += 1
		return tam

	def get_users_recently(self, user_loged):
		l = list()

		for user_visited in User.objects.all():
			if self.get_ultimate_message(user_loged, user_visited):
				read = True
				if self.get_ultimate_message(user_loged, user_visited).emissor != user_loged and self.get_ultimate_message(user_loged, user_visited).visualisada == False:read = False
				l.append([user_visited, self.get_ultimate_message(user_loged, user_visited), read])
		return sorted((sorted(l, key=lambda inst: inst[1].data)[::-1]), key=lambda inst: inst[1].visualisada)

	def get_ultimate_message(self, user_loged, user_visited):
		ms = list()

		mlog = Message.objects.filter(emissor=user_loged, receptor=user_visited)
		mvis = Message.objects.filter(emissor=user_visited, receptor=user_loged)

		for m in mlog:ms.append(m)
		for m in mvis:ms.append(m)

		if len(ms) == 0:return False

		return sorted(ms, key=lambda inst: inst.data)[-1]

	def get_all_messages(self, usuarioLogado, usuarioVisitado):
		ms = list()
		instanciaParaRecuperarData = Profile()

		mlog = Message.objects.filter(emissor=usuarioLogado, receptor=usuarioVisitado)
		mvis = Message.objects.filter(emissor=usuarioVisitado, receptor=usuarioLogado)

		for m in mlog:ms.append(m)
		for m in mvis:
			if m.visualisada == False:
				m.visualisada = True
				m.save()
			ms.append(m)

		lista =  sorted(ms, key=lambda inst: inst.data)

		json = []

		for msg in lista:
			if msg.emissor == usuarioLogado:
				a = [0, msg.texto, instanciaParaRecuperarData.formataDataChat(msg.data)]
			else:
				a = [1, msg.texto, instanciaParaRecuperarData.formataDataChat(msg.data)]
			json.append(a)
		return json

	def get_20_messages(self, usuarioLogado, usuarioVisitado):
		ms = list()

		mlog = Message.objects.filter(emissor=usuarioLogado, receptor=usuarioVisitado)
		mvis = Message.objects.filter(emissor=usuarioVisitado, receptor=usuarioLogado)

		for m in mlog:ms.append(m)
		for m in mvis:
			if m.visualisada == False:
				m.visualisada = True
				m.save()
			ms.append(m)

		return sorted(ms, key=lambda inst: inst.data)

	def get_messages_not_view(self, usuarioLogado, usuarioVisitado):
		a = list()
		mvis = Message.objects.filter(emissor=usuarioVisitado, receptor=usuarioLogado)

		for m in mvis:
			if m.visualisada == False:
				a.append(([m.texto], ["{}/{} - {}:{}:{}".format(m.data.month, m.data.day, m.data.hour, m.data.minute, m.data.second)]))
		return a

	def set_le_mensagens(self, usuarioLogado, usuarioVisitado):
		mvis = Message.objects.filter(emissor=usuarioVisitado, receptor=usuarioLogado)
		for m in mvis:
			if m.visualisada == False:
				m.visualisada = True
				m.save()
		return True

	def send_message(self, usuarioLogado, usuarioVisitado, mensagem):
		newMessage = Message()
		newMessage.texto = mensagem
		newMessage.emissor = usuarioLogado
		newMessage.receptor = usuarioVisitado
		newMessage.save()
		return True

	def verifica_leitura_de_msg(self, usuarioLogado, usuarioVisitado):
		ms = list()

		mlog = Message.objects.filter(emissor=usuarioLogado, receptor=usuarioVisitado)
		mvis = Message.objects.filter(emissor=usuarioVisitado, receptor=usuarioLogado)

		for m in mlog:ms.append(m)
		for m in mvis:ms.append(m)

		if len(ms) == 0:return False

		ultimamsg = sorted(ms, key=lambda inst: inst.data)[-1]
		if ultimamsg.emissor == usuarioLogado and ultimamsg.visualisada == True:
			return True
		return False

	def delete_messages(self, usuarioLogado, usuarioVisitado):
		Message.objects.filter(emissor=usuarioLogado, receptor=usuarioVisitado).delete()
		Message.objects.filter(emissor=usuarioVisitado, receptor=usuarioLogado).delete()
		return True