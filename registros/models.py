#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class Usuario(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	cedula = models.CharField(max_length=8)
	email = models.CharField(max_length=50)	

	def __unicode__(self):
		return self.nombre
