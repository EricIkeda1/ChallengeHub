from django.db import models

class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    example_input = models.TextField()
    example_output = models.TextField()
    solution_code = models.TextField()
    difficulty = models.CharField(max_length=10, choices=[('Easy','Easy'),('Medium','Medium'),('Hard','Hard')])

    def __str__(self):
        return self.title

class Submission(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    code = models.TextField()
    correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission for {self.challenge.title}"
