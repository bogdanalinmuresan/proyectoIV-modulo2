from mongodbforms import *
""""
class BaresForm(DocumentForm):
	class Meta:
		model=Bares
		fields=['nombre','direccion','nrvisitas']

class TapasForm(EmbeddedDocumentForm):
	class Meta:
		model=Tapas
		fields=['nombre','nrvotos']
"""
class UsuarioForm(DocumentForm):
	class Meta:
		model=Usuario
		fields=['username','email','password']

