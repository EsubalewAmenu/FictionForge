from django.db import models

class Persona(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

        
class Query(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    user_query = models.TextField()
    generated_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query ({self.persona.name}): {self.user_query[:30]}"
