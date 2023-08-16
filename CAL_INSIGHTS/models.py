from django.db import models

class TeamLeader(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ACM(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    shift = models.CharField(max_length=50)
    team_leader = models.ForeignKey(TeamLeader, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Files(models.Model):
    client_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=100, decimal_places=2)
    account_name = models.CharField(max_length=100)
    termination_code = models.CharField(max_length=100)
    acm = models.ForeignKey(ACM, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client_name} - {self.product_name}"
