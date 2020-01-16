from django.db import models




class Personne(models.Model):
    """
    Un artiste
    """
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    tel = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return '%s %s' % (self.prenom, self.nom)
        
class Groupe(models.Model):
    """
    Un groupe
    """
    nom = models.CharField(max_length=100)
    membre = models.ManyToManyField(Personne,blank=True)
    email = models.EmailField(max_length=254,blank=True)
    style = models.CharField(max_length=100,blank=True)
    domiciliation = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return '%s' % (self.nom)

class SensInstrument(models.Model):
    """
    Un instrument
    """
    sens = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.sens)
    
class Instrument(models.Model):
    """
    Un instrument
    """
    nom = models.CharField(max_length=100)
    membre = models.ManyToManyField(Personne,blank=True)

    def __str__(self):
        return '%s' % (self.nom)


class ModeleInstrument(models.Model):
    """
    Un instrument
    """
    nom = models.CharField(max_length=100)
    typeinstrument = models.ForeignKey(Instrument,blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % (self.nom)

class ExemplaireInstrument(models.Model):
    """
    un instrument appartenant à quelqu'un
    """
    personne = models.ForeignKey(Personne,blank=True, on_delete=models.PROTECT)
    modeleinstrument = models.ForeignKey(ModeleInstrument,blank=True, on_delete=models.PROTECT)
    sensinstrument = models.ForeignKey(SensInstrument,blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.modeleinstrument, self.personne)

class TypeSortie(models.Model):
    """
    Type de sortie d'un groupe
    """
    nom = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.nom)

class EtapeSortie(models.Model):
    """
    etape du cycle d'une sortie
    """
    nom = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.nom)
    

class CycleSortie(models.Model):
    """
    Avancement du cycle de la sortie en cours
    """
    nom = models.CharField(max_length=100)
    etapesortie = models.ForeignKey(EtapeSortie,blank=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return '%s' % (self.nom)

class Sortie(models.Model):
    """
    Une sortie d'un groupe
    """
    nom = models.CharField(max_length=100)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    typesortie = models.ForeignKey(TypeSortie,blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.groupe,self.nom)

class ReseauxSociauxPersonne(models.Model):
    """
    réseaux sociaux d'une personne
    """
    personne = models.OneToOneField(Groupe,blank=True, on_delete=models.PROTECT)
    facebook = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return 'Réseaux Sociaux - %s' % (self.personne)

class ReseauxSociauxGroupe(models.Model):
    """
    réseaux sociaux d'un groupe
    """
    groupe = models.OneToOneField(Groupe,blank=True, on_delete=models.PROTECT)
    facebook = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)
    bandcamp = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return 'Réseaux Sociaux - %s' % (self.groupe)
    
   
